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
  function closeMenu() { links.classList.remove('open'); toggle.classList.remove('open'); nav.classList.remove('menu-open'); }
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
  $$('.hero, .marquee, .strip, .reel, .geo, .showcase, .sub-hero, .process').forEach(el => offIO.observe(el));
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
    c.addEventListener('pointermove', e => { if (e.pointerType === 'mouse' || e.buttons) set(e.clientX); });
    c.addEventListener('pointerdown', e => set(e.clientX));
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
      pre[0].src = `img/ba/${k}-before.jpg`; pre[1].src = `img/ba/${k}-after.jpg`;
      ba.classList.add('swap');
      Promise.all(pre.map(im => im.decode().catch(() => {}))).then(() => setTimeout(() => {
        bImg.src = pre[0].src; aImg.src = pre[1].src;
        bImg.alt = `Původní web ${t.dataset.name} z roku ${t.dataset.year}`; aImg.alt = `Nový web ${t.dataset.name} od WebHunter`;
        lTag.textContent = `Předtím · ${t.dataset.year}`;
        ba.classList.remove('swap');
        if (hasGsap) { const o = { p: 88 }; gsap.to(o, { p: 50, duration: 1.2, ease: 'expo.inOut', onUpdate: () => ba.style.setProperty('--pos', o.p + '%') }); }
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

  // Form (demo)
  const form = $('.form');
  if (form) form.addEventListener('submit', e => { e.preventDefault(); form.classList.add('sent'); });

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
      const pre = new Image(); pre.src = `img/pf/${slug}-feat.jpg`;
      const swap = () => {
        desk.style.animation = 'none';
        desk.src = pre.src; mob.src = `img/pf/${slug}-m.jpg`;
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
      if (!tall.getAttribute('src')) { tall.src = tall.dataset.src; tall.onload = () => c._hover && go(); }
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
      .from('.hc-card', { y: 260, opacity: 0, duration: 1.6, stagger: { each: 0.08, from: 'center' } }, 0.6)
      .from('.hero-card', { y: 40, opacity: 0, duration: 1.2 }, 1.1)
      .from('.badge', { scale: 0, rotate: -90, duration: 1.2 }, 1.2);
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

  // Reveals
  gsap.utils.toArray('.reveal').forEach(el => {
    gsap.from(el, { y: 40, opacity: 0, duration: 1.1, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 88%' } });
  });
  gsap.utils.toArray('.reveal-group').forEach(g => {
    gsap.from(g.querySelectorAll('.reveal-item'), { y: 40, opacity: 0, duration: 1.1, stagger: 0.08, ease: 'expo.out', scrollTrigger: { trigger: g, start: 'top 85%' } });
  });
  ifEl('.bento', el => gsap.from('.b-card', { y: 70, opacity: 0, scale: 0.96, duration: 1.2, stagger: { each: 0.1, from: 'random' }, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 85%' } }));
  // cards have CSS transitions on transform — disable them while GSAP animates
  const rise = (targets, trigger, vars) => {
    gsap.set(targets, { transition: 'none' });
    gsap.from(targets, Object.assign({ y: 60, opacity: 0, duration: 1.2, ease: 'expo.out', clearProps: 'transition,transform,opacity',
      scrollTrigger: { trigger, start: 'top 85%' } }, vars));
  };
  ifEl('.wt-grid', el => rise(el.children, el, { stagger: 0.12 }));
  ifEl('.showcase', el => {
    gsap.from('.showcase .sc-stage', { y: 80, opacity: 0, duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 75%' } });
    gsap.from('.showcase .sc-item', { y: 30, opacity: 0, duration: 1, stagger: 0.06, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 75%' } });
  });
  ifEl('.sv-grid', el => rise(gsap.utils.toArray('.sv'), el, { stagger: 0.08 }));

  // Process: cards rise, track fills (no pin)
  ifEl('.p-steps', el => {
    gsap.from('.p-step', { y: 90, opacity: 0, duration: 1.3, stagger: 0.15, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 85%' } });
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
    gsap.to(o, { p: 50, duration: 1.8, ease: 'expo.inOut', scrollTrigger: { trigger: cmpS, start: 'top 75%' },
      onUpdate: () => cmpS.style.setProperty('--pos', o.p + '%') });
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
