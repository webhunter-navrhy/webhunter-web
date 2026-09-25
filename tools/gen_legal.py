# -*- coding: utf-8 -*-
"""Generates /obchodni-podminky/ from tools/vop_cs.md, using the privacy page as the layout template.
Edit the text in vop_cs.md (plain Markdown), then run sh tools/build.sh."""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from seo import SITE, ORG, ld, breadcrumb, head_extras
from gen_en import SEO_LINE, LD_RE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EFFECTIVE = '25. 9. 2026'
TITLE = 'Obchodní podmínky | WebHunter'
DESC = 'Všeobecné obchodní podmínky společnosti WebHunter s.r.o. pro tvorbu webů, e-shopů, SEO, GEO, správu webů a hosting.'
PATH = '/obchodni-podminky/'


def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)


def md_to_html(md):
    out, toc, ul = [], [], False
    for line in md.splitlines():
        s = line.strip()
        if s.startswith('* '):
            if not ul: out.append('<ul>'); ul = True
            out.append(f'<li>{inline(s[2:])}</li>'); continue
        if ul: out.append('</ul>'); ul = False
        if not s or s == '---' or s.startswith('# '):
            continue
        if s.startswith('## '):
            t = s[3:]; n = t.split('.')[0]
            toc.append((f'cl{n}', t)); out.append(f'<h2 id="cl{n}">{inline(t)}</h2>')
        elif s.startswith('### '):
            m = re.match(r'(\d+\.\d+)\s+(.*)', s[4:])
            out.append(f'<h3><span class="cl-n">{m.group(1)}</span> {inline(m.group(2))}</h3>' if m else f'<h3>{inline(s[4:])}</h3>')
        else:
            m = re.match(r'(\d+\.\d+)\s+(.*)', s)
            out.append(f'<p><span class="cl-n">{m.group(1)}</span> {inline(m.group(2))}</p>' if m else f'<p>{inline(s)}</p>')
    if ul: out.append('</ul>')
    return '\n      '.join(out), toc


def main():
    tpl = open(os.path.join(ROOT, 'ochrana-osobnich-udaju/index.html'), encoding='utf-8').read()
    body, toc = md_to_html(open(os.path.join(ROOT, 'tools/vop_cs.md'), encoding='utf-8').read())
    main_html = f'''<main class="legal">
  <section class="legal-hero">
    <div class="container">
      <div class="crumbs mono"><a href="../">Úvod</a> <span>/</span> Obchodní podmínky</div>
      <h1>Všeobecné obchodní <span class="serif">podmínky</span></h1>
      <p>Platnost od {EFFECTIVE} · WebHunter s.r.o., IČO 29498511</p>
    </div>
  </section>
  <section class="container legal-body">
    <nav class="legal-toc toc-long" aria-label="Obsah">
      {''.join(f'<a href="#{i}">{html.escape(t)}</a>' for i, t in toc)}
    </nav>
    <article class="legal-text legal-vop">
      {body}
    </article>
  </section>
</main>'''
    s = re.sub(r'<main class="legal">.*?</main>', lambda m: main_html, tpl, count=1, flags=re.S)
    s = SEO_LINE.sub('', s)
    s = LD_RE.sub('', s)
    s = re.sub(r'<title>.*?</title>\n', lambda m: f'<title>{TITLE}</title>\n<meta name="description" content="{html.escape(DESC)}">\n{head_extras(PATH, TITLE, DESC)}\n', s, count=1)
    s = s.replace('</head>', ld(ORG) + '\n' + ld(breadcrumb([('Úvod', '/'), ('Obchodní podmínky', PATH)])) + '\n</head>', 1)
    s = re.sub(r'<a href="[^"]*" class="lang-sw"', '<a href="../en/" class="lang-sw"', s, count=1)
    d = os.path.join(ROOT, 'obchodni-podminky')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(s)
    print('obchodni-podminky ok,', len(toc), 'sections')


if __name__ == '__main__':
    main()
