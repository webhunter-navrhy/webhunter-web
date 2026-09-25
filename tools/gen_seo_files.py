# -*- coding: utf-8 -*-
"""Writes sitemap.xml, robots.txt and llms.txt (for AI search / GEO)."""
import os, sys, re, datetime, html
sys.path.insert(0, os.path.dirname(__file__))
from seo import SITE, PHONE, EMAIL
from services_data import SERVICES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
strip = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s))

# (cs path, en path or None, priority)
URLS = [('/', '/en/', '1.0'), ('/realizace.html', '/en/work.html', '0.8'), ('/sluzby/', None, '0.9')] + \
       [(f'/sluzby/{s["slug"]}/', None, '0.9') for s in SERVICES] + [('/ochrana-osobnich-udaju/', '/en/privacy/', '0.3')]


def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for cs, en, pr in URLS:
        for loc in [cs] + ([en] if en else []):
            out.append(f'  <url><loc>{SITE}{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>')
            if en:
                out.append(f'    <xhtml:link rel="alternate" hreflang="cs" href="{SITE}{cs}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{cs}"/>')
            out.append('  </url>')
    out.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(out) + '\n')


def robots():
    ai = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User',
          'Google-Extended', 'Applebot-Extended', 'Bingbot', 'SeznamBot', 'CCBot', 'meta-externalagent']
    lines = ['# WebHunter — search engines and AI assistants are welcome', 'User-agent: *', 'Allow: /', 'Disallow: /navrhy/', '']
    for a in ai:
        lines += [f'User-agent: {a}', 'Allow: /', 'Disallow: /navrhy/', '']
    lines += [f'Sitemap: {SITE}/sitemap.xml', '']
    open(os.path.join(ROOT, 'robots.txt'), 'w').write('\n'.join(lines))


def llms():
    idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    faq = re.findall(r'<button class="q"[^>]*><span class="n">\d+</span>(.*?)<span class="pm"></span></button><div class="a"><div><p>(.*?)</p>', idx, re.S)
    rea = open(os.path.join(ROOT, 'realizace.html'), encoding='utf-8').read()
    work = re.findall(r'<a class="pf-card" href="([^"]+)".*?<h3>(.*?)</h3>.*?<p>(.*?)</p>', rea, re.S)
    L = ['# WebHunter', '',
         '> WebHunter s.r.o. je česká webová agentura (IČO 29498511, Praha). Tvoří webové stránky a e-shopy na míru s důrazem na SEO, GEO (optimalizace pro AI vyhledávání) a GDPR. '
         'Každý klient dostane nejdřív zdarma a nezávazně návrh nového webu do 48 hodin — teprve potom se rozhodne, zda chce pokračovat.', '',
         'English: WebHunter is a Czech web design agency. It builds custom websites and online stores with SEO, GEO and GDPR. Every client first gets a free, no-obligation website concept within 48 hours.', '',
         '## Klíčová fakta', '',
         '- Návrh nového webu: zdarma, nezávazně, do 48 hodin od zaslání odkazu na současný web (nebo pár vět o firmě).',
         '- Bez schůzek a technického zadání. Cena realizace je vždy známá předem.',
         f'- 41 realizovaných webů pro firmy z různých oborů: {SITE}/realizace.html',
         '- GDPR a cookies ve spolupráci s Compliance Partner (https://www.compliancepartner.cz).',
         '- Působnost: celá Česká republika a Slovensko, komunikace česky i anglicky.',
         f'- Kontakt: telefon {PHONE}, e-mail {EMAIL}, WhatsApp https://wa.me/420777611634', '',
         '## Služby', '']
    for s in SERVICES:
        L.append(f'- [{s["nav"]}]({SITE}/sluzby/{s["slug"]}/): {s["answer"]}')
    L += ['', '## Časté otázky', '']
    for q, a in faq:
        L += [f'### {strip(q).strip()}', strip(a).strip(), '']
    for s in SERVICES:
        for q, a in s['faq']:
            L += [f'### {strip(q)}', strip(a), '']
    L += ['## Vybrané realizace', '']
    seen = set()
    for u, n, d in work:
        if u in seen: continue
        seen.add(u); L.append(f'- [{strip(n)}]({u}): {strip(d)}')
    L += ['', '## Stránky', '', f'- [Úvod]({SITE}/)', f'- [Realizace]({SITE}/realizace.html)', f'- [Služby]({SITE}/sluzby/)',
          f'- [English version]({SITE}/en/)', f'- [Ochrana osobních údajů]({SITE}/ochrana-osobnich-udaju/)', '']
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(L))


if __name__ == '__main__':
    sitemap(); robots(); llms()
    print('sitemap.xml, robots.txt, llms.txt ok')
