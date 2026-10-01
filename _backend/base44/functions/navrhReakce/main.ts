import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';

// Reakce klienta Studentských Webů z pruhu na /navrhy/<id> (404.html).
// Uloží LeadInquiry a pošle upozornění na info.webhunter@email.cz — předmět začíná
// „Zdarma web od studentů – reakce na návrh“, aby ho zachytil hlídač pošty SW (~/sw-ops/watcher.py).
// Přijímá jen návrhy ze seznamu navrhy/sw.json (tools/sw_navrhy.py); ostatní návrhy odmítne.

const SW_LIST = 'https://webhunter.cz/navrhy/sw.json';
const TO = 'info.webhunter@email.cz';
const TYPES: Record<string, { status: string; label: string }> = {
  pokracovat: { status: 'navrh_pokracovat', label: 'Líbí se mi, chci pokračovat' },
  zmena: { status: 'navrh_zmena', label: 'Chci něco změnit' },
};
const MIN_GAP_MS = 2 * 60 * 1000;   // jedna reakce na návrh za 2 minuty
const DAY_MAX = 10;                 // nejvýš 10 reakcí na návrh za 24 h

const ts = (d: string) => Date.parse(/[zZ]|[+-]\d\d:\d\d$/.test(d) ? d : d + 'Z');

Deno.serve(async (req) => {
  try {
    const base44 = createClientFromRequest(req);
    const body = await req.json().catch(() => ({}));
    if (body.hp) return Response.json({ success: true }); // honeypot vyplnil robot – tváříme se, že prošlo

    const id = String(body.id || '');
    const t = TYPES[String(body.typ || '')];
    const text = String(body.text || '').trim().slice(0, 2000);
    const test = body.test === true;
    if (!/^[a-f0-9]{24}$/.test(id) || !t) return Response.json({ error: 'bad_request' }, { status: 400 });
    if (body.typ === 'zmena' && !text) return Response.json({ error: 'empty' }, { status: 400 });

    const list = await fetch(SW_LIST + '?t=' + Date.now()).then((r) => (r.ok ? r.json() : null)).catch(() => null);
    if (!list || !Array.isArray(list.ids) || !list.ids.includes(id)) return Response.json({ error: 'not_sw' }, { status: 404 });

    const db = base44.asServiceRole.entities;
    const p = await db.Proposal.get(id).catch(() => null);
    if (!p) return Response.json({ error: 'not_found' }, { status: 404 });

    const recent = await db.LeadInquiry.filter({ company: id }, '-created_date', DAY_MAX).catch(() => []);
    const now = Date.now();
    if (recent[0] && now - ts(recent[0].created_date) < MIN_GAP_MS) return Response.json({ error: 'rate' }, { status: 429 });
    if (recent.length >= DAY_MAX && now - ts(recent[DAY_MAX - 1].created_date) < 864e5) return Response.json({ error: 'rate' }, { status: 429 });

    const link = 'https://webhunter.cz/navrhy/' + id;
    const name = String(p.name || id).replace(/\s+/g, ' ').slice(0, 90);
    const when = new Date().toLocaleString('cs-CZ', { timeZone: 'Europe/Prague' });
    const subject = `Zdarma web od studentů – reakce na návrh: ${t.label} (${name})${test ? ' – TEST' : ''}`;
    const message = `Reakce: ${t.label} (${t.status})\nNávrh: ${name}\nOdkaz: ${link}\n\n${text || '(bez textu)'}`;
    const emailText = `${test ? 'TEST – nejde o skutečnou reakci klienta, neodpovídat.\n\n' : ''}Klient Studentských Webů reagoval přímo na stránce se svým návrhem.

Reakce: ${t.label}
Návrh: ${name}
Odkaz: ${link}
Web návrhu: ${p.url || '—'}
ID návrhu: ${id}

Zpráva od klienta:
${text || '(bez textu – jen kliknul na tlačítko)'}

Klienta najdete v CRM Studentských Webů podle pole proposal_link, které obsahuje ${id}.
Odesláno: ${when}`;

    const key = Deno.env.get('RESEND_API_KEY');
    if (!key) return Response.json({ error: 'mail_not_configured' }, { status: 500 });
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: 'noreply@webhunter.cz', to: TO, subject, text: emailText }),
    });
    if (!r.ok) return Response.json({ error: 'mail', detail: await r.text() }, { status: 502 });

    const rec = await db.LeadInquiry.create({
      name: `${test ? 'TEST – ' : ''}Reakce na návrh: ${name}`,
      company: id,
      email: '',
      phone: '',
      message,
      status: t.status,
    }).catch((e: Error) => { console.error('LeadInquiry:', e.message); return null; });

    return Response.json({ success: true, id: rec ? rec.id : null });
  } catch (error) {
    return Response.json({ error: (error as Error).message }, { status: 500 });
  }
});
