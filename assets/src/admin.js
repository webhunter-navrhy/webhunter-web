/* WebHunter — hidden admin tools (loaded on demand after a triple-click in the footer).
   IČO → Návrhy (Proposal) · © → Analytika (LandingPageMetric) · WebHunter s.r.o. → Poptávky (LeadInquiry)
   Backend: Base44 app 6a366c8ba95efe01593d4844 (same data as the previous site). */
(() => {
  const APP = '6a366c8ba95efe01593d4844';
  const API = 'https://base44.app/api/apps/' + APP + '/entities/';
  const H = { 'Content-Type': 'application/json', 'X-App-Id': APP };
  const PUBLIC_BASE = 'https://webhunter.cz'; // copied links must stay 1:1 with the previous site
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const el = (html) => { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; };
  const fmtDate = s => { try { return new Date(s.endsWith('Z') || s.includes('+') ? s : s + 'Z').toLocaleString('cs-CZ', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }); } catch (e) { return '—'; } };
  const toDate = s => new Date(s && (s.endsWith('Z') || s.includes('+')) ? s : s + 'Z');
  const nf = new Intl.NumberFormat('cs-CZ');

  const db = {
    async list(ent, { sort = '-created_date', limit = 50, skip = 0, q = null, fields = null } = {}) {
      const p = new URLSearchParams({ sort, limit, skip }); if (q) p.set('q', JSON.stringify(q)); if (fields) p.set('fields', fields);
      const r = await fetch(API + ent + '?' + p, { headers: H }); if (!r.ok) throw new Error('HTTP ' + r.status); return r.json();
    },
    async all(ent, sort = '-created_date') { let out = [], skip = 0; for (;;) { const b = await this.list(ent, { sort, limit: 5000, skip }); out = out.concat(b); if (b.length < 5000) return out; skip += 5000; } },
    async create(ent, data) { const r = await fetch(API + ent, { method: 'POST', headers: H, body: JSON.stringify(data) }); if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); },
    async update(ent, id, data) { const r = await fetch(API + ent + '/' + id, { method: 'PUT', headers: H, body: JSON.stringify(data) }); if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); },
    async del(ent, id) { const r = await fetch(API + ent + '/' + id, { method: 'DELETE', headers: H }); if (!r.ok) throw new Error('HTTP ' + r.status); }
  };

  /* ---------- modal shell ---------- */
  let current = null;
  function shell(title, sub, wide) {
    close();
    const m = el(`<div class="wa-ov" data-lenis-prevent role="dialog" aria-modal="true" aria-label="${esc(title)}">
      <div class="wa-box ${wide ? 'wa-wide' : ''}">
        <header class="wa-head"><div><h2>${esc(title)}</h2><p class="wa-sub">${sub || ''}</p></div><div class="wa-head-act"></div><button class="wa-x" aria-label="Zavřít">✕</button></header>
        <div class="wa-body"></div>
      </div></div>`);
    document.body.appendChild(m); document.documentElement.classList.add('wa-lock');
    m.querySelector('.wa-x').addEventListener('click', close);
    m.addEventListener('click', e => { if (e.target === m) close(); });
    current = m; return { root: m, body: m.querySelector('.wa-body'), act: m.querySelector('.wa-head-act'), sub: m.querySelector('.wa-sub') };
  }
  function close() { if (current) { current.remove(); current = null; document.documentElement.classList.remove('wa-lock'); if (window.__waTimer) { clearInterval(window.__waTimer); window.__waTimer = null; } } }
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && current) close(); });
  const copy = async (text, btn) => {
    try { await navigator.clipboard.writeText(text); } catch (e) { const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); document.execCommand('copy'); t.remove(); }
    if (btn) { const o = btn.textContent; btn.textContent = 'Zkopírováno ✓'; btn.classList.add('ok'); setTimeout(() => { btn.textContent = o; btn.classList.remove('ok'); }, 1400); }
  };

  /* =================================================================
     NÁVRHY (Proposal) — 1:1 with the previous site
     ================================================================= */
  function proposals() {
    const s = shell('Návrhy', 'Nahrajte návrh a zkopírujte odkaz ve tvaru webhunter.cz/navrhy/…');
    s.body.innerHTML = `
      <form class="wp-form">
        <label><span>Název</span><input name="name" required placeholder="Např. Prodej bytu 3+1 — Vršovice"></label>
        <label><span>URL návrhu</span><input name="url" type="url" required placeholder="https://…"></label>
        <button class="wa-btn wa-btn-dark" type="submit">Přidat návrh</button>
      </form>
      <div class="wp-tools"><input class="wp-search" type="search" placeholder="Hledat podle názvu, URL nebo ID…" aria-label="Hledat návrhy"><span class="wp-count"></span></div>
      <ul class="wp-list"></ul>
      <div class="wp-more"><button class="wa-btn" type="button" hidden>Načíst další</button></div>`;
    const list = s.body.querySelector('.wp-list'), more = s.body.querySelector('.wp-more button'), count = s.body.querySelector('.wp-count');
    const form = s.body.querySelector('.wp-form'), search = s.body.querySelector('.wp-search');
    let skip = 0, q = null, loading = false;
    const row = p => el(`<li class="wp-row"><div class="wp-main"><b>${esc(p.name)}</b><a href="${esc(p.url)}" target="_blank" rel="noopener">${esc(p.url)}</a><small>${fmtDate(p.created_date)}</small></div>
      <div class="wp-act"><a class="wa-btn" href="${PUBLIC_BASE}/navrhy/${esc(p.id)}" target="_blank" rel="noopener">Otevřít</a><button class="wa-btn wa-btn-lime" data-copy="${PUBLIC_BASE}/navrhy/${esc(p.id)}">Kopírovat</button></div></li>`);
    async function load(reset) {
      if (loading) return; loading = true;
      if (reset) { skip = 0; list.innerHTML = '<li class="wa-empty">Načítám…</li>'; }
      try {
        const b = await db.list('Proposal', { limit: 50, skip, q });
        if (reset) list.innerHTML = '';
        b.forEach(p => list.appendChild(row(p))); skip += b.length;
        more.hidden = b.length < 50;
        if (!list.children.length) list.innerHTML = '<li class="wa-empty">Nic nenalezeno.</li>';
        count.textContent = q ? `${nf.format(skip)}${b.length < 50 ? '' : '+'} výsledků` : `zobrazeno ${nf.format(skip)}`;
      } catch (e) { list.innerHTML = '<li class="wa-empty">Načtení se nepovedlo. Zkuste to znovu.</li>'; }
      loading = false;
    }
    list.addEventListener('click', e => { const b = e.target.closest('[data-copy]'); if (b) copy(b.dataset.copy, b); });
    more.addEventListener('click', () => load(false));
    let tmr; search.addEventListener('input', () => { clearTimeout(tmr); tmr = setTimeout(() => {
      const raw = search.value.trim(), v = raw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      // name search is fast; URL / id search only when the input looks like one
      q = !raw ? null : /^[0-9a-f]{24}$/i.test(raw) ? { id: raw } : (/[\/.:]/.test(raw) || /^\d{4,}$/.test(raw)) ? { url: { $regex: v, $options: 'i' } } : { name: { $regex: v, $options: 'i' } };
      list.innerHTML = '<li class="wa-empty">Hledám…</li>'; load(true);
    }, 300); });
    form.addEventListener('submit', async e => {
      e.preventDefault(); const btn = form.querySelector('button'); btn.disabled = true;
      try {
        const p = await db.create('Proposal', { name: form.name.value.trim(), url: form.url.value.trim() });
        form.reset(); const r = row(p); r.classList.add('wp-new'); list.prepend(r);
        const cb = r.querySelector('[data-copy]'); copy(cb.dataset.copy, cb);
      } catch (x) { alert('Návrh se nepodařilo uložit.'); }
      btn.disabled = false;
    });
    load(true);
    // total count (cheap: fetch ids only is not supported → estimate by paging in the background)
    (async () => { try { let n = 0, sk = 0; for (;;) { const b = await db.list('Proposal', { limit: 5000, skip: sk, sort: 'created_date', fields: 'id' }); n += b.length; if (b.length < 5000) break; sk += 5000; } if (current === s.root) s.sub.textContent = `Celkem ${nf.format(n)} návrhů · odkazy ve tvaru webhunter.cz/navrhy/…`; } catch (e) {} })();
  }

  /* =================================================================
     POPTÁVKY (LeadInquiry) — like the previous site
     ================================================================= */
  function leads() {
    const s = shell('Poptávky', 'Poptávky z kontaktního formuláře');
    const ST = { new: 'Nová', contacted: 'Kontaktováno', closed: 'Uzavřeno' };
    s.body.innerHTML = '<ul class="wl-list"><li class="wa-empty">Načítám…</li></ul>';
    const list = s.body.querySelector('.wl-list');
    async function load() {
      try {
        const b = await db.list('LeadInquiry', { limit: 200 });
        s.sub.textContent = `${b.length} poptávek · ${b.filter(x => x.status === 'new').length} nových`;
        list.innerHTML = b.length ? '' : '<li class="wa-empty">Zatím žádné poptávky.</li>';
        b.forEach(l => list.appendChild(el(`<li class="wl-row" data-id="${esc(l.id)}">
          <div class="wl-top"><b>${esc(l.name || '—')}</b>${l.company ? `<span>${esc(l.company)}</span>` : ''}<small>${fmtDate(l.created_date)}</small></div>
          <div class="wl-contact">${l.email ? `<a href="mailto:${esc(l.email)}">${esc(l.email)}</a>` : ''}${l.phone ? `<a href="tel:${esc(l.phone)}">${esc(l.phone)}</a>` : ''}${l.landing ? `<span class="wa-tag">${esc(l.landing)}</span>` : ''}</div>
          ${l.message ? `<p>${esc(l.message)}</p>` : ''}
          <div class="wl-act">${Object.entries(ST).map(([k, v]) => `<button class="wa-chip ${l.status === k ? 'on' : ''}" data-st="${k}">${v}</button>`).join('')}<button class="wa-btn wa-btn-del" data-del>Smazat</button></div>
        </li>`)));
      } catch (e) { list.innerHTML = '<li class="wa-empty">Načtení se nepovedlo.</li>'; }
    }
    list.addEventListener('click', async e => {
      const li = e.target.closest('.wl-row'); if (!li) return;
      const st = e.target.closest('[data-st]'), del = e.target.closest('[data-del]');
      if (st) { await db.update('LeadInquiry', li.dataset.id, { status: st.dataset.st }).catch(() => {}); load(); }
      if (del) {
        if (del.dataset.confirm) { await db.del('LeadInquiry', li.dataset.id).catch(() => {}); load(); }
        else { del.dataset.confirm = 1; del.textContent = 'Opravdu smazat?'; setTimeout(() => { if (del.isConnected) { delete del.dataset.confirm; del.textContent = 'Smazat'; } }, 3000); }
      }
    });
    load();
  }

  /* =================================================================
     ANALYTIKA (LandingPageMetric)
     ================================================================= */
  const C1 = '#2a78d6', C2 = '#eb6834';
  const SEQ = ['#eef4fd', '#cde2fb', '#9ec5f4', '#6da7ec', '#3987e5', '#256abf', '#184f95', '#0d366b'];
  const SEC_LABEL = { top: 'Úvod (hero)', realizace: 'Realizace', proces: 'Jak to funguje', sluzby: 'Co dostanete', geo: 'AI vyhledávání', tym: 'Tým', faq: 'Otázky', kontakt: 'Kontakt / formulář', paticka: 'Patička',
    hero: 'Úvod (hero)', benefits: 'Výhody', process: 'Proces', portfolio: 'Portfolio', contact: 'Kontakt' };
  const EV_LABEL = { cta: 'Tlačítka (CTA)', out: 'Prokliky na weby klientů', faq: 'Otevřené otázky', tel: 'Kliknutí na telefon', mail: 'Kliknutí na e-mail', ba: 'Přepnutí předtím/teď', filter: 'Filtry realizací', nav: 'Navigace', showcase: 'Vybrané realizace', hero_form: 'Pole v úvodu', form_start: 'Začal vyplňovat formulář', lead: 'Odeslaná poptávka' };
  const pageLabel = (path, legacy) => {
    const p = (path || '/').replace(/index\.html$/, '').replace(/\/+$/, '/') || '/';
    if (legacy) return 'Starý web ' + p;
    if (p === '/' || p === '') return 'Úvod';
    if (/realizace/.test(p)) return 'Realizace';
    if (/ochrana-osobnich-udaju/.test(p)) return 'Ochrana údajů';
    if (/navrhy/.test(p)) return 'Návrhy';
    return p;
  };
  function normalize(r) {
    let d = null; const sv = r.sections_viewed || '';
    if (sv && sv[0] === '{') { try { d = JSON.parse(sv); } catch (e) {} }
    let host = '', path = '/'; try { const u = new URL(r.entry_url); host = u.hostname; path = u.pathname; } catch (e) {}
    const legacy = !d;
    const t = toDate(r.created_date);
    return {
      id: r.id, t, upd: toDate(r.updated_date || r.created_date), host, url: r.entry_url, path: d ? d.path : path, legacy,
      page: pageLabel(d ? d.path : path, legacy), src: r.source || 'direct', dev: r.device || 'desktop', dur: Math.min(+r.duration_seconds || 0, 1800), scroll: +r.scroll_depth_max || 0,
      conv: !!r.submitted_form, sid: r.session_id || r.id, vid: d ? d.vid : (r.session_id || r.id), isNew: d ? !!d.new : null, ns: d ? d.ns : null,
      br: d ? d.br : '—', os: d ? d.os : '—', lang: d ? d.lang : '—', scr: d ? d.scr : '—', tz: d ? d.tz : '—', ref: d ? d.ref : '', utm: d ? d.utm || {} : {},
      secs: d ? d.secs || [] : sv ? sv.split(',').filter(Boolean) : [], ev: d ? d.ev || [] : [], vit: d ? d.vit || {} : {}
    };
  }
  const countBy = (rows, fn) => { const m = new Map(); rows.forEach(r => { const k = fn(r); if (k == null || k === '') return; (Array.isArray(k) ? k : [k]).forEach(x => m.set(x, (m.get(x) || 0) + 1)); }); return [...m.entries()].sort((a, b) => b[1] - a[1]); };
  const uniq = (rows, fn) => new Set(rows.map(fn)).size;
  const pct = (a, b) => b ? Math.round(a / b * 1000) / 10 : 0;
  const q75 = arr => { const a = arr.filter(x => x != null && !isNaN(x)).sort((x, y) => x - y); return a.length ? a[Math.min(a.length - 1, Math.floor(a.length * 0.75))] : null; };
  const fmtDur = s => { s = Math.round(s); return s < 60 ? s + ' s' : Math.floor(s / 60) + ' min ' + (s % 60) + ' s'; };
  const sessionsOf = rows => { const m = new Map(); rows.forEach(r => { const s = m.get(r.sid) || { sid: r.sid, vid: r.vid, rows: [], t: r.t }; s.rows.push(r); if (r.t < s.t) s.t = r.t; m.set(r.sid, s); }); return [...m.values()]; };

  function kpis(rows) {
    const ss = sessionsOf(rows);
    const bounce = ss.filter(s => s.rows.length === 1 && s.rows[0].dur < 10 && !s.rows[0].ev.length).length;
    const withNew = rows.filter(r => r.isNew != null);
    return {
      pv: rows.length, vis: uniq(rows, r => r.vid), ses: ss.length,
      dur: (() => { const a = rows.map(r => Math.min(r.dur, 1800)).sort((x, y) => x - y); return a.length ? a[Math.floor(a.length / 2)] : 0; })(),
      bounce: pct(bounce, ss.length), scroll: rows.length ? Math.round(rows.reduce((a, r) => a + r.scroll, 0) / rows.length) : 0,
      leads: rows.filter(r => r.conv).length, conv: pct(ss.filter(s => s.rows.some(r => r.conv)).length, ss.length),
      newPct: withNew.length ? pct(uniq(withNew.filter(r => r.isNew), r => r.vid), uniq(withNew, r => r.vid)) : null
    };
  }

  /* ---- chart primitives (inline SVG, recessive axes, hover tooltips) ---- */
  function tip(host) { let t = host.querySelector('.wa-tip'); if (!t) { t = el('<div class="wa-tip" role="status" hidden></div>'); host.appendChild(t); } return t; }
  function lineChart(host, labels, series) {
    const W = 900, Hh = 240, P = { l: 44, r: 12, t: 12, b: 28 };
    const max = Math.max(1, ...series.flatMap(s => s.values));
    const nice = Math.ceil(max / Math.pow(10, Math.floor(Math.log10(max)))) * Math.pow(10, Math.floor(Math.log10(max)));
    const x = i => P.l + (labels.length < 2 ? (W - P.l - P.r) / 2 : i * (W - P.l - P.r) / (labels.length - 1));
    const y = v => P.t + (Hh - P.t - P.b) * (1 - v / nice);
    const ticks = [0, nice / 2, nice];
    const step = Math.max(1, Math.ceil(labels.length / 8));
    const svg = `<svg viewBox="0 0 ${W} ${Hh}" class="wa-svg" role="img" aria-label="Návštěvnost v čase">
      ${ticks.map(v => `<line x1="${P.l}" x2="${W - P.r}" y1="${y(v)}" y2="${y(v)}" class="wa-grid"/><text x="${P.l - 8}" y="${y(v) + 4}" text-anchor="end" class="wa-axis">${nf.format(Math.round(v))}</text>`).join('')}
      ${labels.map((l, i) => i % step === 0 ? `<text x="${x(i)}" y="${Hh - 8}" text-anchor="middle" class="wa-axis">${esc(l)}</text>` : '').join('')}
      ${series.map(s => `<path d="${s.values.map((v, i) => (i ? 'L' : 'M') + x(i).toFixed(1) + ' ' + y(v).toFixed(1)).join(' ')} L${x(s.values.length - 1)} ${y(0)} L${x(0)} ${y(0)} Z" fill="${s.color}" opacity="0.08"/>
        <path d="${s.values.map((v, i) => (i ? 'L' : 'M') + x(i).toFixed(1) + ' ' + y(v).toFixed(1)).join(' ')}" fill="none" stroke="${s.color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>`).join('')}
      <line class="wa-cross" y1="${P.t}" y2="${Hh - P.b}" x1="-10" x2="-10"/>
      ${series.map((s, k) => `<circle class="wa-dot" data-k="${k}" r="4.5" cx="-10" cy="-10" fill="${s.color}" stroke="#fff" stroke-width="2"/>`).join('')}
      <rect x="${P.l}" y="0" width="${W - P.l - P.r}" height="${Hh}" fill="transparent" class="wa-hit"/></svg>`;
    host.innerHTML = svg + `<div class="wa-legend">${series.map(s => `<span><i style="background:${s.color}"></i>${esc(s.name)}</span>`).join('')}</div>`;
    const sv = host.querySelector('svg'), cross = sv.querySelector('.wa-cross'), dots = sv.querySelectorAll('.wa-dot'), tt = tip(host); tt.hidden = true;
    const move = e => {
      const r = sv.getBoundingClientRect(), px = (e.clientX - r.left) / r.width * W;
      let i = Math.round((px - P.l) / ((W - P.l - P.r) / Math.max(1, labels.length - 1))); i = Math.max(0, Math.min(labels.length - 1, i));
      cross.setAttribute('x1', x(i)); cross.setAttribute('x2', x(i));
      dots.forEach(d => { const s = series[d.dataset.k]; d.setAttribute('cx', x(i)); d.setAttribute('cy', y(s.values[i])); });
      tt.innerHTML = `<b>${esc(labels[i])}</b>` + series.map(s => `<span><i style="background:${s.color}"></i>${esc(s.name)}: <b>${nf.format(s.values[i])}</b></span>`).join('');
      tt.style.left = Math.min(r.width - 170, Math.max(0, x(i) / W * r.width + 12)) + 'px'; tt.style.top = '8px'; tt.hidden = false;
    };
    sv.querySelector('.wa-hit').addEventListener('pointermove', move);
    sv.addEventListener('pointerleave', () => { tt.hidden = true; cross.setAttribute('x1', -10); cross.setAttribute('x2', -10); dots.forEach(d => d.setAttribute('cx', -10)); });
  }
  function barList(host, rows, { total, fmt = v => nf.format(v), limit = 8, empty = 'Zatím bez dat' } = {}) {
    if (!rows.length) { host.innerHTML = `<p class="wa-none">${empty}</p>`; return; }
    const shown = rows.slice(0, limit), rest = rows.slice(limit).reduce((a, r) => a + r[1], 0);
    if (rest) shown.push(['Ostatní', rest]);
    const max = Math.max(...shown.map(r => r[1])); const tot = total || rows.reduce((a, r) => a + r[1], 0);
    host.innerHTML = `<ul class="wa-bars">${shown.map(([k, v]) => `<li title="${esc(k)}: ${fmt(v)} (${pct(v, tot)} %)"><span class="wa-bl">${esc(k)}</span><span class="wa-bt"><i style="width:${Math.max(2, v / max * 100)}%"></i></span><span class="wa-bv">${fmt(v)}<small>${pct(v, tot)} %</small></span></li>`).join('')}</ul>`;
  }
  function heat(host, rows) {
    const M = Array.from({ length: 7 }, () => new Array(24).fill(0));
    rows.forEach(r => { const d = (r.t.getDay() + 6) % 7; M[d][r.t.getHours()]++; });
    const max = Math.max(1, ...M.flat()); const days = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne'];
    host.innerHTML = `<div class="wa-heat" role="img" aria-label="Návštěvy podle dne a hodiny">
      <span></span>${Array.from({ length: 24 }, (_, h) => `<span class="wa-hh">${h % 3 === 0 ? h : ''}</span>`).join('')}
      ${M.map((row, d) => `<span class="wa-hd">${days[d]}</span>` + row.map((v, h) => `<i style="background:${v ? SEQ[Math.min(7, 1 + Math.floor(v / max * 6.99))] : SEQ[0]}" title="${days[d]} ${h}:00–${h}:59 · ${v} zobrazení"></i>`).join('')).join('')}
    </div><div class="wa-scale"><span>méně</span>${SEQ.slice(1).map(c => `<i style="background:${c}"></i>`).join('')}<span>více</span></div>`;
  }

  async function analytics() {
    const s = shell('Analytika návštěvnosti', 'Načítám data…', true);
    s.act.innerHTML = `<button class="wa-btn" data-a="refresh">Obnovit</button><button class="wa-btn" data-a="csv">Export CSV</button><button class="wa-btn" data-a="me"></button>`;
    const meBtn = s.act.querySelector('[data-a="me"]');
    const meSet = () => { let v = null; try { v = localStorage.getItem('wh_notrack'); } catch (e) {} meBtn.textContent = v ? 'Tento prohlížeč se neměří ✓' : 'Neměřit tento prohlížeč'; meBtn.classList.toggle('on', !!v); };
    meBtn.addEventListener('click', () => { try { localStorage.getItem('wh_notrack') ? localStorage.removeItem('wh_notrack') : localStorage.setItem('wh_notrack', '1'); } catch (e) {} meSet(); }); meSet();
    const state = { range: '30', page: 'all', src: 'all', dev: 'all', legacy: true };
    let ALL = [];
    s.body.innerHTML = `
      <div class="wa-filters">
        <div class="wa-seg" data-f="range">${[['1', 'Dnes'], ['7', '7 dní'], ['30', '30 dní'], ['90', '90 dní'], ['all', 'Vše']].map(([k, v]) => `<button data-v="${k}" class="${k === state.range ? 'on' : ''}">${v}</button>`).join('')}</div>
        <label><span>Stránka</span><select data-f="page"></select></label>
        <label><span>Zdroj</span><select data-f="src"></select></label>
        <label><span>Zařízení</span><select data-f="dev"><option value="all">Všechna</option><option value="desktop">Počítač</option><option value="mobile">Mobil</option><option value="tablet">Tablet</option></select></label>
        <label class="wa-check"><input type="checkbox" data-f="legacy" checked> Včetně starého webu</label>
        <span class="wa-live"><i></i><b data-live>0</b> právě na webu</span>
      </div>
      <div class="wa-kpis"></div>
      <section class="wa-card wa-span2"><h3>Návštěvnost v čase</h3><div data-c="line"></div></section>
      <div class="wa-grid3">
        <section class="wa-card"><h3>Zdroje návštěvnosti</h3><div data-c="src"></div></section>
        <section class="wa-card"><h3>Odkazující weby</h3><div data-c="ref"></div></section>
        <section class="wa-card"><h3>Kampaně (UTM)</h3><div data-c="utm"></div></section>
        <section class="wa-card"><h3>Stránky</h3><div data-c="pages"></div></section>
        <section class="wa-card"><h3>Vstupní stránky</h3><div data-c="entry"></div></section>
        <section class="wa-card"><h3>Zařízení</h3><div data-c="dev"></div></section>
        <section class="wa-card"><h3>Prohlížeče</h3><div data-c="br"></div></section>
        <section class="wa-card"><h3>Operační systémy</h3><div data-c="os"></div></section>
        <section class="wa-card"><h3>Jazyk a časové pásmo</h3><div data-c="lang"></div></section>
      </div>
      <div class="wa-grid2">
        <section class="wa-card"><h3>Cesta k poptávce</h3><p class="wa-note">Relace, které došly do daného kroku</p><div data-c="funnel"></div></section>
        <section class="wa-card"><h3>Dosah sekcí na úvodní stránce</h3><p class="wa-note">Podíl zobrazení úvodu, ve kterých návštěvník sekci viděl</p><div data-c="secs"></div></section>
        <section class="wa-card"><h3>Kdy lidé chodí</h3><div data-c="heat"></div></section>
        <section class="wa-card"><h3>Hloubka scrollu</h3><div data-c="scroll"></div></section>
        <section class="wa-card"><h3>Interakce</h3><div data-c="ev"></div></section>
        <section class="wa-card"><h3>Nejklikanější prvky</h3><div data-c="evtop"></div></section>
        <section class="wa-card"><h3>Prokliky na weby klientů</h3><div data-c="out"></div></section>
        <section class="wa-card"><h3>Rychlost webu (Core Web Vitals, 75. percentil)</h3><div data-c="vit"></div></section>
      </div>
      <section class="wa-card"><h3>Posledních 30 návštěv</h3><p class="wa-note">Kompletní data stáhnete přes Export CSV</p><div data-c="table"></div></section>`;
    const $ = sel => s.body.querySelector(sel);
    const fill = (sel, opts, cur) => { $(sel).innerHTML = opts.map(([k, v]) => `<option value="${esc(k)}" ${k === cur ? 'selected' : ''}>${esc(v)}</option>`).join(''); };

    async function fetchAll() {
      s.sub.textContent = 'Načítám data…';
      try {
        const raw = await db.all('LandingPageMetric');
        ALL = raw.map(normalize).filter(r => !/localhost|127\.0\.0\.1|test\.local/.test(r.host));
        render();
      } catch (e) { s.sub.textContent = 'Data se nepodařilo načíst.'; }
    }
    function filtered(prev) {
      const now = new Date(); let from = null, to = now;
      if (state.range === '1') { from = new Date(now); from.setHours(0, 0, 0, 0); }
      else if (state.range !== 'all') from = new Date(now - state.range * 864e5);
      if (prev) { if (!from) return []; const len = to - from; to = from; from = new Date(from - len); }
      return ALL.filter(r => (!from || r.t >= from) && r.t < to && (state.legacy || !r.legacy) && (state.page === 'all' || r.page === state.page) && (state.src === 'all' || r.src === state.src) && (state.dev === 'all' || r.dev === state.dev));
    }
    function render() {
      const scope = ALL.filter(r => state.legacy || !r.legacy);
      fill('[data-f="page"]', [['all', 'Všechny']].concat(countBy(scope, r => r.page).map(([k]) => [k, k])), state.page);
      fill('[data-f="src"]', [['all', 'Všechny']].concat(countBy(scope, r => r.src).map(([k]) => [k, k])), state.src);
      const rows = filtered(false), prevRows = filtered(true);
      const k = kpis(rows), kp = kpis(prevRows);
      const newest = ALL.length ? ALL.reduce((a, r) => r.t > a ? r.t : a, ALL[0].t) : null;
      s.sub.textContent = `${nf.format(ALL.length)} zaznamenaných zobrazení celkem · poslední ${newest ? newest.toLocaleString('cs-CZ') : '—'}`;
      const live = ALL.filter(r => Date.now() - r.upd < 5 * 60e3); $('[data-live]').textContent = uniq(live, r => r.sid);
      const delta = (a, b, inv) => { if (state.range === 'all' || !prevRows.length) return ''; const d = b ? Math.round((a - b) / b * 100) : (a ? 100 : 0); if (!d) return '<small class="wa-d">beze změny</small>'; const good = inv ? d < 0 : d > 0; return `<small class="wa-d ${good ? 'up' : 'down'}">${d > 0 ? '▲' : '▼'} ${Math.abs(d)} %</small>`; };
      const tiles = [['Zobrazení stránek', nf.format(k.pv), delta(k.pv, kp.pv)], ['Návštěvníci', nf.format(k.vis), delta(k.vis, kp.vis)], ['Relace', nf.format(k.ses), delta(k.ses, kp.ses)],
        ['Medián aktivního času', fmtDur(k.dur), delta(k.dur, kp.dur)], ['Okamžitý odchod', k.bounce + ' %', delta(k.bounce, kp.bounce, true)], ['Prům. scroll', k.scroll + ' %', delta(k.scroll, kp.scroll)],
        ['Poptávky', nf.format(k.leads), delta(k.leads, kp.leads)], ['Konverzní poměr', k.conv + ' %', delta(k.conv, kp.conv)], ['Noví návštěvníci', k.newPct == null ? '—' : k.newPct + ' %', '']];
      $('.wa-kpis').innerHTML = tiles.map(([l, v, d]) => `<div class="wa-kpi"><span>${l}</span><b>${v}</b>${d}</div>`).join('');

      // time series
      const byHour = state.range === '1';
      const buckets = new Map(); const labels = [];
      if (byHour) { for (let h = 0; h < 24; h++) { buckets.set(h, []); labels.push(h + ':00'); } rows.forEach(r => buckets.get(r.t.getHours()).push(r)); }
      else {
        const days = state.range === 'all' ? Math.max(1, Math.ceil((Date.now() - (rows.length ? Math.min(...rows.map(r => +r.t)) : Date.now())) / 864e5) + 1) : +state.range;
        for (let i = days - 1; i >= 0; i--) { const d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - i); const key = d.toDateString(); buckets.set(key, []); labels.push(d.toLocaleDateString('cs-CZ', { day: 'numeric', month: 'numeric' })); }
        rows.forEach(r => { const d = new Date(r.t); d.setHours(0, 0, 0, 0); const b = buckets.get(d.toDateString()); if (b) b.push(r); });
      }
      const bs = [...buckets.values()];
      lineChart($('[data-c="line"]'), labels, [{ name: 'Zobrazení stránek', color: C1, values: bs.map(b => b.length) }, { name: 'Návštěvníci', color: C2, values: bs.map(b => uniq(b, r => r.vid)) }]);

      const ss = sessionsOf(rows); const T = rows.length;
      barList($('[data-c="src"]'), countBy(rows, r => r.src === 'direct' ? 'Přímý přístup' : r.src === 'internal' ? 'Z webu (interní)' : r.src), { total: T });
      barList($('[data-c="ref"]'), countBy(rows.filter(r => r.ref && r.src !== 'internal'), r => r.ref), { empty: 'Žádné odkazující weby' });
      barList($('[data-c="utm"]'), countBy(rows.filter(r => r.utm && (r.utm.campaign || r.utm.source)), r => [r.utm.source, r.utm.medium, r.utm.campaign].filter(Boolean).join(' / ')), { empty: 'Žádné kampaně s UTM parametry' });
      barList($('[data-c="pages"]'), countBy(rows, r => r.page), { total: T });
      barList($('[data-c="entry"]'), countBy(ss, x => x.rows.sort((a, b) => a.t - b.t)[0].page), { total: ss.length });
      barList($('[data-c="dev"]'), countBy(rows, r => ({ desktop: 'Počítač', mobile: 'Mobil', tablet: 'Tablet' }[r.dev] || r.dev)), { total: T });
      barList($('[data-c="br"]'), countBy(rows.filter(r => !r.legacy), r => r.br));
      barList($('[data-c="os"]'), countBy(rows.filter(r => !r.legacy), r => r.os));
      barList($('[data-c="lang"]'), countBy(rows.filter(r => !r.legacy), r => (r.lang || '—') + ' · ' + (r.tz || '—')), { limit: 6 });

      // funnel
      const steps = [['Návštěva', () => true], ['Scroll aspoň 50 %', x => x.rows.some(r => r.scroll >= 50)], ['Viděl kontaktní sekci', x => x.rows.some(r => r.secs.includes('kontakt') || r.secs.includes('contact'))],
        ['Začal vyplňovat', x => x.rows.some(r => r.ev.some(e => e[1] === 'form_start' || e[1] === 'hero_form'))], ['Odeslal poptávku', x => x.rows.some(r => r.conv)]];
      const fr = steps.map(([l, f]) => [l, ss.filter(f).length]);
      $('[data-c="funnel"]').innerHTML = `<ol class="wa-funnel">${fr.map(([l, v], i) => `<li><span>${i + 1}. ${l}</span><span class="wa-bt"><i style="width:${ss.length ? Math.max(1.5, v / ss.length * 100) : 0}%"></i></span><b>${nf.format(v)}<small>${pct(v, ss.length)} %</small></b></li>`).join('')}</ol>`;

      // sections reach (new homepage only)
      const home = rows.filter(r => r.page === 'Úvod' && !r.legacy);
      const order = ['top', 'realizace', 'proces', 'sluzby', 'geo', 'tym', 'faq', 'kontakt', 'paticka'];
      barList($('[data-c="secs"]'), home.length ? order.map(k => [SEC_LABEL[k], home.filter(r => r.secs.includes(k)).length]) : [], { total: home.length, limit: 12, fmt: v => pct(v, home.length) + ' %', empty: 'Zatím bez dat z nového webu — začnou se sbírat po spuštění.' });
      $('[data-c="secs"]').querySelectorAll('.wa-bv small').forEach(x => x.remove());

      heat($('[data-c="heat"]'), rows);
      const sb = [['0–25 %', 0], ['25–50 %', 0], ['50–75 %', 0], ['75–100 %', 0]]; rows.forEach(r => sb[Math.min(3, Math.floor(r.scroll / 25.0001))][1]++);
      barList($('[data-c="scroll"]'), sb.map(x => x), { total: T, limit: 4 });

      const evs = rows.flatMap(r => r.ev);
      barList($('[data-c="ev"]'), countBy(evs, e => EV_LABEL[e[1]] || e[1]), { empty: 'Zatím žádné interakce' });
      barList($('[data-c="evtop"]'), countBy(evs.filter(e => ['cta', 'nav', 'faq', 'showcase', 'ba', 'filter'].includes(e[1])), e => e[2] || e[1]), { empty: 'Zatím žádné kliky', limit: 10 });
      barList($('[data-c="out"]'), countBy(evs.filter(e => e[1] === 'out'), e => e[2]), { empty: 'Zatím žádné prokliky', limit: 10 });

      const vit = [['LCP (načtení hlavního obsahu)', q75(rows.map(r => r.vit.lcp)), v => (v / 1000).toFixed(2) + ' s', 2500, 4000],
        ['INP (odezva na kliknutí)', q75(rows.map(r => r.vit.inp)), v => Math.round(v) + ' ms', 200, 500],
        ['CLS (posouvání obsahu)', q75(rows.map(r => r.vit.cls)), v => v.toFixed(3), 0.1, 0.25]];
      $('[data-c="vit"]').innerHTML = `<ul class="wa-vit">${vit.map(([l, v, f, g, p]) => { const st = v == null ? ['none', '—', 'bez dat'] : v <= g ? ['good', '●', 'Dobré'] : v <= p ? ['warn', '▲', 'Zlepšit'] : ['bad', '■', 'Špatné']; return `<li><span>${l}</span><b>${v == null ? '—' : f(v)}</b><em class="st-${st[0]}">${st[1]} ${st[2]}</em></li>`; }).join('')}</ul>`;

      // recent table
      const recent = rows.slice().sort((a, b) => b.t - a.t).slice(0, 30);
      $('[data-c="table"]').innerHTML = recent.length ? `<div class="wa-tw"><table class="wa-table"><thead><tr><th>Čas</th><th>Stránka</th><th>Zdroj</th><th>Zařízení</th><th>Prohlížeč</th><th>Aktivní čas</th><th>Scroll</th><th>Sekce</th><th>Interakce</th><th>Poptávka</th></tr></thead><tbody>
        ${recent.map(r => `<tr><td>${r.t.toLocaleString('cs-CZ', { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' })}</td><td>${esc(r.page)}</td><td>${esc(r.src)}${r.ref && r.src !== r.ref ? ` <small>${esc(r.ref)}</small>` : ''}</td><td>${esc(r.dev)}</td><td>${esc(r.br)}${r.os !== '—' ? ` <small>${esc(r.os)}</small>` : ''}</td><td>${fmtDur(r.dur)}</td><td>${r.scroll} %</td><td>${r.secs.length}</td>
          <td>${r.ev.length ? `<details><summary>${r.ev.length}</summary><ol>${r.ev.map(e => `<li><b>${e[0]} s</b> ${esc(EV_LABEL[e[1]] || e[1])}${e[2] ? ' · ' + esc(e[2]) : ''}</li>`).join('')}</ol></details>` : '0'}</td><td>${r.conv ? '<em class="st-good">● Ano</em>' : '—'}</td></tr>`).join('')}
      </tbody></table></div>` : '<p class="wa-none">Pro zvolené filtry nejsou žádné návštěvy.</p>';
      s.root._rows = rows;
    }
    s.body.addEventListener('click', e => { const b = e.target.closest('.wa-seg button'); if (!b) return; state.range = b.dataset.v; s.body.querySelectorAll('.wa-seg button').forEach(x => x.classList.toggle('on', x === b)); render(); });
    s.body.addEventListener('change', e => { const f = e.target.dataset.f; if (!f) return; state[f] = e.target.type === 'checkbox' ? e.target.checked : e.target.value; render(); });
    s.act.addEventListener('click', e => {
      const a = e.target.closest('[data-a]'); if (!a) return;
      if (a.dataset.a === 'refresh') fetchAll();
      if (a.dataset.a === 'csv') {
        const rows = s.root._rows || []; const head = ['cas', 'stranka', 'url', 'zdroj', 'odkazujici_web', 'utm_source', 'utm_medium', 'utm_campaign', 'zarizeni', 'prohlizec', 'os', 'jazyk', 'casove_pasmo', 'rozliseni', 'aktivni_cas_s', 'scroll_pct', 'sekce', 'udalosti', 'poptavka', 'navstevnik', 'relace', 'lcp_ms', 'inp_ms', 'cls'];
        const q = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
        const csv = [head.join(';')].concat(rows.map(r => [r.t.toISOString(), r.page, r.url, r.src, r.ref, r.utm.source, r.utm.medium, r.utm.campaign, r.dev, r.br, r.os, r.lang, r.tz, r.scr, r.dur, r.scroll, r.secs.join(' '), r.ev.map(e => e[1] + ':' + e[2]).join(' | '), r.conv ? 'ano' : 'ne', r.vid, r.sid, r.vit.lcp, r.vit.inp, r.vit.cls].map(q).join(';'))).join('\n');
        const blob = new Blob(['﻿' + csv], { type: 'text/csv;charset=utf-8' }); const u = URL.createObjectURL(blob);
        const l = document.createElement('a'); l.href = u; l.download = 'webhunter-analytika-' + new Date().toISOString().slice(0, 10) + '.csv'; document.body.appendChild(l); l.click(); l.remove(); setTimeout(() => URL.revokeObjectURL(u), 2000);
      }
    });
    await fetchAll();
    window.__waTimer = setInterval(() => { if (current === s.root) fetchAll(); }, 60000);
  }

  window.WHAdmin = { open(kind) { if (kind === 'navrhy') proposals(); else if (kind === 'analytics') analytics(); else if (kind === 'leads') leads(); }, close };
})();
