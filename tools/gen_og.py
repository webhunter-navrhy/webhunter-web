# -*- coding: utf-8 -*-
"""Generates link-preview images (Open Graph, 1200×630) for every page type into img/og/, plus the favicon set.
Run manually after changing texts:  python3 tools/gen_og.py   (needs Playwright + Chromium)"""
import os, sys, re, html, asyncio
sys.path.insert(0, os.path.dirname(__file__))
from services_data import SERVICES
from blog_data import ARTICLES, CATS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = 'file://' + ROOT + '/'
E = html.escape
strip = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s))

CSS = f'''
@font-face {{ font-family: Geist; font-weight: 300 500; src: url({F}assets/fonts/Geist-normal-latin-gyByhwUxId.woff2) format('woff2'); unicode-range: U+0000-00FF; }}
@font-face {{ font-family: Geist; font-weight: 300 500; src: url({F}assets/fonts/Geist-normal-latin-ext-gyByhwUxId.woff2) format('woff2'); unicode-range: U+0100-024F, U+1E00-1EFF; }}
@font-face {{ font-family: GMono; src: url({F}assets/fonts/GeistMono-normal-latin-or3nQ6H-1_.woff2) format('woff2'); unicode-range: U+0000-00FF; }}
@font-face {{ font-family: GMono; src: url({F}assets/fonts/GeistMono-normal-latin-ext-or3nQ6H-1_.woff2) format('woff2'); unicode-range: U+0100-024F; }}
@font-face {{ font-family: ISerif; font-style: italic; src: url({F}assets/fonts/InstrumentSerif-italic-latin-jizHRFtNs2.woff2) format('woff2'); unicode-range: U+0000-00FF; }}
@font-face {{ font-family: ISerif; font-style: italic; src: url({F}assets/fonts/InstrumentSerif-italic-latin-ext-jizHRFtNs2.woff2) format('woff2'); unicode-range: U+0100-024F; }}
* {{ margin: 0; box-sizing: border-box; }}
body {{ width: 1200px; height: 630px; overflow: hidden; font-family: Geist, sans-serif; color: #fff; background: #1E4FD0; position: relative; }}
.sky {{ position: absolute; inset: -20px; background: url({F}img/hero-sky-1400.webp) center 30% / cover; }}
.tint {{ position: absolute; inset: 0; background: linear-gradient(90deg, rgba(8,30,90,0.82) 0%, rgba(10,40,120,0.55) 48%, rgba(10,40,120,0.05) 78%), linear-gradient(180deg, rgba(8,30,90,0.25), transparent 40%); }}
.wrap {{ position: absolute; inset: 0; padding: 58px 64px; display: flex; flex-direction: column; }}
.logo {{ font-size: 34px; font-weight: 500; letter-spacing: -0.05em; }}
.logo i {{ font-family: ISerif; font-weight: 400; font-size: 1.08em; letter-spacing: -0.02em; color: #C9F266; }}
.kick {{ margin-top: auto; display: inline-flex; align-self: flex-start; font-family: GMono; font-size: 17px; letter-spacing: 0.1em; text-transform: uppercase; padding: 10px 18px; border-radius: 999px; background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.35); }}
h1 {{ margin-top: 22px; font-weight: 400; font-size: var(--fs, 76px); line-height: 1.0; letter-spacing: -0.05em; max-width: var(--mw, 700px); }}
h1 em, h1 .serif {{ font-family: ISerif; font-weight: 400; font-size: 1.08em; letter-spacing: -0.02em; color: #C9F266; }}
p.sub {{ margin-top: 22px; font-size: 25px; font-weight: 300; line-height: 1.4; color: rgba(255,255,255,0.9); max-width: 620px; }}
.row {{ margin-top: 34px; display: flex; align-items: center; gap: 12px; }}
.url {{ font-family: GMono; font-size: 19px; letter-spacing: 0.06em; text-transform: uppercase; background: #C9F266; color: #0A0E14; padding: 14px 22px; border-radius: 999px; }}
.chip {{ font-size: 19px; padding: 12px 18px; border-radius: 999px; background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.3); }}
.side {{ position: absolute; right: 56px; top: 50%; transform: translateY(-50%); width: 400px; height: 470px; }}
.card {{ position: absolute; border-radius: 30px; padding: 26px; box-shadow: 0 40px 80px rgba(5,20,60,0.45); overflow: hidden; }}
.c-dark {{ background: radial-gradient(120% 90% at 85% 20%, #16306E 0%, #0B1430 45%, #070B12 100%); color: #fff; }}
.c-lime {{ background: linear-gradient(160deg, #DDF98E 0%, #C9F266 50%, #B2E046 100%); color: #0A0E14; }}
.c-sky {{ background: linear-gradient(165deg, #F4F8FF 0%, #DCE8FF 55%, #C4D8FF 100%); color: #0A0E14; }}
.c-blue {{ background: linear-gradient(160deg, #4B86FF 0%, #1E62F0 45%, #0C36A8 100%); color: #fff; }}
.chipk {{ display: inline-block; font-family: GMono; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; padding: 7px 12px; border-radius: 999px; background: #C9F266; color: #0A0E14; }}
.chipk.d {{ background: #0A0E14; color: #C9F266; }}
.big {{ font-size: 64px; letter-spacing: -0.04em; margin-top: 14px; font-family: GMono; }}
.bar {{ height: 5px; border-radius: 3px; background: linear-gradient(90deg, #1E62F0, #C9F266); margin-top: 16px; }}
.t {{ font-size: 30px; letter-spacing: -0.03em; line-height: 1.1; margin-top: 16px; }}
.t em {{ font-family: ISerif; color: #C9F266; font-size: 1.1em; }}
.obj {{ position: absolute; filter: drop-shadow(0 24px 30px rgba(5,20,60,0.35)); }}
.shot {{ position: absolute; background: #fff; border-radius: 18px; padding: 6px; box-shadow: 0 40px 80px rgba(5,20,60,0.45); }}
.shot img {{ display: block; width: 100%; border-radius: 0 0 13px 13px; }}
.shot .b {{ height: 22px; display: flex; gap: 5px; align-items: center; padding-left: 8px; }}
.shot .b i {{ width: 7px; height: 7px; border-radius: 50%; background: #d9dee6; }}
'''


def page_html(kicker, title, sub, side, fs=76, mw=700, chips=None, url='webhunter.cz'):
    n = len(strip(title))
    if n > 44: fs = min(fs, 58)
    elif n > 34: fs = min(fs, 64)
    mw = min(mw, 610)
    chips = chips if chips is not None else ['Návrh zdarma', 'Do 48 hodin']
    ch = ''.join(f'<span class="chip">{E(c)}</span>' for c in chips)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="sky"></div><div class="tint"></div>{side}
<div class="wrap"><div class="logo">Web<i>Hunter</i></div>
<span class="kick">{E(kicker)}</span>
<h1 style="--fs:{fs}px;--mw:{mw}px">{title}</h1>
{f'<p class="sub">{E(sub)}</p>' if sub else ''}
<div class="row"><span class="url">{E(url)}</span>{ch}</div></div></body></html>'''


def side_home(en=False):
    return f'''<div class="side">
<div class="card c-lime" style="width:230px;height:230px;right:0;top:0;transform:rotate(7deg)"><span class="chipk d">{'Free' if en else 'Zdarma'}</span>
<img class="obj" src="{F}img/3d/{'spark' if en else 'coin'}.webp" style="width:{'130' if en else '165'}px;left:50%;top:58%;transform:translate(-50%,-50%) rotate(-7deg)"></div>
<div class="card c-dark" style="width:330px;left:0;bottom:0;transform:rotate(-4deg)"><span class="chipk">{'Your design' if en else 'Váš návrh'}</span>
<div class="t">{'A new website for <em>your business</em>' if en else 'Nový web pro <em>vaši firmu</em>'}</div><div class="big">47:59:59</div><div class="bar"></div></div></div>'''


def side_obj(obj, variant='c-lime', chip='', text=''):
    return f'''<div class="side"><div class="card {variant}" style="width:360px;height:420px;right:10px;top:25px;transform:rotate(4deg)">
{f'<span class="chipk d">{E(chip)}</span>' if chip else ''}<img class="obj" src="{F}img/3d/{obj}.webp" style="width:250px;left:50%;top:52%;transform:translate(-50%,-50%)">
{f'<div class="t" style="position:absolute;left:26px;right:26px;bottom:26px;font-size:26px">{text}</div>' if text else ''}</div></div>'''


def side_work():
    sh = lambda slug, st: f'<div class="shot" style="{st}"><div class="b"><i></i><i></i><i></i></div><img src="{F}img/pf/{slug}-480.webp"></div>'
    return '<div class="side">' + sh('hasobeh-cz', 'width:300px;right:70px;top:0;transform:rotate(-6deg)') + sh('jakubmachalaphoto-cz', 'width:300px;right:-10px;top:150px;transform:rotate(5deg)') + sh('papapech-cz', 'width:320px;right:110px;top:270px;transform:rotate(-2deg);z-index:2') + '</div>'


def jobs():
    J = []
    J.append(('home', page_html('Tvorba webů na míru', 'Nový web zdarma <em>do&nbsp;48&nbsp;hodin.</em>', 'Potom se sami rozhodnete, zda budete chtít pokračovat.', side_home(), fs=84, mw=640)))
    J.append(('en', page_html('Custom website design', 'Your new website, <em>free in 48 hours.</em>', 'Then you decide whether to continue.', side_home(True), fs=84, mw=640, chips=['Free concept', 'No obligation'])))
    J.append(('realizace', page_html('Realizace', '41 webů. <em>Každý jiný.</em>', 'Videomakeři, fotografové, sportovní akce, farmy, e-shopy i reality.', side_work(), fs=88, mw=600, chips=['41 realizací'])))
    J.append(('en-work', page_html('Our work', '41 websites. <em>Each different.</em>', 'Videomakers, photographers, sports events, farms, online stores and real estate.', side_work(), fs=88, mw=600, chips=['41 projects'])))
    J.append(('sluzby', page_html('Služby', 'Všechno pro web, který <em>přivádí zákazníky.</em>', 'Weby, e-shopy, SEO, GEO a GDPR pod jednou střechou.', side_obj('spark', 'c-sky', 'Návrh zdarma do 48 h'), fs=70, mw=640)))
    V = {'tvorba-webu': 'c-lime', 'redesign-webu': 'c-blue', 'eshopy': 'c-lime', 'seo': 'c-sky', 'geo': 'c-dark', 'gdpr-cookies': 'c-sky'}
    for s in SERVICES:
        J.append((f'sluzby-{s["slug"]}', page_html(s['label'], s['h1'], strip(s['lead']).split('. ')[0].rstrip('.') + '.', side_obj(s['obj'], V.get(s['slug'], 'c-sky'), 'Návrh zdarma do 48 h'), fs=70, mw=660)))
    J.append(('blog', page_html('Blog', 'Rady, které vám <em>přivedou zákazníky.</em>', 'Ceny webů, SEO, AI vyhledávání a GDPR srozumitelně.', side_obj('bubble', 'c-dark', f'{len(ARTICLES)} článků'), fs=70, mw=640, chips=['Blog'])))
    for a in ARTICLES:
        J.append((f'blog-{a["slug"]}', page_html(f'Blog · {CATS[a["cat"]]}', a['h1'], None, side_obj(a['obj'], a['variant'].replace('bnv-', 'c-'), f'{a["read"]} min čtení'), fs=68, mw=680, chips=['Blog'])))
    return J


def favicons():
    """favicon.svg (brand W from Instrument Serif italic) + PNG sizes + favicon.ico + web manifest."""
    from fontTools.ttLib import TTFont
    from fontTools.pens.svgPathPen import SVGPathPen
    f = TTFont(ROOT + '/assets/fonts/InstrumentSerif-italic-latin-jizHRFtNs2.woff2'); gs = f.getGlyphSet()
    pen = SVGPathPen(gs); gs[f.getBestCmap()[ord('W')]].draw(pen)
    s = 42 / 730; tx = 32 - 431.5 * s + 0.8; ty = 32 + 355 * s
    def svg(rx=15, glow=True):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4B86FF"/><stop offset="0.5" stop-color="#1E62F0"/><stop offset="1" stop-color="#0C36A8"/></linearGradient>'
                f'<radialGradient id="l" cx="0.82" cy="0.14" r="0.62"><stop offset="0" stop-color="#C9F266" stop-opacity="0.38"/><stop offset="1" stop-color="#C9F266" stop-opacity="0"/></radialGradient></defs>'
                f'<rect width="64" height="64" rx="{rx}" fill="url(#g)"/>' + (f'<rect width="64" height="64" rx="{rx}" fill="url(#l)"/>' if glow else '') +
                f'<path transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f} {-s:.5f})" d="{pen.getCommands()}" fill="#C9F266" stroke="#C9F266" stroke-width="22" stroke-linejoin="round"/></svg>')
    open(ROOT + '/img/favicon.svg', 'w').write(svg())
    return svg(rx=0)  # full-bleed variant for app icons (iOS/Android round the corners themselves)


async def render():
    from playwright.async_api import async_playwright
    from PIL import Image
    os.makedirs(ROOT + '/img/og', exist_ok=True)
    square = favicons()
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        for name, doc in jobs():
            tmp = ROOT + f'/_raw/og_{name}.html'; os.makedirs(ROOT + '/_raw', exist_ok=True)
            open(tmp, 'w').write(doc)
            await pg.goto('file://' + tmp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            await pg.screenshot(path=ROOT + f'/img/og/{name}.png'); os.remove(tmp)
            im = Image.open(ROOT + f'/img/og/{name}.png').convert('RGB'); im.save(ROOT + f'/img/og/{name}.jpg', 'JPEG', quality=86, optimize=True, progressive=True)
            os.remove(ROOT + f'/img/og/{name}.png')
        for size, fn, svgdoc in [(32, 'favicon-32.png', open(ROOT + '/img/favicon.svg').read()), (48, 'favicon-48.png', open(ROOT + '/img/favicon.svg').read()),
                                 (180, 'apple-touch-icon.png', square), (192, 'icon-192.png', square), (512, 'icon-512.png', square)]:
            ip = await b.new_page(viewport={'width': size, 'height': size})
            await ip.set_content(f'<html><body style="margin:0;background:transparent">{svgdoc.replace("<svg ", f"<svg width=\"{size}\" height=\"{size}\" ")}</body></html>')
            await ip.screenshot(path=ROOT + '/img/' + fn, omit_background=True); await ip.close()
        await b.close()
    ico = Image.open(ROOT + '/img/favicon-48.png'); ico.save(ROOT + '/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    open(ROOT + '/site.webmanifest', 'w').write('{"name":"WebHunter","short_name":"WebHunter","icons":[{"src":"/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/img/icon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#1E62F0","background_color":"#F2F5F8","display":"browser","start_url":"/"}\n')
    print('og images + favicons ok')


if __name__ == '__main__':
    asyncio.run(render())
