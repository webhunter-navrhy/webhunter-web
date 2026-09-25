# -*- coding: utf-8 -*-
"""Generates /blog/ and /blog/<slug>/ from tools/blog_data.py (layout pieces shared with gen_pages.py).
Run: python3 tools/gen_blog.py   (sh tools/build.sh runs it)"""
import os, re, sys, html, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from gen_pages import FX, obj, page, words, contact, CALLCARD
from blog_data import ARTICLES, CATS, DATE
from services_data import SERVICES
from seo import SITE, ORG, breadcrumb, faq_ld

E = html.escape
SVC = {s['slug']: s for s in SERVICES}
BY = {a['slug']: a for a in ARTICLES}
SKY = '<div class="sub-bg"><img decoding="async" class="sky-par" src="img/hero-sky-1400.webp" srcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" sizes="100vw" alt="" fetchpriority="high"></div>'
ARROW = '<span class="svc-go"><svg><use href="#i-arrow"/></svg></span>'


def cz_date(d):
    y, m, dd = d.split('-')
    return f'{int(dd)}. {int(m)}. {y}'


def slugify(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
    return ('k-' + t) if t[:1].isdigit() else t


def strip(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def render_body(blocks):
    out, toc = [], []
    for b in blocks:
        k = b[0]
        if k == 'h2':
            i = slugify(b[1]); toc.append((i, b[1])); out.append(f'<h2 id="{i}">{E(b[1])}</h2>')
        elif k == 'h3': out.append(f'<h3>{E(b[1])}</h3>')
        elif k == 'p': out.append(f'<p>{b[1]}</p>')
        elif k == 'ul': out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ul>')
        elif k == 'ol': out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ol>')
        elif k == 'check': out.append('<ul class="svc-list post-check">' + ''.join(f'<li><i><svg><use href="#i-check"/></svg></i><span>{x}</span></li>' for x in b[1]) + '</ul>')
        elif k == 'tip': out.append(f'<div class="post-tip"><span class="post-tip-ico"><svg><use href="#i-spark-f"/></svg></span><div><b>{E(b[1])}</b><p>{b[2]}</p></div></div>')
        elif k == 'table':
            head = ''.join(f'<th scope="col">{E(h)}</th>' for h in b[1])
            rows = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in b[2])
            out.append(f'<div class="post-table"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif k == 'cta':
            out.append(f'''<div class="post-cta bnx bnv-dark">{FX.format(obj('stopwatch', 'float-a post-cta-obj', '(max-width: 767px) 90px, 140px'))}
        <span class="bn-chip">Návrh zdarma · do 48 hodin</span>
        <b>Chcete vidět, jak by mohl vypadat váš nový web?</b>
        <p>Pošlete nám odkaz na současný web. Do 48 hodin máte konkrétní návrh a potom se sami rozhodnete, zda pokračovat.</p>
        <a href="#kontakt" class="btn btn--lime">Chci návrh zdarma <span class="arr"><svg><use href="#i-arrow"/></svg></span></a></div>''')
    return '\n      '.join(out), toc


def card(a, cls='post-card', h='h3'):
    return f'''<a class="{cls} bnx {a['variant']} reveal-item tilt" href="blog/{a['slug']}/">{FX.format(obj(a['obj'], 'float-a post-card-obj', '(max-width: 767px) 100px, 150px'))}
      <span class="post-card-top"><span class="post-chip">{E(CATS[a['cat']])}</span><span class="mono">{a['read']} min čtení</span></span>
      <div class="post-card-txt"><{h}>{E(strip(a['h1']))}</{h}><span class="post-card-desc">{E(a['desc'].split('. ')[0].rstrip('.'))}.</span></div>
      <span class="svc-go-row">Číst článek {ARROW}</span></a>'''


def article(a):
    path = f'/blog/{a["slug"]}/'
    body, toc = render_body(a['body'])
    words_n = len(strip(' '.join(str(x) for b in a['body'] for x in b[1:])).split())
    lds = [ORG,
           breadcrumb([('Úvod', '/'), ('Blog', '/blog/'), (strip(a['h1']), path)]),
           {"@context": "https://schema.org", "@type": "BlogPosting", "@id": SITE + path + '#article', "headline": a['title'], "description": a['desc'],
            "datePublished": DATE, "dateModified": DATE, "inLanguage": "cs-CZ", "articleSection": CATS[a['cat']], "wordCount": words_n,
            "image": SITE + f'/img/og/blog-{a["slug"]}.jpg', "mainEntityOfPage": SITE + path, "url": SITE + path,
            "author": {"@type": "Organization", "@id": SITE + '/#org', "name": "WebHunter"}, "publisher": {"@id": SITE + '/#org'},
            "abstract": a['answer']},
           faq_ld(a['faq'])]
    toc_html = ''.join(f'<a href="#{i}">{E(t)}</a>' for i, t in toc)
    faq = ''.join(
        f'<div class="qa{" open" if i == 0 else ""} reveal-item"><button class="q" aria-expanded="{"true" if i == 0 else "false"}"><span class="n">0{i + 1}</span>{E(q)}<span class="pm"></span></button><div class="a"><div><p>{E(ans)}</p></div></div></div>'
        for i, (q, ans) in enumerate(a['faq']))
    rel = [x for x in ARTICLES if x['slug'] != a['slug'] and x['cat'] == a['cat']] + [x for x in ARTICLES if x['slug'] != a['slug'] and x['cat'] != a['cat']]
    svc = ''.join(f'<a class="post-svc" href="sluzby/{s}/"><span class="mono">Služba</span><b>{E(SVC[s]["nav"])}</b>{ARROW}</a>' for s in a['services'])
    take = ''.join(f'<li><i><svg><use href="#i-check"/></svg></i>{E(t)}</li>' for t in a['takeaways'])
    body_html = f'''<section class="sub-hero svc-hero post-hero" id="top">
  <div class="sub-frame">
    {SKY}
    <div class="sub-copy">
      <div class="crumbs mono"><a href="index.html">Úvod</a> <span>/</span> <a href="blog/">Blog</a> <span>/</span> {E(CATS[a['cat']])}</div>
      <div class="post-meta mono"><span class="post-chip">{E(CATS[a['cat']])}</span><span>{a['read']} min čtení</span><time datetime="{DATE}">{cz_date(DATE)}</time></div>
      <h1>{words(a['h1'])}</h1>
      <p>{E(a['lead'])}</p>
    </div>
    <div class="svc-hcard post-hcard bnx {a['variant']}">{FX.format(obj(a['obj'], 'float-a svc-hobj', '(max-width: 767px) 120px, 220px', lazy=False))}
      <span class="bn-chip dark">Ve zkratce</span>
      <ul class="post-take">{take}</ul>
    </div>
  </div>
</section>

<section class="post-wrap">
  <div class="container post-grid">
    <nav class="post-toc" aria-label="Obsah článku"><span class="mono">Obsah článku</span>{toc_html}<a class="post-toc-cta" href="#kontakt">Návrh webu zdarma <span class="arr"><svg><use href="#i-arrow"/></svg></span></a></nav>
    <article class="post-body">
      <div class="post-answer"><span class="label">Odpověď ve zkratce</span><p>{E(a['answer'])}</p></div>
      {body}
      <div class="post-svcs"><span class="mono">Související služby</span>{svc}</div>
      <p class="post-by mono">Napsal tým WebHunter · <time datetime="{DATE}">{cz_date(DATE)}</time></p>
    </article>
  </div>
</section>

<section class="faq" id="faq">
  <div class="faq-panel">
    <div class="faq-deco" aria-hidden="true">?</div>
    <div class="container faq-grid">
      <div class="faq-side">
        <span class="label reveal">Časté otázky</span>
        <h2 class="reveal">Na co se <span class="serif">ptáte nejčastěji.</span></h2>
        <p class="reveal">Nenašli jste odpověď? Zavolejte nebo napište, odpovídáme lidsky a rychle.</p>
        {CALLCARD}
      </div>
      <div class="faq-list reveal-group">{faq}</div>
    </div>
  </div>
</section>

<section class="svc-more-sec post-related">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">Další články</span><h2 class="reveal">Čtěte <span class="serif">dál.</span></h2></div>
    <div class="post-cards post-cards-3 reveal-group">{''.join(card(x) for x in rel[:3])}</div>
  </div>
</section>

{contact('Blog: ' + a['title'])}'''
    page('../../', path, a['title'], a['desc'], lds, body_html, body_cls='page-sub page-svc page-post', og_type='article',
         extra_head=f'\n<meta property="article:published_time" content="{DATE}">\n<meta property="article:section" content="{E(CATS[a["cat"]])}">', og_img=f'img/og/blog-{a["slug"]}.jpg')


def index():
    path = '/blog/'
    title = 'Blog — rady k webům, SEO, AI vyhledávání a GDPR | WebHunter'
    desc = 'Praktické rady k tvorbě webových stránek: kolik stojí web, redesign bez ztráty pozic, GEO pro ChatGPT a AI vyhledávání, cookie lišta a GDPR, texty, které prodávají.'
    feat, rest = ARTICLES[0], ARTICLES[1:]
    lds = [ORG, breadcrumb([('Úvod', '/'), ('Blog', path)]),
           {"@context": "https://schema.org", "@type": "Blog", "@id": SITE + path + '#blog', "name": "Blog WebHunter", "url": SITE + path, "inLanguage": "cs-CZ", "publisher": {"@id": SITE + '/#org'},
            "blogPost": [{"@type": "BlogPosting", "headline": x['title'], "url": SITE + f'/blog/{x["slug"]}/', "datePublished": DATE, "description": x['desc']} for x in ARTICLES]}]
    body_html = f'''<section class="sub-hero svc-hero blog-hero" id="top">
  <div class="sub-frame">
    {SKY}
    <div class="sub-copy">
      <div class="crumbs mono"><a href="index.html">Úvod</a> <span>/</span> Blog</div>
      <span class="svc-kicker mono">Blog</span>
      <h1>{words('Rady, které vám <span class="serif">přivedou zákazníky.</span>')}</h1>
      <p>Kolik stojí web, jak na redesign bez ztráty pozic, jak se dostat do odpovědí ChatGPT a co musí splňovat cookie lišta. Srozumitelně a bez žargonu.</p>
    </div>
    {card(feat, 'post-feat', 'h2').replace('reveal-item ', '')}
  </div>
</section>

<section class="blog-list">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">Všechny články</span><h2 class="reveal">Web, SEO a AI <span class="serif">bez žargonu.</span></h2></div>
    <div class="post-cards reveal-group">{''.join(card(x) for x in rest)}</div>
  </div>
</section>

{contact('Blog')}'''
    page('../', path, title, desc, lds, body_html, body_cls='page-sub page-svc page-blog', og_img='img/og/blog.jpg')


if __name__ == '__main__':
    for a in ARTICLES:
        article(a)
    index()
    print('blog:', len(ARTICLES), 'articles')
