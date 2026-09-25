# -*- coding: utf-8 -*-
"""1) Normalises the SEO <head> (canonical to webhunter.cz, hreflang, OG, JSON-LD) and the CZ/EN switch on the Czech pages.
2) Generates the English pages /en/, /en/work.html, /en/privacy/ from them using tools/i18n_en.py.
Run before gen_pages.py (build.sh does both)."""
import os, re, sys, html, json, copy
sys.path.insert(0, os.path.dirname(__file__))
from seo import SITE, ORG, WEBSITE, ld, breadcrumb, faq_ld, head_extras
from i18n_en import T, BLOCKS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
ALT = {  # production paths cs <-> en
    'home': {'cs': '/', 'en': '/en/'},
    'work': {'cs': '/realizace.html', 'en': '/en/work.html'},
    'privacy': {'cs': '/ochrana-osobnich-udaju/', 'en': '/en/privacy/'},
}
META = {
    ('home', 'cs'): ('WebHunter — Tvorba webů na míru, návrh zdarma do 48 hodin',
                     'Zdarma vám navrhneme nový web do 48 hodin. Potom se sami rozhodnete, zda budete chtít pokračovat. Tvorba webových stránek a e-shopů na míru s SEO, GEO a GDPR.', 'img/og.jpg'),
    ('work', 'cs'): ('Realizace — 41 webů na míru | WebHunter',
                     '41 webů, které jsme navrhli a postavili: videomakeři, fotografové, sportovní akce, farmy, e-shopy, řemeslníci i reality. Prohlédněte si portfolio WebHunter.', 'img/og-realizace.jpg'),
    ('privacy', 'cs'): ('Ochrana osobních údajů a cookies | WebHunter', 'Jak WebHunter s.r.o. zpracovává osobní údaje, jaké používá cookies a jaká máte práva.', 'img/og.jpg'),
    ('home', 'en'): ('WebHunter — Custom Website Design, Free Concept in 48 Hours',
                     'We design your new website for free within 48 hours. Then you decide whether to continue. Custom websites and online stores with SEO, GEO and GDPR from a Czech web agency.', 'img/og.jpg'),
    ('work', 'en'): ('Our Work — 41 Custom Websites | WebHunter',
                     '41 websites we designed and built for videomakers, photographers, sports events, farms, online stores, trades and real estate. Browse the WebHunter portfolio.', 'img/og-realizace.jpg'),
    ('privacy', 'en'): ('Privacy Policy & Cookies | WebHunter', 'How WebHunter s.r.o. processes personal data, which cookies it uses and what rights you have.', 'img/og.jpg'),
}
SEO_LINE = re.compile(r'^<(?:link rel="(?:canonical|alternate)"|meta property="og:|meta name="(?:twitter:|theme-color|description|robots|format-detection))[^\n]*\n', re.M)
LD_RE = re.compile(r'<script type="application/ld\+json">.*?</script>\n?', re.S)


def org(lang):
    o = copy.deepcopy(ORG)
    if lang == 'en':
        o['description'] = 'Czech web design agency. We build custom websites and online stores with a focus on SEO, GEO (AI search) and GDPR. A free, no-obligation website concept within 48 hours.'
        o['slogan'] = 'We design your new website for free within 48 hours. Then you decide whether to continue.'
        o.pop('hasOfferCatalog', None)
        o['knowsAbout'] = ['Website design', 'Online store development', 'Website redesign', 'SEO', 'GEO – generative engine optimisation', 'GDPR and cookies', 'Copywriting', 'Conversion optimisation']
    return o


def faq_pairs(s):
    return [(re.sub(r'<span class="n">\d+</span>|<span class="pm"></span>', '', q).strip(), a) for q, a in
            re.findall(r'<button class="q"[^>]*>(.*?)</button><div class="a"><div><p>(.*?)</p>', s, re.S)]


def ld_for(key, lang, s):
    base = '/en/' if lang == 'en' else '/'
    home = 'Home' if lang == 'en' else 'Úvod'
    web = copy.deepcopy(WEBSITE)
    if lang == 'en':
        web['inLanguage'] = 'en'; web['@id'] = SITE + '/en/#website'; web['url'] = SITE + '/en/'
    out = [org(lang)]
    if key == 'home':
        out += [web, faq_ld(faq_pairs(s))]
    elif key == 'work':
        items = re.findall(r'<a class="pf-card" href="([^"]+)".*?<h3>(.*?)</h3>', s, re.S)
        out += [breadcrumb([(home, base), ('Our work' if lang == 'en' else 'Realizace', ALT['work'][lang])]),
                {"@context": "https://schema.org", "@type": "CollectionPage", "name": META[(key, lang)][0], "url": SITE + ALT['work'][lang],
                 "about": {"@id": SITE + '/#org'}, "mainEntity": {"@type": "ItemList", "numberOfItems": len(items),
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "WebSite", "name": html.unescape(n), "url": u, "creator": {"@id": SITE + '/#org'}}} for i, (u, n) in enumerate(items)]}}]
    else:
        out += [breadcrumb([(home, base), (META[(key, lang)][0].split(' |')[0], ALT['privacy'][lang])])]
    return out


def set_head(s, key, lang):
    title, desc, og = META[(key, lang)]
    s = SEO_LINE.sub('', s)
    s = LD_RE.sub('', s)
    s = re.sub(r'<title>.*?</title>\n', lambda m: f'<title>{E(title)}</title>\n<meta name="description" content="{E(desc)}">\n{head_extras(ALT[key][lang], title, desc, og_img=og, lang=lang, alt=ALT[key])}\n', s, count=1)
    s = s.replace('</head>', '\n'.join(ld(x) for x in ld_for(key, lang, s)) + '\n</head>', 1)
    s = re.sub(r'<html lang="[a-z]+">', f'<html lang="{lang}">', s, count=1)
    return s


def lang_switch(s, href, lang):
    """wrap the nav CTA with a CZ/EN switch (idempotent)"""
    label, hl, aria = ('EN', 'en', 'EN – English version') if lang == 'cs' else ('CZ', 'cs', 'CZ – Česká verze')
    sw = f'<a href="{href}" class="lang-sw" hreflang="{hl}" lang="{hl}" aria-label="{aria}">{label}</a>'
    if 'class="nav-end"' in s:
        return re.sub(r'<a href="[^"]*" class="lang-sw"[^>]*>[A-Z]{2}</a>', sw, s, count=1)
    return re.sub(r'(<nav class="nav".*?)(<a href="[^"]*#kontakt" class="btn btn--lime">.*?</a>)', lambda m: f'{m.group(1)}<div class="nav-end">{sw}{m.group(2)}</div>', s, count=1, flags=re.S)


# ---------- translation ----------
def norm(t):
    return re.sub(r'\s+', ' ', html.unescape(t).replace('\xa0', ' ')).strip()


MISSING = set()
CZ = re.compile(r'[áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]')
KEEP = {'Hasoběh', 'Farma Tájek', 'Beka Bazar', 'Držíme ti palce', 'Nájem s radostí', 'Alissa Beauté', 'Obrazy z nitra', 'Jiří Kubišta', 'Ondřej Hucek',
        'Bydlení Týniště', 'Anna Krčmová', 'Nonstop Zámky', 'Pošta Trojka', 'Bystřice s vizí', 'Portál Výsluní', 'Reality Nekvinda', '‹ ›'}


def tr_text(t):
    k = norm(t)
    if not k:
        return t
    if k in T:
        lead, trail = re.match(r'^\s*', t).group(0), re.search(r'\s*$', t).group(0)
        return lead + E(T[k], quote=False) + trail
    if CZ.search(k) and k not in KEEP:
        MISSING.add(k)
    return t


def tr_attr(m):
    name, v = m.group(1), m.group(2)
    k = norm(v)
    if k in T:
        return f' {name}="{E(T[k])}"'
    mm = re.match(r'^Web (.+?) — (\S+)$', k)
    if mm:
        return f' {name}="{E(mm.group(1))} website — {mm.group(2)}"'
    if CZ.search(k) and k not in KEEP and name != 'data-name':
        MISSING.add('@' + k)
    return m.group(0)


def translate(s):
    for a, b in BLOCKS:
        s = s.replace(a, b)
    head, body = s.split('<body', 1)
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<svg width="0".*?</svg>)', body, flags=re.S)
    for i in range(0, len(parts), 2):
        p = re.sub(r'>([^<>]+)<', lambda m: '>' + tr_text(m.group(1)) + '<', parts[i])
        parts[i] = re.sub(r'\s(alt|placeholder|aria-label|title|data-name|data-t|data-d)="([^"]*)"', tr_attr, p)
    return head + '<body' + ''.join(parts)


def relink_en(s, depth):
    """Czech root-relative links -> links valid from /en/ (depth 1) or /en/privacy/ (depth 2)"""
    up = '../' * depth
    here = {'home': '' if depth == 1 else '../', 'work': 'work.html' if depth == 1 else '../work.html', 'privacy': 'privacy/' if depth == 1 else './'}

    def fix(u):
        if re.match(r'(https?:|mailto:|tel:|#|data:|/)', u): return u
        pre = '../' if u.startswith('../') and depth == 2 else ''
        v = u[3:] if pre else u  # the privacy source page already uses ../
        if v in ('', 'index.html', './'): return here['home'] or './'
        if v.startswith('index.html#') or (pre and v.startswith('#')): return (here['home'] or './') + v[v.index('#'):]
        if v.startswith('realizace.html'): return here['work'] + v[len('realizace.html'):]
        if v.startswith('ochrana-osobnich-udaju/'): return here['privacy']
        return up + v
    s = re.sub(r'(\s(?:href|src|data-src))="([^"]*)"', lambda m: f'{m.group(1)}="{fix(m.group(2))}"', s)
    s = re.sub(r'(\s(?:srcset|imagesrcset))="([^"]*)"', lambda m: m.group(1) + '="' + ', '.join(fix(p.split()[0]) + ' ' + p.split()[1] for p in m.group(2).split(',')) + '"', s)
    s = re.sub(r"url\((?:\.\./)?(assets/[^)]+)\)", lambda m: f'url({up}{m.group(1)})', s)
    return s


def drop_services_col(s):
    s = re.sub(r'\s*<div class="foot-col">\s*<h4>Služby</h4>.*?</div>', '', s, count=1, flags=re.S)
    return s.replace('<div class="foot-top">', '<div class="foot-top ft4">', 1)


PAGES = [  # key, czech source, english dest, depth of the source (0 = root, 1 = /ochrana-osobnich-udaju/), en depth
    ('home', 'index.html', 'en/index.html', 1),
    ('work', 'realizace.html', 'en/work.html', 1),
    ('privacy', 'ochrana-osobnich-udaju/index.html', 'en/privacy/index.html', 2),
]

if __name__ == '__main__':
    for key, src, dst, depth in PAGES:
        p = os.path.join(ROOT, src)
        s = open(p, encoding='utf-8').read()
        cz_up = '../' if src.count('/') else ''
        s = set_head(s, key, 'cs')
        s = lang_switch(s, cz_up + ALT[key]['en'].lstrip('/'), 'cs')
        open(p, 'w', encoding='utf-8').write(s)
        # english
        e = drop_services_col(s)
        e = re.sub(r'\s*<span class="qa-more">.*?</span>', '', e)  # links to Czech-only service pages
        e = translate(e)
        e = set_head(e, key, 'en')
        e = relink_en(e, depth)
        back = ('../' * depth) + ALT[key]['cs'].lstrip('/')
        e = lang_switch(e, back if back else '../', 'en')
        e = e.replace('<form class="form reveal" novalidate>', '<form class="form reveal" novalidate data-landing="EN – free website concept in 48 h">')
        d = os.path.join(ROOT, dst)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        open(d, 'w', encoding='utf-8').write(e)
    if MISSING:
        print('UNTRANSLATED (%d):' % len(MISSING))
        for m in sorted(MISSING): print('  ', m)
    print('en pages ok')
