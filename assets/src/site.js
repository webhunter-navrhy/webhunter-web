/* WebHunter — shared site script */
const WH_ASSETS = (document.currentScript && document.currentScript.src.replace(/site(\.min)?\.js.*$/, '')) || 'assets/';
const WH_VER = ((document.currentScript && document.currentScript.src.match(/[?&]v=(\d+)/)) || [])[1] || '1';
const WH_APP = '6a366c8ba95efe01593d4844';
const WH_API = 'https://base44.app/api/apps/' + WH_APP;
const WH_PIXEL = '1023099023693684';
const WH_IMG = WH_ASSETS + '../img/';
const WH_EN = (document.documentElement.lang || '').startsWith('en');
const tr = (cs, en) => (WH_EN ? en : cs);
if (navigator.webdriver) document.documentElement.classList.add('wh-bot');
// Lite mode for weaker computers (few cores / little memory / reduced motion): no glass blur, calmer card effects
const WH_LITE = /[?&]lite=1/.test(location.search) || (!/[?&]lite=0/.test(location.search) && (
  (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4) || (navigator.deviceMemory && navigator.deviceMemory <= 4) ||
  window.matchMedia('(prefers-reduced-motion: reduce)').matches));
if (WH_LITE) document.documentElement.classList.add('lite');
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
    const pl = document.querySelector('a[href$="ochrana-osobnich-udaju/"], a[href$="privacy/"]');
    const privacy = pl ? pl.getAttribute('href') : 'ochrana-osobnich-udaju/';
    const d = document.createElement('div'); d.className = 'ck'; d.hidden = true;
    const img = WH_ASSETS + '../img/3d/shield-s.webp';
    d.innerHTML = WH_EN ? `<div class="ck-card bnx bnv-dark" role="dialog" aria-modal="false" aria-labelledby="ck-t">
      <div class="bn-fx" aria-hidden="true"><span class="bn-pat"></span><span class="bn-orb o1"></span><span class="bn-orb o2"></span><i class="sp s1"></i><i class="sp s2"></i></div>
      <img class="ck-obj" src="${img}" alt="" width="240" height="321" decoding="async">
      <div class="ck-head">
        <span class="bn-chip">Cookies &amp; privacy</span>
        <h2 id="ck-t">We value your <span class="serif">privacy.</span></h2>
        <p>Necessary cookies keep the website running. Analytics cookies help us improve it and marketing cookies measure how our ads perform. We only use optional cookies with your consent, which you can change at any time in the footer. More in our <a href="${privacy}">privacy policy</a>.</p>
      </div>
      <div class="ck-opts" hidden>
        <label class="ck-opt"><b>Necessary</b><small>Stores your choice and basic website functions. Always on.</small><span class="ck-sw"><input type="checkbox" checked disabled><i></i></span></label>
        <label class="ck-opt"><b>Analytics</b><small>Anonymous visit statistics, so we know what works on the website.</small><span class="ck-sw"><input type="checkbox" data-ck="a"><i></i></span></label>
        <label class="ck-opt"><b>Marketing</b><small>Meta Pixel to measure and target ads on Facebook and Instagram.</small><span class="ck-sw"><input type="checkbox" data-ck="m"><i></i></span></label>
      </div>
      <div class="ck-btns"><button type="button" class="ck-s" data-ck-set>Settings</button><button type="button" class="ck-r" data-ck-no>Necessary only</button><button type="button" class="ck-a" data-ck-yes>Accept all <span class="arr"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button></div>
    </div>` : `<div class="ck-card bnx bnv-dark" role="dialog" aria-modal="false" aria-labelledby="ck-t">
      <div class="bn-fx" aria-hidden="true"><span class="bn-pat"></span><span class="bn-orb o1"></span><span class="bn-orb o2"></span><i class="sp s1"></i><i class="sp s2"></i></div>
      <img class="ck-obj" src="${img}" alt="" width="240" height="321" decoding="async">
      <div class="ck-head">
        <span class="bn-chip">Cookies &amp; soukromí</span>
        <h2 id="ck-t">Vážíme si vašeho <span class="serif">soukromí.</span></h2>
        <p>Nezbytné cookies zajišťují fungování webu. Analytické nám pomáhají web zlepšovat a marketingové měří účinnost reklam. Volitelné použijeme jen s vaším souhlasem, který můžete kdykoli změnit v patičce. Více v <a href="${privacy}">zásadách ochrany osobních údajů</a>.</p>
      </div>
      <div class="ck-opts" hidden>
        <label class="ck-opt"><b>Nezbytné</b><small>Uložení vaší volby a základní funkce webu. Vždy zapnuté.</small><span class="ck-sw"><input type="checkbox" checked disabled><i></i></span></label>
        <label class="ck-opt"><b>Analytické</b><small>Anonymní statistiky návštěvnosti, abychom věděli, co na webu funguje.</small><span class="ck-sw"><input type="checkbox" data-ck="a"><i></i></span></label>
        <label class="ck-opt"><b>Marketingové</b><small>Meta Pixel pro měření a cílení reklam na Facebooku a Instagramu.</small><span class="ck-sw"><input type="checkbox" data-ck="m"><i></i></span></label>
      </div>
      <div class="ck-btns"><button type="button" class="ck-s" data-ck-set>Nastavení</button><button type="button" class="ck-r" data-ck-no>Pouze nutné</button><button type="button" class="ck-a" data-ck-yes>Přijmout vše <span class="arr"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button></div>
    </div>`;
    d.querySelector('.ck-card').classList.add('bn-live');
    document.body.appendChild(d);
    const opts = d.querySelector('.ck-opts'), setBtn = d.querySelector('[data-ck-set]');
    const close = () => { d.hidden = true; document.body.classList.remove('ck-open'); };
    d.querySelector('[data-ck-yes]').addEventListener('click', () => { save(true, true); close(); });
    d.querySelector('[data-ck-no]').addEventListener('click', () => { save(false, false); close(); });
    setBtn.addEventListener('click', () => {
      if (opts.hidden) { opts.hidden = false; setBtn.textContent = tr('Uložit výběr', 'Save choice'); return; }
      save(d.querySelector('[data-ck="a"]').checked, d.querySelector('[data-ck="m"]').checked); close();
    });
    return { el: d, opts, setBtn };
  };
  const open = (detailed) => {
    ui = ui || build();
    const c = read() || { a: false, m: false };
    ui.el.querySelector('[data-ck="a"]').checked = !!c.a; ui.el.querySelector('[data-ck="m"]').checked = !!c.m;
    ui.opts.hidden = !detailed; ui.setBtn.textContent = detailed ? tr('Uložit výběr', 'Save choice') : tr('Nastavení', 'Settings');
    ui.el.hidden = false; document.body.classList.add('ck-open');
  };
  const init = () => {
    const c = read();
    if (c) apply(c); else setTimeout(() => open(false), navigator.webdriver ? 0 : 900);
    document.querySelectorAll('[data-cookie-settings]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); open(true); }));
  };
  return { read, save, open, init };
})();
window.whConsent = whConsent;

document.addEventListener('DOMContentLoaded', () => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const hasGsap = typeof gsap !== 'undefined';
  const nav = $('.nav');
  const finePointer = window.matchMedia('(pointer: fine)').matches;

  // Native scrolling (no JS smooth-scroll library): the browser scrolls on the compositor thread,
  // so slow trackpad scrolling stays perfectly smooth even on weaker computers.
  const smoothTo = (el, offset = -10) => window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY + offset, behavior: 'smooth' });
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const el = $(id);
      if (!el) return;
      e.preventDefault();
      closeMenu();
      if (id === '#top') window.scrollTo({ top: 0, behavior: 'smooth' }); else smoothTo(el);
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

  // ---------- Mobile: swipe rails + auto-hiding nav ----------
  const mq = window.matchMedia('(max-width: 767px)');
  const rails = [];
  const makeRail = (el, items) => {
    if (!el || el._rail || (items && !items.length)) return;
    let host = el;
    if (items) { // move a subset of children into a new rail (services: keep the before/after card full width)
      host = document.createElement('div'); host.className = el.className.replace(/\bsv-grid\b/, '') + ' sv-rail';
      el._moved = items; items.forEach(n => host.appendChild(n)); el.appendChild(host);
    }
    host.classList.add('m-rail'); el._rail = host;
    const dots = document.createElement('div'); dots.className = 'm-rail-dots'; dots.setAttribute('aria-hidden', 'true');
    const kids = [...host.children]; dots.innerHTML = kids.map((_, i) => `<i class="${i ? '' : 'on'}"></i>`).join('');
    host.after(dots);
    let raf = 0;
    host.addEventListener('scroll', () => { if (raf) return; raf = requestAnimationFrame(() => { raf = 0;
      const w = kids[0].getBoundingClientRect().width + 12; const i = Math.round(host.scrollLeft / w);
      [...dots.children].forEach((d, k) => d.classList.toggle('on', k === Math.min(i, kids.length - 1))); }); }, { passive: true });
    rails.push({ el, host, dots });
  };
  const unRail = () => rails.splice(0).forEach(({ el, host, dots }) => {
    dots.remove();
    if (el._moved) { el._moved.forEach(n => el.appendChild(n)); host.remove(); el._moved = null; } else host.classList.remove('m-rail');
    el._rail = null;
  });
  const applyRails = () => {
    if (!mq.matches) { unRail(); return; }
    makeRail($('.bento')); makeRail($('.p-steps')); makeRail($('.vals')); makeRail($('.svc-more')); makeRail($('.svc-pf')); makeRail($('.post-cards-3'));
    const sv = $('.sv-grid'); if (sv) makeRail(sv, $$('.sv', sv).filter(n => !n.classList.contains('sv-ba')));
  };
  applyRails(); mq.addEventListener('change', applyRails);

  let lastY = window.scrollY;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (mq.matches) nav.classList.toggle('nav-hide', y > lastY && y > 300);
    lastY = y;
  }, { passive: true });

  // Nav state
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 60);
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Rail active section — IntersectionObserver on a thin band at 45 % of the viewport (no per-frame measuring)
  const railLinks = $$('.rail a[data-sec]');
  if (railLinks.length && 'IntersectionObserver' in window) {
    const setRail = id => railLinks.forEach(l => l.classList.toggle('active', l.dataset.sec === id && !l.classList.contains('rail-cta')));
    const rio = new IntersectionObserver(en => en.forEach(x => { if (x.isIntersecting) setRail(x.target.dataset.section); }), { rootMargin: '-45% 0px -54% 0px' });
    $$('[data-section]').forEach(sct => rio.observe(sct));
  }

  // Blog: highlight the table-of-contents entry of the section being read (only recalculated when a heading crosses the line)
  const tocLinks = $$('.post-toc a[href^="#"]').filter(a => a.getAttribute('href').length > 1 && a.getAttribute('href') !== '#kontakt');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const heads = tocLinks.map(a => document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
    const tu = () => { let cur = heads[0]; for (const h of heads) { if (h.getBoundingClientRect().top < innerHeight * 0.35) cur = h; else break; }
      tocLinks.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + cur.id)); };
    const tio = new IntersectionObserver(tu, { rootMargin: '0px 0px -65% 0px' });
    heads.forEach(h => tio.observe(h)); tu();
  }

  // Banner card effects animate only while the card is (nearly) on screen — keeps the layer count low while scrolling
  const bnCards = $$('.bn, .bnx');
  if ('IntersectionObserver' in window) {
    const bnIO = new IntersectionObserver(entries => entries.forEach(en => en.target.classList.toggle('bn-live', en.isIntersecting)), { rootMargin: '120px 0px' });
    bnCards.forEach(c => bnIO.observe(c));
  } else bnCards.forEach(c => c.classList.add('bn-live'));

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
      pre[0].src = `${WH_IMG}ba/${k}-before.webp`; pre[1].src = `${WH_IMG}ba/${k}-after.webp`;
      ba.classList.add('swap');
      Promise.all(pre.map(im => im.decode().catch(() => {}))).then(() => setTimeout(() => {
        bImg.src = pre[0].src; aImg.src = pre[1].src;
        bImg.alt = tr(`Původní web ${t.dataset.name} z roku ${t.dataset.year}`, `The original ${t.dataset.name} website from ${t.dataset.year}`); aImg.alt = tr(`Nový web ${t.dataset.name} od WebHunter`, `The new ${t.dataset.name} website by WebHunter`);
        lTag.textContent = tr('Předtím', 'Before') + ` · ${t.dataset.year}`;
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
    smoothTo(target);
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
    $$('.hero, .sub-hero, #kontakt, .cta-band, footer').forEach(el => mio.observe(el));
    window.addEventListener('scroll', sync, { passive: true });
    toggle.addEventListener('click', () => document.body.classList.toggle('menu-lock', links.classList.contains('open')));
  }

  whConsent.init();

  // WhatsApp quick contact (floating button on every page)
  const WA_NUM = '420777611634';
  const isEN = WH_EN;
  const waText = isEN ? 'Hello, I am interested in a free website design.' : 'Dobrý den, mám zájem o návrh webu zdarma.';
  const waUrl = 'https://wa.me/' + WA_NUM + '?text=' + encodeURIComponent(waText);
  const WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm0 18.13c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.36c0-4.54 3.7-8.23 8.24-8.23 4.54 0 8.23 3.69 8.23 8.23 0 4.54-3.69 8.22-8.22 8.22Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.08.14-1.18-.06-.1-.22-.16-.47-.28Z"/></svg>';
  const fab = document.createElement('a');
  fab.className = 'wa-fab'; fab.href = waUrl; fab.target = '_blank'; fab.rel = 'noopener';
  fab.setAttribute('aria-label', isEN ? 'Message us on WhatsApp' : 'Napište nám na WhatsApp');
  fab.innerHTML = WA_SVG + '<span>' + (isEN ? 'WhatsApp us' : 'Napište na WhatsApp') + '</span>';
  document.body.appendChild(fab);
  $$('[data-wa]').forEach(a => { a.href = waUrl; a.target = '_blank'; a.rel = 'noopener'; });
  document.addEventListener('click', e => { if (e.target.closest('.wa-fab, [data-wa]')) window.whTrack('wa', 'whatsapp'); if (window.fbq && e.target.closest('.wa-fab, [data-wa]')) window.fbq('track', 'Contact'); });

  // Contact form -> Base44 sendContactEmail (same backend as the previous site)
  const form = $('.form');
  if (form) form.addEventListener('submit', async e => {
    e.preventDefault();
    const err = $('.form-err', form), v = n => (form.elements[n] ? form.elements[n].value.trim() : '');
    const fail = m => { if (err) { err.textContent = m; err.hidden = false; } };
    if (err) err.hidden = true;
    if (!v('name')) return fail(tr('Vyplňte prosím své jméno.', 'Please enter your name.'));
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v('email'))) return fail(tr('Zkontrolujte prosím e-mail.', 'Please check your email address.'));
    if (!v('web') && !v('popis')) return fail(tr('Pošlete odkaz na současný web, nebo napište pár vět o projektu.', 'Send a link to your current website or write a few lines about your project.'));
    if (form.elements.consent && !form.elements.consent.checked) return fail(tr('Potvrďte prosím souhlas se zpracováním údajů.', 'Please confirm the data processing notice.'));
    const web = v('web');
    const payload = { name: v('name'), company: web, email: v('email'), phone: v('tel'),
      message: (web ? 'Současný web: ' + web + '\n\n' : '') + (v('popis') || '(bez popisu)') + (WH_EN ? '\n\n[EN verze webu]' : ''), landing: form.dataset.landing || 'Nový web – návrh zdarma do 48 h' };
    form.classList.add('sending');
    try {
      const r = await fetch(WH_API + '/functions/sendContactEmail', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-App-Id': WH_APP }, body: JSON.stringify(payload) });
      if (!r.ok) throw new Error(r.status);
      form.classList.add('sent');
      window.whTrack('lead', 'contact_form');
      if (window.fbq) window.fbq('track', 'Lead');
    } catch (x) {
      fail(tr('Odeslání se nepovedlo. Zkuste to prosím znovu, nebo nám zavolejte na +420 777 611 634.', 'Sending failed. Please try again or call us at +420 777 611 634.'));
    } finally { form.classList.remove('sending'); }
  });

  // Hidden admin tools — triple-click in the footer (IČO = návrhy, © = analytika, firma = poptávky)
  let admLoading = null;
  const loadAdmin = () => admLoading || (admLoading = new Promise((res, rej) => {
    const css = document.createElement('link'); css.rel = 'stylesheet'; css.href = WH_ASSETS + 'admin.min.css?v=' + WH_VER; document.head.appendChild(css);
    const js = document.createElement('script'); js.src = WH_ASSETS + 'admin.min.js?v=' + WH_VER; js.onload = res; js.onerror = rej; document.head.appendChild(js);
  }));
  // like the previous site: every 3rd click opens the tool (no time limit — external automations click it too)
  $$('[data-adm]').forEach(el => {
    let n = 0;
    el.addEventListener('click', () => {
      n += 1;
      if (n >= 3) { n = 0; loadAdmin().then(() => window.WHAdmin.open(el.dataset.adm)); }
    });
  });

  // Chat typing
  const chat = $('[data-chat]');
  if (chat) {
    const answer = tr('Dobré reference má například <b>Koupelny Hanák</b>. Specializují se na kompletní rekonstrukce, ceny uvádějí předem a na webu mají fotky hotových zakázek i recenze zákazníků.', '<b>Koupelny Hanák</b> has great references, for example. They specialise in complete renovations, publish their prices upfront and show photos of finished jobs and customer reviews on their website.');
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
      kEl.textContent = tr('Co přináší vašemu webu', 'What it brings to your website'); tEl.textContent = nodes[i].dataset.t; dEl.textContent = nodes[i].dataset.d;
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
      const pre = new Image(); pre.src = `${WH_IMG}pf/${slug}-feat.webp`;
      const swap = () => {
        desk.style.animation = 'none';
        desk.src = pre.src; mob.src = `${WH_IMG}pf/${slug}-m.webp`;
        desk.alt = 'Web ' + $('.nm', it).textContent;
        urlA.href = it.dataset.url; domEl.textContent = it.dataset.dom;
        requestAnimationFrame(() => { desk.style.animation = ''; fit(); stage.classList.remove('out'); });
      };
      setTimeout(() => pre.complete ? swap() : (pre.onload = swap), 380);
      cur = i; t0 = performance.now(); elapsed = 0;
    };
    items.forEach((it, k) => $('.sc-btn', it).addEventListener('click', () => {
      show(k, true);
      if (window.innerWidth < 1025) { smoothTo(stage, -90); }
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
    };
    $$('.filter').forEach(b => b.addEventListener('click', () => {
      $$('.filter').forEach(x => x.classList.toggle('on', x === b));
      filter = b.dataset.f; apply('all');
    }));
    if (moreBtn) moreBtn.addEventListener('click', () => { expanded = true; apply(true); });
    apply(false);
  }

  if (!hasGsap) { $$('.fw').forEach(w => w.classList.add('on')); return; }
  const ifEl = (sel, fn) => { const el = $(sel); if (el) fn(el); };


  // Hero intro (homepage)
  const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
  tl.from('.nav-inner > *', { y: -20, opacity: 0, duration: 1, stagger: 0.06, clearProps: 'transform' }, 0.2);
  ifEl('.hero-frame', () => {
    tl.from('.hero-bg img', { scale: 1.15, duration: 2.4, ease: 'power3.out' }, 0)
      .from('.hero-pill', { y: 20, opacity: 0, duration: 1 }, 0.2)
      .from('.hero h1 .w > span', { yPercent: 110, duration: 1.2, stagger: 0.055 }, 0.3)
      .from('.hero-sub, .hero-buttons', { y: 24, opacity: 0, duration: 1.1, stagger: 0.1 }, 0.75)
      .from('.hc-card', { y: 220, opacity: 0, duration: 1.3, stagger: { each: 0.06, from: 'center' } }, 0.55);
  });
  // Subpage hero intro
  ifEl('.sub-frame', () => {
    tl.from('.sub-bg img', { scale: 1.12, duration: 2.2, ease: 'power3.out' }, 0);
    if ($('.sub-hero h1 .w > span')) tl.from('.sub-hero h1 .w > span', { yPercent: 110, duration: 1.2, stagger: 0.06 }, 0.25);
    tl.from($$('.sub-copy > :not(h1)'), { y: 24, opacity: 0, duration: 1.1, stagger: 0.08 }, 0.55);
    if ($('.fan-card')) tl.from('.fan-card', { y: 160, opacity: 0, rotate: 0, duration: 1.6, stagger: 0.12 }, 0.5);
    if ($('.svc-hcard')) tl.from('.svc-hcard', { y: 140, opacity: 0, duration: 1.6 }, 0.5);
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

  // Parallax, scroll progress and the hero ring drift are CSS scroll-driven animations (compositor, zero JS per frame)

  // Scroll progress of an element, computed only while it is on screen (no permanent scroll library loop).
  // p = 0 when the element's top reaches `a`·viewport, 1 when its bottom reaches `b`·viewport.
  const onProgress = (el, a, b, fn) => {
    let q = 0, on = false;
    const calc = () => { q = 0; const r = el.getBoundingClientRect(), vh = innerHeight;
      fn(Math.min(1, Math.max(0, (a * vh - r.top) / (r.height + (a - b) * vh)))); };
    const onScroll = () => { if (!q) q = requestAnimationFrame(calc); };
    new IntersectionObserver(en => { const v = en[0].isIntersecting; if (v === on) return; on = v;
      if (v) { window.addEventListener('scroll', onScroll, { passive: true }); calc(); } else window.removeEventListener('scroll', onScroll); }, { rootMargin: '20% 0px' }).observe(el);
  };

  // Fill words
  const fws = $$('.fw'), fillEl = $('.fill-text');
  if (fws.length && fillEl) onProgress(fillEl, 0.8, 0.45, p => { const n = Math.round(p * fws.length); if (n === fws._n) return; fws._n = n; fws.forEach((w, i) => w.classList.toggle('on', i < n)); });

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

  // Process: track fills as the steps scroll by
  ifEl('.p-steps', el => {
    const nodes = $$('.p-node'), line = $('.p-track .line i');
    if (line) onProgress(el, 0.8, 0.6, p => { line.style.transform = `scaleX(${p})`; nodes.forEach((n, i) => n.classList.toggle('on', p >= i / 2 - 0.01)); });
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

});
