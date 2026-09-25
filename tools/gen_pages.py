# -*- coding: utf-8 -*-
"""Generates /sluzby/ and /sluzby/<slug>/ from tools/services_data.py.
Shared chrome (sprite, nav, footer, process, FAQ call card, contact form) is cut out of index.html / realizace.html,
so the subpages always match the rest of the site.   Run: python3 tools/gen_pages.py && sh tools/build.sh"""
import os, re, sys, html
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from services_data import SERVICES
from seo import SITE, ORG, ld, breadcrumb, faq_ld, head_extras

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
rea = open(os.path.join(ROOT, 'realizace.html'), encoding='utf-8').read()


def cut(s, a, b):
    i = s.index(a)
    return s[i:s.index(b, i) + len(b)]


FAVICON = cut(rea, '<link rel="icon"', '>')
FONTS = cut(rea, '<link rel="preload" as="font"', '</style>')
SPRITE = cut(rea, '<svg width="0" height="0"', '</svg>\n\n<nav')[:-len('\n\n<nav')]
NAV = cut(rea, '<nav class="nav"', '</nav>').replace(' class="current"', '')
FOOTER = cut(rea, '<footer>', '</footer>')
MCTA = cut(rea, '<a href="index.html#kontakt" class="m-cta"', '</a>')
PROCESS = cut(idx, '<!-- PROCESS -->', '</section>')
CONTACT = cut(idx, '<!-- CTA / CONTACT -->', '</section>')
BA = cut(idx, '<article class="sv wide observe sv-ba', '</article>')
CALLCARD = cut(idx, '<div class="call-card', '</a>\n          </div>\n        </div>')
FX = '<div class="bn-fx" aria-hidden="true"><span class="bn-pat"></span><span class="bn-orb o1"></span><span class="bn-orb o2"></span><span class="bn-shine"></span><i class="sp s1"></i><i class="sp s2"></i><i class="sp s3"></i>{}</div>'
SIZES = {f[:-5]: Image.open(os.path.join(ROOT, 'img/3d', f)).size for f in os.listdir(os.path.join(ROOT, 'img/3d')) if f.endswith('.webp') and not f.endswith('-s.webp')}


def pf_card(slug):
    for m in re.finditer(r'<a class="pf-card".*?</a>\n', rea, re.S):
        if f'img/pf/{slug}-480.webp' in m.group(0):
            return m.group(0)
    raise SystemExit('missing portfolio card ' + slug)


def obj(n, cls, sizes='(max-width: 767px) 90px, 130px', lazy=True):
    w, h = SIZES[n]
    return (f'<img class="bn-obj {cls}" src="img/3d/{n}-s.webp" srcset="img/3d/{n}-s.webp 240w, img/3d/{n}.webp {w}w" sizes="{sizes}" '
            f'alt="" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""} decoding="async">')


def relink(s, R):
    """Rewrite root-relative URLs for a page living under R ('../' or '../../')."""
    def fix(u):
        if re.match(r'(https?:|mailto:|tel:|#|data:|/)', u): return u
        if u == 'index.html': return R
        if u.startswith('index.html#'): return R + u[len('index.html'):]
        return R + u
    s = re.sub(r'(\s(?:href|src|data-src))="([^"]*)"', lambda m: f'{m.group(1)}="{fix(m.group(2))}"', s)
    s = re.sub(r'(\s(?:srcset|imagesrcset))="([^"]*)"',
               lambda m: m.group(1) + '="' + ', '.join(fix(p.split()[0]) + ' ' + p.split()[1] for p in m.group(2).split(',')) + '"', s)
    s = re.sub(r"url\((assets/[^)]+)\)", lambda m: f'url({R}{m.group(1)})', s)
    return s


def page(R, path, title, desc, lds, body, body_cls='page-sub page-svc', og_type='website', extra_head=''):
    nav = NAV.replace('<a href="index.html#sluzby">Co dostanete</a>', '<a href="sluzby/">Služby</a><a href="blog/">Blog</a>').replace('<a href="index.html#tym">Tým</a>', '').replace('href="en/work.html" class="lang-sw"', 'href="en/" class="lang-sw"')
    out = f'''<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{head_extras(path, title, desc, og_type=og_type)}{extra_head}
{FAVICON}

{FONTS}

<script src="assets/vendor/gsap.min.js" defer></script>

<link rel="preload" as="image" href="img/hero-sky-1400.webp" imagesrcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" imagesizes="100vw" fetchpriority="high">
<link rel="stylesheet" href="assets/site.min.css?v=1">
{chr(10).join(ld(x) for x in lds)}
</head>
<body class="{body_cls}">

<div class="scroll-progress"></div>
{SPRITE}

{nav}

<main>
{body}
</main>

{FOOTER}

{MCTA}
<script src="assets/site.min.js?v=1" defer></script>
</body>
</html>
'''
    dest = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(relink(out, R))


def words(h1):
    """wrap every word in .w > span for the intro animation (serif spans become em.serif)"""
    out = []
    for serif, plain in re.findall(r'<span class="serif">(.*?)</span>|([^<]+)', h1):
        for w in (serif or plain).split():
            out.append(f'<span class="w"><span><em class="serif">{w}</em></span></span>' if serif else f'<span class="w"><span>{w}</span></span>')
    return ' '.join(out)


def hero(label, h1, lead, crumbs, card_obj, card_variant='bnv-lime'):
    h1 = words(h1)
    cr = ' <span>/</span> '.join(f'<a href="{u}">{E(n)}</a>' if u else E(n) for n, u in crumbs)
    return f'''<section class="sub-hero svc-hero" id="top">
  <div class="sub-frame">
    <div class="sub-bg"><img decoding="async" class="sky-par" src="img/hero-sky-1400.webp" srcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" sizes="100vw" alt="" fetchpriority="high"></div>
    <div class="sub-copy">
      <div class="crumbs mono">{cr}</div>
      <span class="svc-kicker mono">{E(label)}</span>
      <h1>{h1}</h1>
      <p>{lead}</p>
      <form class="hero-url svc-url" data-hero-url novalidate>
        <label class="hu-field"><svg aria-hidden="true"><use href="#i-link"/></svg><span class="sr-only">Odkaz na váš současný web</span><input id="hero-web" name="hero-web" type="text" inputmode="url" autocomplete="url" placeholder="vasefirma.cz" spellcheck="false"></label>
        <button type="submit" class="btn btn--lime">Chci návrh zdarma <span class="arr"><svg><use href="#i-arrow"/></svg></span></button>
      </form>
      <div class="svc-alt"><a href="#kontakt" data-no-web>Nemám web</a><span aria-hidden="true">·</span><a href="https://wa.me/420777611634" data-wa><svg aria-hidden="true"><use href="#i-wa"/></svg>Napsat na WhatsApp</a></div>
    </div>
    <div class="svc-hcard bnx {card_variant}" aria-hidden="true">{FX.format(obj(card_obj, 'float-a svc-hobj', '(max-width: 767px) 150px, 260px', lazy=False))}
      <span class="bn-chip dark">Návrh zdarma</span>
      <div class="svc-hstats">
        <div><b>48 h</b><span>návrh webu</span></div>
        <div><b>0 Kč</b><span>za návrh</span></div>
        <div><b>41</b><span>realizací</span></div>
      </div>
    </div>
  </div>
</section>'''


def contact(landing):
    return CONTACT.replace('<form class="form reveal" novalidate>', f'<form class="form reveal" novalidate data-landing="{E(landing)}">')


def service_page(s):
    path = f'/sluzby/{s["slug"]}/'
    lds = [ORG,
           breadcrumb([('Úvod', '/'), ('Služby', '/sluzby/'), (s['nav'], path)]),
           {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + '#service', "name": s['nav'], "serviceType": s['label'],
            "description": s['desc'], "url": SITE + path, "provider": {"@id": SITE + '/#org'},
            "areaServed": [{"@type": "Country", "name": "Česká republika"}, {"@type": "Country", "name": "Slovensko"}],
            "offers": {"@type": "Offer", "name": "Návrh nového webu zdarma do 48 hodin", "price": "0", "priceCurrency": "CZK",
                       "description": "Nezávazný návrh zdarma. Za realizaci platíte, jen pokud se pro ni sami rozhodnete."}},
           faq_ld(s['faq'])]
    ben = ''.join(
        f'<div class="val bnx {v} reveal-item tilt">{FX.format(obj(o, "float-a ob-val"))}<span class="n-chip">0{i + 1}</span><b>{E(t)}</b><p>{E(d)}</p></div>'
        for i, (v, o, t, d) in enumerate(s['benefits']))
    blocks = ''
    for n, (h2, parts) in enumerate(s['sections']):
        body = ''
        for p in parts:
            if isinstance(p, str):
                body += f'<p>{p}</p>'
            else:
                body += '<ul class="svc-list">' + ''.join(f'<li><i><svg><use href="#i-check"/></svg></i>{E(x)}</li>' for x in p) + '</ul>'
        blocks += f'<article class="svc-block reveal"><span class="svc-no mono">0{n + 1}</span><div><h2>{E(h2)}</h2>{body}</div></article>'
    others = [o for o in SERVICES if o['slug'] != s['slug']]
    mv = ['bnv-sky', 'bnv-blue', 'bnv-lime', 'bnv-dark', 'bnv-sky']
    more = ''.join(
        f'<a class="svc-mini bnx {mv[i]} reveal-item" href="sluzby/{o["slug"]}/">{FX.format(obj(o["obj"], "float-a svc-mini-obj", "90px"))}'
        f'<span class="mono">{E(o["label"])}</span><b>{E(o["nav"])}</b><span class="svc-go"><svg><use href="#i-arrow"/></svg></span></a>'
        for i, o in enumerate(others))
    faq = ''.join(
        f'<div class="qa{" open" if i == 0 else ""} reveal-item"><button class="q" aria-expanded="{"true" if i == 0 else "false"}"><span class="n">0{i + 1}</span>{E(q)}<span class="pm"></span></button><div class="a"><div><p>{a}</p></div></div></div>'
        for i, (q, a) in enumerate(s['faq']))
    ba = ''
    if s.get('ba'):
        ba = f'''<section class="svc-ba-sec">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">Předtím a teď</span><h2 class="reveal">Skutečné weby našich klientů. <span class="serif">Posuňte jezdcem.</span></h2></div>
    <div class="sv-grid svc-ba-grid">{BA}</div>
  </div>
</section>'''
    body = f'''{hero(s["label"], s["h1"], s["lead"], [('Úvod', 'index.html'), ('Služby', 'sluzby/'), (s['nav'], None)], s['obj'])}

<section class="svc-intro">
  <div class="container">
    <div class="svc-answer reveal"><span class="label">Ve zkratce</span><p>{E(s["answer"])}</p></div>
    <div class="vals svc-vals reveal-group">{ben}</div>
  </div>
</section>
{ba}
<section class="svc-content">
  <div class="container svc-blocks">{blocks}</div>
</section>

{PROCESS}

<section class="svc-work">
  <div class="container">
    <div class="arch-head"><h2 class="reveal">Weby, které jsme <span class="serif">postavili.</span></h2><a href="realizace.html" class="btn btn--dark reveal">Všech 41 realizací <span class="arr"><svg><use href="#i-arrow"/></svg></span></a></div>
    <div class="pf-grid svc-pf">{''.join(pf_card(x) for x in s['work'])}</div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="faq-panel">
    <div class="faq-deco" aria-hidden="true">?</div>
    <div class="container faq-grid">
      <div class="faq-side">
        <span class="label reveal">Časté otázky</span>
        <h2 class="reveal">{E(s["label"])}: <span class="serif">na co se ptáte.</span></h2>
        <p class="reveal">Nenašli jste odpověď? Zavolejte nebo napište, odpovídáme lidsky a rychle.</p>
        {CALLCARD}
      </div>
      <div class="faq-list reveal-group">{faq}</div>
    </div>
  </div>
</section>

<section class="svc-more-sec">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">Další služby</span><h2 class="reveal">Všechno pro web <span class="serif">pod jednou střechou.</span></h2></div>
    <div class="svc-more reveal-group">{more}</div>
  </div>
</section>

{contact(s["nav"])}'''
    page('../../', path, s['title'], s['desc'], lds, body)


def services_index():
    path = '/sluzby/'
    title = 'Služby — tvorba webů, e-shopů, SEO, GEO a GDPR | WebHunter'
    desc = 'Tvorba webových stránek na míru, redesign, e-shopy, SEO, GEO optimalizace pro AI vyhledávání a GDPR. Návrh nového webu zdarma do 48 hodin.'
    lds = [ORG, breadcrumb([('Úvod', '/'), ('Služby', path)]),
           {"@context": "https://schema.org", "@type": "ItemList", "name": "Služby WebHunter",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + f'/sluzby/{s["slug"]}/', "name": s['nav']} for i, s in enumerate(SERVICES)]}]
    variants = ['bnv-blue', 'bnv-sky', 'bnv-lime', 'bnv-dark', 'bnv-sky', 'bnv-blue']
    cards = ''.join(
        f'<a class="svc-card bnx {variants[i]} reveal-item tilt" href="sluzby/{s["slug"]}/">{FX.format(obj(s["obj"], "float-a svc-card-obj", "(max-width: 767px) 110px, 170px"))}'
        f'<span class="n-chip">0{i + 1}</span><div class="svc-card-txt"><span class="mono">{E(s["label"])}</span><h2>{E(s["nav"])}</h2><p>{E(s["lead"].split(". ")[0].rstrip("."))}.</p></div>'
        f'<span class="svc-go-row">Více o službě <span class="svc-go"><svg><use href="#i-arrow"/></svg></span></span></a>'
        for i, s in enumerate(SERVICES))
    body = f'''{hero('Služby', 'Všechno pro web, který <span class="serif">přivádí zákazníky.</span>',
                  'Design, texty, technologie, SEO, AI vyhledávání i GDPR pod jednou střechou. A na začátku vždy návrh zdarma do 48 hodin.',
                  [('Úvod', 'index.html'), ('Služby', None)], 'spark', 'bnv-sky')}

<section class="svc-index">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">Co pro vás uděláme</span><h2 class="reveal">Šest služeb. <span class="serif">Jeden partner.</span></h2></div>
    <div class="svc-cards reveal-group">{cards}</div>
  </div>
</section>

{PROCESS}

{contact('Služby')}'''
    page('../', path, title, desc, lds, body)


if __name__ == '__main__':
    for s in SERVICES:
        service_page(s)
    services_index()
    print('generated', len(SERVICES) + 1, 'pages')
