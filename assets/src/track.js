/* WebHunter analytics tracker — loaded only after analytics consent.
   Writes one record per page view into Base44 entity LandingPageMetric (same entity as the previous site).
   Rich details live as JSON in `sections_viewed` (the entity schema is fixed). */
(() => {
  if (window.__whTrackOn) return; window.__whTrackOn = true;
  try { if (localStorage.getItem('wh_notrack')) return; } catch (e) {}
  // measure only on the production domain (preview / GitHub Pages / localhost is never recorded)
  if (!/(^|\.)webhunter\.cz$/.test(location.hostname)) return;
  const APP = '6a366c8ba95efe01593d4844';
  const URL_ = 'https://base44.app/api/apps/' + APP + '/entities/LandingPageMetric';
  const H = { 'Content-Type': 'application/json', 'X-App-Id': APP };
  const ls = (k, v) => { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } };
  const rid = p => p + Date.now().toString(36) + Math.random().toString(36).slice(2, 9);
  const t0 = performance.now();

  // visitor + session
  let vid = ls('wh_vid'); const isNew = !vid; if (!vid) { vid = rid('v_'); ls('wh_vid', vid); ls('wh_first', new Date().toISOString()); }
  let sid = null; try { sid = sessionStorage.getItem('wh_landing_session'); } catch (e) {}
  const newSession = !sid;
  if (!sid) { sid = 's_' + Date.now() + '_' + Math.random().toString(36).slice(2, 10); try { sessionStorage.setItem('wh_landing_session', sid); } catch (e) {} }
  let visits = parseInt(ls('wh_visits') || '0', 10); if (newSession) { visits += 1; ls('wh_visits', String(visits)); }

  // source (same labels as the previous site: Google, Meta, LinkedIn, direct …)
  const q = new URLSearchParams(location.search);
  const utm = {}; ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(k => { if (q.get(k)) utm[k.slice(4)] = q.get(k).slice(0, 80); });
  if (q.get('gclid')) utm.gclid = 1; if (q.get('fbclid')) utm.fbclid = 1;
  let refHost = ''; try { refHost = document.referrer ? new URL(document.referrer).hostname.replace(/^www\./, '') : ''; } catch (e) {}
  const internal = refHost && refHost === location.hostname.replace(/^www\./, '');
  const classify = h => {
    if (!h) return 'direct';
    if (/google\./.test(h)) return 'Google'; if (/seznam\.cz|szn\.cz/.test(h)) return 'Seznam'; if (/bing\./.test(h)) return 'Bing';
    if (/facebook|instagram|fb\.com|m\.me/.test(h)) return 'Meta'; if (/linkedin|lnkd/.test(h)) return 'LinkedIn';
    if (/chatgpt|openai/.test(h)) return 'ChatGPT'; if (/perplexity/.test(h)) return 'Perplexity'; if (/gemini|bard/.test(h)) return 'Gemini'; if (/copilot/.test(h)) return 'Copilot';
    if (/t\.co$|twitter|x\.com/.test(h)) return 'X'; if (/youtube/.test(h)) return 'YouTube'; if (/tiktok/.test(h)) return 'TikTok';
    if (/mail|email|seznam\.cz\/email|outlook/.test(h)) return 'E-mail';
    return h;
  };
  const source = utm.source ? utm.source : internal ? 'internal' : classify(refHost);

  // device / environment
  const ua = navigator.userAgent;
  const device = /iPad|Tablet/i.test(ua) || (/Android/i.test(ua) && !/Mobile/i.test(ua)) ? 'tablet' : /Mobi|iPhone|Android/i.test(ua) || innerWidth < 768 ? 'mobile' : 'desktop';
  const br = /Edg\//.test(ua) ? 'Edge' : /OPR\/|Opera/.test(ua) ? 'Opera' : /SamsungBrowser/.test(ua) ? 'Samsung' : /Firefox\//.test(ua) ? 'Firefox' : /Chrome\//.test(ua) ? 'Chrome' : /Safari\//.test(ua) ? 'Safari' : 'Jiný';
  const os = /Windows/.test(ua) ? 'Windows' : /iPhone|iPad|iPod/.test(ua) ? 'iOS' : /Mac OS X/.test(ua) ? 'macOS' : /Android/.test(ua) ? 'Android' : /Linux/.test(ua) ? 'Linux' : 'Jiný';
  const nav = (performance.getEntriesByType && performance.getEntriesByType('navigation')[0]) || {};

  // state
  const d = {
    v: 2, vid, new: isNew, n: visits, ns: newSession, path: location.pathname.replace(/\/webhunter-web/, '') || '/', title: document.title.slice(0, 90),
    ref: refHost, utm, br, os, lang: (navigator.language || '').slice(0, 5), scr: screen.width + 'x' + screen.height, vp: innerWidth + 'x' + innerHeight,
    dpr: Math.round((devicePixelRatio || 1) * 10) / 10, tz: (Intl.DateTimeFormat().resolvedOptions().timeZone || ''), nt: nav.type || '',
    secs: [], ev: [], vit: {}, eng: 0
  };
  let id = null, active = 0, lastTick = performance.now(), visible = document.visibilityState === 'visible', scrollMax = 0, submitted = false, dirty = true;
  const now = () => Math.round((performance.now() - t0) / 1000);
  const ev = (type, label) => { if (d.ev.length >= 80) return; d.ev.push([now(), type, String(label || '').slice(0, 80)]); dirty = true; };

  // active time
  const tick = () => { const n = performance.now(); if (visible) active += n - lastTick; lastTick = n; };
  document.addEventListener('visibilitychange', () => { tick(); visible = document.visibilityState === 'visible'; if (!visible) flush(true); });
  setInterval(tick, 1000);

  // scroll depth
  const onScroll = () => { const h = document.documentElement.scrollHeight - innerHeight; const p = h > 0 ? Math.min(100, Math.round(scrollY / h * 100)) : 100; if (p > scrollMax) { scrollMax = p; dirty = true; } };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // sections reached
  const secIO = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const k = e.target.id || e.target.dataset.section; if (k && !d.secs.includes(k)) { d.secs.push(k); dirty = true; } secIO.unobserve(e.target); } }), { threshold: 0.35 });
  document.querySelectorAll('main > section[id], main > section[data-section], footer').forEach(el => { if (!el.id && el.tagName === 'FOOTER') el.dataset.section = 'paticka'; secIO.observe(el); });

  // interactions
  document.addEventListener('click', e => {
    const a = e.target.closest('a, button, summary, [data-adm]'); if (!a || a.closest('.wa, .wp')) return;
    const txt = (a.getAttribute('aria-label') || a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50);
    const href = a.getAttribute && a.getAttribute('href');
    if (href && /^tel:/.test(href)) return ev('tel', href.slice(4));
    if (href && /wa\.me\//.test(href)) return ev('wa', 'WhatsApp');
    if (href && /^mailto:/.test(href)) return ev('mail', href.slice(7));
    if (a.matches('[data-ba-case]')) return ev('ba', a.dataset.baCase);
    if (a.matches('.filter')) return ev('filter', a.dataset.f);
    if (a.matches('.qa .q')) return ev('faq', txt);
    if (a.matches('.sc-btn, [data-sc]')) return ev('showcase', txt);
    if (a.matches('[data-cookie-settings]')) return;
    if (href && /^https?:/.test(href)) { let h = ''; try { h = new URL(href).hostname.replace(/^www\./, ''); } catch (x) {} if (h && h !== location.hostname.replace(/^www\./, '')) return ev('out', h); }
    if (a.closest('.nav, .rail')) return ev('nav', txt || href);
    if (a.matches('.btn, .m-cta, .hero-alt, .cta-contact a, .sc-link')) return ev('cta', txt);
  }, true);
  document.addEventListener('submit', e => { if (e.target.matches('.hero-url')) ev('hero_form', (e.target.querySelector('input') || {}).value ? 'vyplněno' : 'prázdné'); }, true);
  document.addEventListener('focusin', e => { const f = e.target.closest('.form'); if (f && !f._whStarted) { f._whStarted = 1; ev('form_start', e.target.name); } });

  // web vitals
  try {
    new PerformanceObserver(l => { const e = l.getEntries().pop(); if (e) d.vit.lcp = Math.round(e.startTime); }).observe({ type: 'largest-contentful-paint', buffered: true });
    let cls = 0; new PerformanceObserver(l => { l.getEntries().forEach(e => { if (!e.hadRecentInput) cls += e.value; }); d.vit.cls = Math.round(cls * 1000) / 1000; }).observe({ type: 'layout-shift', buffered: true });
    let inp = 0; new PerformanceObserver(l => { l.getEntries().forEach(e => { if (e.interactionId && e.duration > inp) { inp = e.duration; d.vit.inp = Math.round(inp); } }); }).observe({ type: 'event', buffered: true, durationThreshold: 40 });
    if (nav.responseStart) d.vit.ttfb = Math.round(nav.responseStart);
  } catch (e) {}

  // public API used by the site (queued calls from before load are replayed)
  const api = (type, label) => { if (type === 'lead') { submitted = true; ev('lead', label); flush(); } else ev(type, label); };
  (window.whTrackQ || []).forEach(a => api.apply(null, a)); window.whTrack = api;

  // persistence
  const body = () => { tick(); d.eng = Math.round(active / 1000); return { duration_seconds: d.eng, scroll_depth_max: scrollMax, submitted_form: submitted, sections_viewed: JSON.stringify(d) }; };
  const create = () => fetch(URL_, { method: 'POST', headers: H, body: JSON.stringify(Object.assign({ session_id: sid, source, entry_url: location.href.split('#')[0].slice(0, 300), device }, body())) })
    .then(r => r.ok ? r.json() : null).then(j => { if (j && j.id) { id = j.id; dirty = false; } }).catch(() => {});
  function flush(unload) {
    if (!id) return; if (!dirty && !unload && !visible) return; dirty = false;
    try { fetch(URL_ + '/' + id, { method: 'PUT', headers: H, body: JSON.stringify(body()), keepalive: !!unload }).catch(() => {}); } catch (e) {}
  }
  create();
  setInterval(() => flush(false), 15000);
  addEventListener('pagehide', () => flush(true));
})();
