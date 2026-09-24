/* WebHunter — shared site script */
const WH_ASSETS = (document.currentScript && document.currentScript.src.replace(/site(\.min)?\.js.*$/, '')) || 'assets/';
const WH_VER = ((document.currentScript && document.currentScript.src.match(/[?&]v=(\d+)/)) || [])[1] || '1';
const WH_APP = '6a366c8ba95efe01593d4844';
const WH_API = 'https://base44.app/api/apps/' + WH_APP;
const WH_PIXEL = '1023099023693684';
window.whTrack = window.whTrack || function () { (window.whTrackQ = window.whTrackQ || []).push([].slice.call(arguments)); };

/* ---------- Consent (GDPR) ---------- */
const whConsent = (() => {
  const KEY = 'wh_cookie_consent';
  const read = () => {
    let raw = null; try { raw = localStorage.getItem(KEY); } catch (e) {}
    if (!raw) return null;
    if (raw === 'all') return { a: true, m: true, legacy: true };
    if (raw === 'necessary') return { a: false, m: false, legacy: true };
    try { const o = JSON.parse(raw); return o && o.v ? o : null; } catch (e) { return null; }
  };
  const loaded = {};
  const loadScript = (src, attrs = {}) => new Promise((res, rej) => { const el = document.createElement('script'); el.src = src; el.async = true; Object.assign(el, attrs); el.onload = res; el.onerror = rej; document.head.appendChild(el); });
  const apply = c => {
    if (!c) return;
    if (c.a && !loaded.a) { loaded.a = true; loadScript(WH_ASSETS + 'track.min.js?v=' + WH_VER).catch(() => {}); }
    if (c.m && !loaded.m) {
      loaded.m = true;
      /* Meta Pixel — loaded only after marketing consent */
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', WH_PIXEL); window.fbq('consent', 'grant'); window.fbq('track', 'PageView');
    }
    if (!c.m && window.fbq) { try { window.fbq('consent', 'revoke'); } catch (e) {} }
  };
  const save = (a, m) => {
    const c = { v: 1, a: !!a, m: !!m, t: new Date().toISOString() };
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    if (!a) { try { ['wh_vid', 'wh_first', 'wh_visits'].forEach(k => localStorage.removeItem(k)); sessionStorage.removeItem('wh_landing_session'); } catch (e) {} }
    apply(c); return c;
  };
  let ui = null;
  const build = () => {
    const privacy = (document.querySelector('a[href$="ochrana-osobnich-udaju/"]') || {}).getAttribute ? document.querySelector('a[href$="ochrana-osobnich-udaju/"]').getAttribute('href') : 'ochrana-osobnich-udaju/';
    const d = document.createElement('div'); d.className = 'ck'; d.hidden = true;
    d.innerHTML = `<div class="ck-card" role="dialog" aria-modal="false" aria-labelledby="ck-t">
      <div class="ck-head"><svg class="cp-mark" viewBox="0 0 48 56" aria-hidden="true"><path d="M24 3 L43 10 V28 C43 40 34 50 24 54 C14 50 5 40 5 28 V10 Z" fill="#16345F"/><path d="M15 28 l6.5 6.5 L34 21" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div><h2 id="ck-t">Vážíme si vašeho soukromí</h2><p>Nezbytné cookies zajišťují fungování webu. Analytické nám pomáhají web zlepšovat a marketingové měří účinnost reklam. Volitelné použijeme jen s vaším souhlasem, který můžete kdykoli změnit v patičce. Více v <a href="${privacy}">zásadách ochrany osobních údajů</a>.</p></div></div>
      <div class="ck-opts" hidden>
        <label class="ck-opt"><b>Nezbytné</b><small>Uložení vaší volby a základní funkce webu. Vždy zapnuté.</small><span class="ck-sw"><input type="checkbox" checked disabled><i></i></span></label>
        <label class="ck-opt"><b>Analytické</b><small>Anonymní statistiky návštěvnosti, abychom věděli, co na webu funguje.</small><span class="ck-sw"><input type="checkbox" data-ck="a"><i></i></span></label>
        <label class="ck-opt"><b>Marketingové</b><small>Meta Pixel pro měření a cílení reklam na Facebooku a Instagramu.</small><span class="ck-sw"><input type="checkbox" data-ck="m"><i></i></span></label>
      </div>
      <div class="ck-btns"><button type="button" class="ck-s" data-ck-set>Nastavení</button><button type="button" class="ck-r" data-ck-no>Odmítnout vše</button><button type="button" class="ck-a" data-ck-yes>Přijmout vše</button></div>
    </div>`;
    document.body.appendChild(d);
    const opts = d.querySelector('.ck-opts'), setBtn = d.querySelector('[data-ck-set]');
    const close = () => { d.hidden = true; document.body.classList.remove('ck-open'); };
    d.querySelector('[data-ck-yes]').addEventListener('click', () => { save(true, true); close(); });
    d.querySelector('[data-ck-no]').addEventListener('click', () => { save(false, false); close(); });
    setBtn.addEventListener('click', () => {
      if (opts.hidden) { opts.hidden = false; setBtn.textContent = 'Uložit výběr'; return; }
      save(d.querySelector('[data-ck="a"]').checked, d.querySelector('[data-ck="m"]').checked); close();
    });
    return { el: d, opts, setBtn };
  };
  const open = (detailed) => {
    ui = ui || build();
    const c = read() || { a: false, m: false };
    ui.el.querySelector('[data-ck="a"]').checked = !!c.a; ui.el.querySelector('[data-ck="m"]').checked = !!c.m;
    ui.opts.hidden = !detailed; ui.setBtn.textContent = detailed ? 'Uložit výběr' : 'Nastavení';
    ui.el.hidden = false; document.body.classList.add('ck-open');
  };
  const init = () => {
    const c = read();
    if (c) apply(c); else setTimeout(() => open(false), 900);
    document.querySelectorAll('[data-cookie-settings]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); open(true); }));
  };
  return { read, save, open, init };
})();
window.whConsent = whConsent;

document.addEventListener('DOMContentLoaded', () => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const hasGsap = typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined';
  const nav = $('.nav');
  const finePointer = window.matchMedia('(pointer: fine)').matches;

  // Lenis
  let lenis = null;
  if (typeof Lenis !== 'undefined') {
    lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
    if (hasGsap) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(time => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      const raf = t => { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
  }
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const el = $(id);
      if (!el) return;
      e.preventDefault();
      closeMenu();
      if (lenis) lenis.scrollTo(el, { offset: id === '#top' ? 0 : -10, duration: 1.4 });
      else el.scrollIntoView({ behavior: 'smooth' });
    });
  });

  // Mobile menu
  const toggle = $('.nav-toggle');
  const links = $('.nav-links');
  function closeMenu() { links.classList.remove('open'); toggle.classList.remove('open'); nav.classList.remove('menu-open'); document.body.classList.remove('menu-lock'); }
  toggle.addEventListener('click', () => {
    const open = !links.classList.contains('open');
    links.classList.toggle('open', open); toggle.classList.toggle('open', open); nav.classList.toggle('menu-open', open);
  });
  $$('.nav-links a').forEach(a => a.addEventListener('click', closeMenu));

  // Nav state
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 60);
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Rail active section
  const railLinks = $$('.rail a[data-sec]');
  if (railLinks.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) {
          const id = en.target.dataset.section;
          railLinks.forEach(l => l.classList.toggle('active', l.dataset.sec === id && !l.classList.contains('rail-cta')));
        }
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    $$('[data-section]').forEach(s => io.observe(s));
  }

  // Pause CSS animation loops in sections that are off screen
  const offIO = new IntersectionObserver(entries => entries.forEach(en => en.target.classList.toggle('is-off', !en.isIntersecting)), { rootMargin: '100px 0px' });
  $$('.hero, .marquee, .strip, .reel, .bento, .services, .team, .faq, .cta, .cta-band, .geo, .showcase, .sub-hero, .process').forEach(el => offIO.observe(el));
  const heroEl = $('.hero');

  // In-view triggers for CSS animations
  const vio = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in-view'); vio.unobserve(en.target); } });
  }, { threshold: 0.35 });
  $$('.observe, .cmp').forEach(el => vio.observe(el));

  // Hero timer
  const timer = $('[data-timer]');
  if (timer) {
    let secs = 48 * 3600 - 1;
    setInterval(() => {
      secs = secs > 0 ? secs - 1 : 48 * 3600 - 1;
      if (heroEl && heroEl.classList.contains('is-off')) return;
      const h = String(Math.floor(secs / 3600)).padStart(2, '0');
      const m = String(Math.floor(secs % 3600 / 60)).padStart(2, '0');
      const s = String(secs % 60).padStart(2, '0');
      timer.firstChild.nodeValue = `${h}:${m}:${s}`;
    }, 1000);
  }

  // Manifest fill words
  const fill = $('.fill-text');
  if (fill) [...fill.childNodes].forEach(n => {
    if (n.nodeType === 3 && n.textContent.trim()) {
      const frag = document.createDocumentFragment();
      n.textContent.split(/(\s+)/).forEach(part => {
        if (!part.trim()) { frag.appendChild(document.createTextNode(part)); return; }
        const sp = document.createElement('span'); sp.className = 'fw'; sp.textContent = part; frag.appendChild(sp);
      });
      n.replaceWith(frag);
    }
  });

  // Compare slider
  $$('[data-compare]').forEach(c => {
    const set = x => {
      const r = c.getBoundingClientRect();
      const p = Math.min(96, Math.max(4, (x - r.left) / r.width * 100));
      c.style.setProperty('--pos', p + '%');
    };
    c.addEventListener('pointermove', e => { if (e.pointerType === 'mouse' || e.buttons) { c._touched = performance.now(); set(e.clientX); } });
    c.addEventListener('pointerdown', e => { c._touched = performance.now(); set(e.clientX); });
  });

  // Real before/after cases
  const ba = $('[data-ba]');
  if (ba) {
    const bImg = $('[data-ba-before]', ba), aImg = $('[data-ba-after]', ba), lTag = $('[data-ba-l]', ba);
    const tabs = $$('[data-ba-case]');
    tabs.forEach(t => t.addEventListener('click', () => {
      if (t.classList.contains('on')) return;
      tabs.forEach(x => x.classList.toggle('on', x === t));
      const k = t.dataset.baCase, pre = [new Image(), new Image()];
      pre[0].src = `img/ba/${k}-before.webp`; pre[1].src = `img/ba/${k}-after.webp`;
      ba.classList.add('swap');
      Promise.all(pre.map(im => im.decode().catch(() => {}))).then(() => setTimeout(() => {
        bImg.src = pre[0].src; aImg.src = pre[1].src;
        bImg.alt = `Původní web ${t.dataset.name} z roku ${t.dataset.year}`; aImg.alt = `Nový web ${t.dataset.name} od WebHunter`;
        lTag.textContent = `Předtím · ${t.dataset.year}`;
        ba.classList.remove('swap');
        if (hasGsap) { const o = { p: 88 }; gsap.to(o, { p: 50, duration: 1.2, ease: 'expo.inOut', onUpdate: () => { if (performance.now() - (ba._touched || 0) > 1200) ba.style.setProperty('--pos', o.p + '%'); } }); }
      }, 200));
    }));
  }

  // Team comparison: sequential checks
  $$('.cmp .mk.yes').forEach((m, i) => { m.style.transitionDelay = (0.2 + i * 0.12) + 's'; });

  // FAQ accordion
  const qas = $$('.qa');
  qas.forEach(qa => $('.q', qa).addEventListener('click', () => {
    const open = !qa.classList.contains('open');
    qas.forEach(o => { o.classList.remove('open'); $('.q', o).setAttribute('aria-expanded', 'false'); });
    if (open) { qa.classList.add('open'); $('.q', qa).setAttribute('aria-expanded', 'true'); }
    if (hasGsap) setTimeout(() => ScrollTrigger.refresh(), 650);
  }));

  // Magnetic buttons
  if (finePointer) $$('.btn-magnetic').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect();
      btn.style.transition = 'transform .15s linear';
      btn.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * 0.18}px, ${(e.clientY - r.top - r.height / 2) * 0.25}px)`;
    });
    btn.addEventListener('mouseleave', () => { btn.style.transition = 'transform .6s cubic-bezier(.16,1,.3,1)'; btn.style.transform = ''; });
  });

  // Hero URL form -> prefill contact form
  const heroForm = $('[data-hero-url]');
  const goContact = (focusSel) => {
    const target = $('#kontakt');
    if (!target) return;
    if (lenis) lenis.scrollTo(target, { offset: -10, duration: 1.4 }); else target.scrollIntoView({ behavior: 'smooth' });
    const f = $(focusSel);
    setTimeout(() => { if (!f) return; f.focus({ preventScroll: true }); const fld = f.closest('.fld'); if (fld) { fld.classList.remove('flash'); void fld.offsetWidth; fld.classList.add('flash'); } }, 1450);
  };
  if (heroForm) {
    heroForm.addEventListener('submit', e => {
      e.preventDefault();
      const v = $('#hero-web').value.trim();
      if (!v) { heroForm.classList.remove('shake'); void heroForm.offsetWidth; heroForm.classList.add('shake'); $('#hero-web').focus(); return; }
      const web = $('.form [name="web"]');
      if (web) web.value = v.replace(/^https?:\/\//i, '').replace(/\/$/, '');
      goContact('.form [name="email"]');
    });
    const noWeb = $('[data-no-web]');
    if (noWeb) noWeb.addEventListener('click', e => { e.preventDefault(); e.stopImmediatePropagation(); goContact('.form [name="popis"]'); }, true);
  }

  // Mobile sticky CTA: hidden over hero and contact form
  const mCta = $('[data-m-cta]');
  if (mCta) {
    const hide = new Set();
    const sync = () => mCta.classList.toggle('show', hide.size === 0 && window.scrollY > 200);
    const mio = new IntersectionObserver(en => { en.forEach(x => x.isIntersecting ? hide.add(x.target) : hide.delete(x.target)); sync(); }, { threshold: 0.15 });
    $$('.hero, .sub-hero, #kontakt, .cta-band').forEach(el => mio.observe(el));
    window.addEventListener('scroll', sync, { passive: true });
    toggle.addEventListener('click', () => document.body.classList.toggle('menu-lock', links.classList.contains('open')));
  }

  whConsent.init();

  // Contact form -> Base44 sendContactEmail (same backend as the previous site)
  const form = $('.form');
  if (form) form.addEventListener('submit', async e => {
    e.preventDefault();
    const err = $('.form-err', form), v = n => (form.elements[n] ? form.elements[n].value.trim() : '');
    const fail = m => { if (err) { err.textContent = m; err.hidden = false; } };
    if (err) err.hidden = true;
    if (!v('name')) return fail('Vyplňte prosím své jméno.');
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v('email'))) return fail('Zkontrolujte prosím e-mail.');
    if (!v('web') && !v('popis')) return fail('Pošlete odkaz na současný web, nebo napište pár vět o projektu.');
    if (form.elements.consent && !form.elements.consent.checked) return fail('Potvrďte prosím souhlas se zpracováním údajů.');
    const web = v('web');
    const payload = { name: v('name'), company: web, email: v('email'), phone: v('tel'),
      message: (web ? 'Současný web: ' + web + '\n\n' : '') + (v('popis') || '(bez popisu)'), landing: 'Nový web – návrh zdarma do 48 h' };
    form.classList.add('sending');
    try {
      const r = await fetch(WH_API + '/functions/sendContactEmail', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-App-Id': WH_APP }, body: JSON.stringify(payload) });
      if (!r.ok) throw new Error(r.status);
      form.classList.add('sent');
      window.whTrack('lead', 'contact_form');
      if (window.fbq) window.fbq('track', 'Lead');
    } catch (x) {
      fail('Odeslání se nepovedlo. Zkuste to prosím znovu, nebo nám zavolejte na +420 777 611 634.');
    } finally { form.classList.remove('sending'); }
  });

  // Hidden admin tools — triple-click in the footer (IČO = návrhy, © = analytika, firma = poptávky)
  let admLoading = null;
  const loadAdmin = () => admLoading || (admLoading = new Promise((res, rej) => {
    const css = document.createElement('link'); css.rel = 'stylesheet'; css.href = WH_ASSETS + 'admin.min.css?v=' + WH_VER; document.head.appendChild(css);
    const js = document.createElement('script'); js.src = WH_ASSETS + 'admin.min.js?v=' + WH_VER; js.onload = res; js.onerror = rej; document.head.appendChild(js);
  }));
  $$('[data-adm]').forEach(el => {
    let n = 0, t = 0;
    el.addEventListener('click', () => {
      const now = Date.now(); n = now - t < 700 ? n + 1 : 1; t = now;
      if (n >= 3) { n = 0; loadAdmin().then(() => window.WHAdmin.open(el.dataset.adm)); }
    });
  });

  // Chat typing
  const chat = $('[data-chat]');
  if (chat) {
    const answer = 'Dobré reference má například <b>Koupelny Hanák</b>. Specializují se na kompletní rekonstrukce, ceny uvádějí předem a na webu mají fotky hotových zakázek i recenze zákazníků.';
    let chatDone = false;
    const runChat = () => {
      if (chatDone) return; chatDone = true;
      const msgs = $$('.msg', chat);
      const out = $('.ai-text', chat);
      msgs[0].classList.add('in');
      setTimeout(() => msgs[1].classList.add('in'), 700);
      setTimeout(() => {
        $('.typing', chat).remove();
        const plain = answer.replace(/<[^>]+>/g, '');
        let i = 0;
        const tick = () => {
          i += 2; out.textContent = plain.slice(0, i);
          if (i < plain.length) setTimeout(tick, 18);
          else { out.innerHTML = answer; $('.cite', chat).classList.add('in'); }
        };
        tick();
      }, 2000);
    };
    new IntersectionObserver((en, obs) => { if (en[0].isIntersecting) { runChat(); obs.disconnect(); } }, { threshold: 0.4 }).observe(chat);
  }

  // ---------- Who we are: discipline orbit ----------
  const orb = $('.orb');
  if (orb) {
    const core = $('.orb-core', orb), nodes = $$('.orb-node', orb);
    const kEl = $('[data-orb-k]', orb), tEl = $('[data-orb-t]', orb), dEl = $('[data-orb-d]', orb);
    const def = [kEl.textContent, tEl.textContent, dEl.textContent];
    let idx = -1, user = false, visible = false;
    const pick = i => {
      idx = i; nodes.forEach((n, k) => n.classList.toggle('on', k === i));
      core.classList.remove('swap'); void core.offsetWidth; core.classList.add('swap');
      if (i < 0) { [kEl.textContent, tEl.textContent, dEl.textContent] = def; return; }
      kEl.textContent = 'Co přináší vašemu webu'; tEl.textContent = nodes[i].dataset.t; dEl.textContent = nodes[i].dataset.d;
    };
    nodes.forEach((n, k) => {
      n.addEventListener('mouseenter', () => { user = true; pick(k); });
      n.addEventListener('focus', () => { user = true; pick(k); });
      n.addEventListener('click', () => { user = true; pick(k); });
    });
    orb.addEventListener('mouseleave', () => { user = false; });
    new IntersectionObserver(en => { visible = en[0].isIntersecting; }, { threshold: 0.4 }).observe(orb);
    setInterval(() => { if (visible && !user) pick((idx + 1) % nodes.length); }, 3200);
  }

  // ---------- Card spotlight, tilt and object parallax ----------
  if (finePointer) $$('.bnx, .bn').forEach(card => {
    const tilt = card.classList.contains('tilt');
    let raf = 0, ev = null;
    const apply = () => {
      raf = 0; const r = card.getBoundingClientRect();
      const x = (ev.clientX - r.left) / r.width, y = (ev.clientY - r.top) / r.height;
      card.style.setProperty('--mx', (x * 100).toFixed(1) + '%'); card.style.setProperty('--my', (y * 100).toFixed(1) + '%');
      card.style.setProperty('--px', ((x - 0.5) * 2).toFixed(3)); card.style.setProperty('--py', ((y - 0.5) * 2).toFixed(3));
    };
    card.addEventListener('pointermove', e => { ev = e; if (!raf) raf = requestAnimationFrame(apply); });
    card.addEventListener('pointerleave', () => { ['--px', '--py', '--rx', '--ry'].forEach(v => card.style.removeProperty(v)); });
  });

  // ---------- Portfolio showcase ----------
  const sc = $('.showcase');
  if (sc) {
    const items = $$('.sc-item', sc);
    const stage = $('.sc-stage', sc);
    const desk = $('[data-sc-desk]', sc);
    const mob = $('[data-sc-mob]', sc);
    const vp = $('.sc-vp', sc);
    const urlA = $('.sc-url', sc);
    const domEl = $('[data-sc-dom]', sc);
    const cnt = $('[data-sc-count]', sc);
    let cur = 0, t0 = performance.now(), inView = false, hover = false, elapsed = 0;
    const DUR = 9000;
    const fit = () => {
      const d = desk.offsetHeight - vp.offsetHeight;
      desk.style.setProperty('--dist', (-Math.max(0, d)) + 'px');
      desk.style.setProperty('--dur', Math.max(8, d / 170) + 's');
    };
    desk.addEventListener('load', fit); window.addEventListener('resize', fit); if (desk.complete) fit();
    const show = (i, user) => {
      i = (i + items.length) % items.length;
      if (i === cur && !user) return;
      const it = items[i];
      items.forEach((x, k) => { x.classList.toggle('on', k === i); $('.sc-btn', x).setAttribute('aria-expanded', k === i); });
      sc.style.setProperty('--pc', it.dataset.pc); sc.style.setProperty('--pb', it.dataset.pb);
      cnt.textContent = String(i + 1).padStart(2, '0');
      stage.classList.add('out');
      const slug = it.dataset.slug;
      const pre = new Image(); pre.src = `img/pf/${slug}-feat.webp`;
      const swap = () => {
        desk.style.animation = 'none';
        desk.src = pre.src; mob.src = `img/pf/${slug}-m.webp`;
        desk.alt = 'Web ' + $('.nm', it).textContent;
        urlA.href = it.dataset.url; domEl.textContent = it.dataset.dom;
        requestAnimationFrame(() => { desk.style.animation = ''; fit(); stage.classList.remove('out'); });
      };
      setTimeout(() => pre.complete ? swap() : (pre.onload = swap), 380);
      cur = i; t0 = performance.now(); elapsed = 0;
    };
    items.forEach((it, k) => $('.sc-btn', it).addEventListener('click', () => {
      show(k, true);
      if (window.innerWidth < 1025) { if (lenis) lenis.scrollTo(stage, { offset: -90, duration: 1 }); else stage.scrollIntoView({ behavior: 'smooth' }); }
    }));
    $$('[data-sc]', sc).forEach(b => b.addEventListener('click', () => show(cur + (+b.dataset.sc), true)));
    sc.addEventListener('mouseenter', () => hover = true);
    sc.addEventListener('mouseleave', () => hover = false);
    const bars = items.map(x => $('.sc-prog i', x));
    let last = 0, running = false, shownIdx = -1;
    const tick = now => {
      if (!inView) { running = false; return; }
      const dt = last ? now - last : 0; last = now;
      if (!hover) elapsed += dt;
      if (shownIdx !== cur) { bars.forEach(b => b.style.transform = 'scaleX(0)'); shownIdx = cur; }
      bars[cur].style.transform = `scaleX(${Math.min(1, elapsed / DUR)})`;
      if (elapsed >= DUR) show(cur + 1);
      requestAnimationFrame(tick);
    };
    new IntersectionObserver(en => {
      inView = en[0].isIntersecting;
      if (inView && !running) { running = true; last = 0; requestAnimationFrame(tick); }
    }, { threshold: 0.2 }).observe(sc);
  }

  // ---------- Portfolio cards: hover scroll-through ----------
  if (finePointer) $$('.pf-card').forEach(c => {
    const vp = $('.pf-vp', c), tall = $('.pf-tall', c);
    if (!vp || !tall) return;
    const go = () => {
      const d = tall.offsetHeight - vp.offsetHeight;
      if (d <= 0) return;
      c.classList.add('scrolling');
      tall.style.transition = `transform ${Math.max(3, d / 260)}s linear, opacity .35s`;
      tall.style.transform = `translateY(${-d}px)`;
    };
    c.addEventListener('mouseenter', () => {
      c._hover = true;
      if (!tall.dataset.loaded) { tall.dataset.loaded = '1'; tall.onload = () => c._hover && go(); tall.src = tall.dataset.src; }
      else if (tall.complete) go();
    });
    c.addEventListener('mouseleave', () => {
      c._hover = false; c.classList.remove('scrolling');
      tall.style.transition = 'transform .9s cubic-bezier(.16,1,.3,1), opacity .35s';
      tall.style.transform = 'translateY(0)';
    });
  });

  // ---------- Portfolio archive filters ----------
  const grid = $('.pf-grid');
  if (grid) {
    const cards = $$('.pf-card', grid);
    const moreBtn = $('[data-more]');
    let filter = 'all', expanded = !moreBtn;
    const LIMIT = 9;
    const apply = anim => {
      let n = 0;
      cards.forEach(c => {
        const match = filter === 'all' || c.dataset.cat === filter;
        const vis = match && (filter !== 'all' || expanded || n < LIMIT);
        if (vis) n++;
        const was = !c.hidden; c.hidden = !vis;
        if (vis && anim && (!was || anim === 'all')) { c.classList.remove('fade'); void c.offsetWidth; c.style.animationDelay = Math.min(n, 12) * 0.04 + 's'; c.classList.add('fade'); }
      });
      if (moreBtn) moreBtn.hidden = !(filter === 'all' && !expanded);
      if (hasGsap) setTimeout(() => ScrollTrigger.refresh(), 100);
    };
    $$('.filter').forEach(b => b.addEventListener('click', () => {
      $$('.filter').forEach(x => x.classList.toggle('on', x === b));
      filter = b.dataset.f; apply('all');
    }));
    if (moreBtn) moreBtn.addEventListener('click', () => { expanded = true; apply(true); });
    apply(false);
  }

  if (!hasGsap) { $$('.fw').forEach(w => w.classList.add('on')); return; }
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });
  const ifEl = (sel, fn) => { const el = $(sel); if (el) fn(el); };

  gsap.to('.scroll-progress', { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: 0.3 } });

  // Hero intro (homepage)
  const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
  tl.from('.nav-inner > *', { y: -20, opacity: 0, duration: 1, stagger: 0.06, clearProps: 'transform' }, 0.2);
  ifEl('.hero-frame', () => {
    tl.from('.hero-bg img', { scale: 1.15, duration: 2.4, ease: 'power3.out' }, 0)
      .from('.hero-pill', { y: 20, opacity: 0, duration: 1 }, 0.2)
      .from('.hero h1 .w > span', { yPercent: 110, duration: 1.2, stagger: 0.055 }, 0.3)
      .from('.hero-sub, .hero-buttons', { y: 24, opacity: 0, duration: 1.1, stagger: 0.1 }, 0.75)
      .from('.hc-card', { y: 260, opacity: 0, duration: 1.6, stagger: { each: 0.08, from: 'center' } }, 0.6);
    gsap.to('.ring-stage', { y: -80, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 } });
  });
  // Subpage hero intro
  ifEl('.sub-frame', () => {
    tl.from('.sub-bg img', { scale: 1.12, duration: 2.2, ease: 'power3.out' }, 0)
      .from('.sub-hero h1 .w > span', { yPercent: 110, duration: 1.2, stagger: 0.06 }, 0.25)
      .from('.sub-copy .crumbs, .sub-copy p, .sub-copy .work-stats', { y: 24, opacity: 0, duration: 1.1, stagger: 0.1 }, 0.6)
      .from('.fan-card', { y: 160, opacity: 0, rotate: 0, duration: 1.6, stagger: 0.12 }, 0.5);
  });
  if (window.innerWidth >= 1100 && $('.rail-group')) tl.from('.rail-group', { x: -30, opacity: 0, duration: 1.1, stagger: 0.1 }, 0.5);

  // Ring follows mouse
  const ring = $('.ring');
  if (finePointer && ring) {
    const hero = $('.hero-frame');
    gsap.set(ring, { z: -1100, rotationX: -4 });
    const rx = gsap.quickTo(ring, 'rotationY', { duration: 1.4, ease: 'power3.out' });
    hero.addEventListener('mousemove', e => {
      const r = hero.getBoundingClientRect();
      rx(((e.clientX - r.left) / r.width - 0.5) * -10);
    });
  }

  // Parallax
  gsap.utils.toArray('.sky-par').forEach(img => {
    gsap.fromTo(img, { yPercent: -5 }, { yPercent: 5, ease: 'none', scrollTrigger: { trigger: img.closest('section'), start: 'top bottom', end: 'bottom top', scrub: 1 } });
  });
  gsap.utils.toArray('.bento-par').forEach(img => {
    gsap.fromTo(img, { yPercent: -4 }, { yPercent: 4, ease: 'none', scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: 1 } });
  });

  // Fill words
  const fws = gsap.utils.toArray('.fw');
  if (fws.length) ScrollTrigger.create({
    trigger: '.fill-text', start: 'top 80%', end: 'bottom 45%', scrub: true,
    onUpdate: self => { const n = Math.round(self.progress * fws.length); if (n === fws._n) return; fws._n = n; fws.forEach((w, i) => w.classList.toggle('on', i < n)); }
  });

  // Reveals — one IntersectionObserver + CSS transitions instead of dozens of ScrollTriggers
  const rvIO = new IntersectionObserver(entries => entries.forEach(en => {
    if (!en.isIntersecting && en.boundingClientRect.top > 0) return;
    (en.target._rvItems || [en.target]).forEach(x => x.classList.add('rv-in'));
    rvIO.unobserve(en.target);
  }), { rootMargin: '100000px 0px -12% 0px' });
  const reveal = (trigger, items, { y = 40, s = 1, step = 0, random = false } = {}) => {
    items = [...items]; if (!items.length) return;
    const order = items.map((_, i) => i);
    if (random) order.sort(() => Math.random() - 0.5);
    items.forEach((el, i) => {
      el.classList.add('js-rv');
      el.style.setProperty('--rv-y', y + 'px');
      if (s !== 1) el.style.setProperty('--rv-s', s);
      if (step) el.style.setProperty('--rv-d', Math.min(order[i] * step, 0.6) + 's');
    });
    trigger._rvItems = items; rvIO.observe(trigger);
  };
  $$('.reveal').forEach(el => reveal(el, [el]));
  $$('.reveal-group').forEach(g => reveal(g, g.querySelectorAll('.reveal-item'), { step: 0.08 }));
  ifEl('.bento', el => reveal(el, $$('.b-card', el), { y: 70, s: 0.96, step: 0.1, random: true }));
  ifEl('.wt-grid', el => reveal(el, el.children, { y: 60, step: 0.12 }));
  ifEl('.showcase', el => { reveal(el, $$('.sc-stage', el), { y: 80 }); reveal($('.sc-list', el), $$('.sc-item', el), { y: 30, step: 0.06 }); });
  ifEl('.sv-grid', el => reveal(el, $$('.sv', el), { y: 60, step: 0.08 }));
  ifEl('.p-steps', el => reveal(el, $$('.p-step', el), { y: 90, step: 0.15 }));

  // Process: cards rise, track fills (no pin)
  ifEl('.p-steps', el => {
    const nodes = $$('.p-node');
    gsap.to('.p-track .line i', {
      scaleX: 1, ease: 'none',
      scrollTrigger: { trigger: el, start: 'top 80%', end: 'bottom 60%', scrub: 1,
        onUpdate: self => nodes.forEach((n, i) => n.classList.toggle('on', self.progress >= i / 2 - 0.01)) }
    });
  });

  // Compare intro sweep
  ifEl('[data-compare]', cmpS => {
    const o = { p: 88 };
    const cio = new IntersectionObserver(en => {
      if (!en[0].isIntersecting) return; cio.disconnect();
      gsap.to(o, { p: 50, duration: 1.8, ease: 'expo.inOut',
        onUpdate: () => { if (!cmpS._touched) cmpS.style.setProperty('--pos', o.p + '%'); } });
    }, { rootMargin: '0px 0px -25% 0px' });
    cio.observe(cmpS);
  });

  // Frames open up as they enter (smoother section transitions)
  const from = window.innerWidth < 768 ? 0.95 : 0.92;
  gsap.utils.toArray('.showcase, .p-frame, .geo, .faq-panel, .cta-frame, .cta-band').forEach(fr => {
    gsap.fromTo(fr, { scale: from, transformOrigin: '50% 0%' }, {
      scale: 1, ease: 'none', force3D: true,
      scrollTrigger: { trigger: fr, start: 'top bottom', end: 'top 30%', scrub: 0.6 }
    });
  });

  window.addEventListener('load', () => ScrollTrigger.refresh());
});
