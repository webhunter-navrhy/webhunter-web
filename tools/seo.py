# -*- coding: utf-8 -*-
"""Shared SEO/GEO data: production URL, organisation schema, head builder."""
import json, re, html

SITE = 'https://webhunter.cz'
ORG_ID = SITE + '/#org'
PHONE = '+420777611634'
EMAIL = 'info.webhunter@email.cz'

ORG = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": ORG_ID,
  "name": "WebHunter s.r.o.",
  "alternateName": "WebHunter",
  "url": SITE + "/",
  "logo": SITE + "/img/logo.png",
  "image": SITE + "/img/og.jpg",
  "description": "Česká webová agentura. Tvoříme webové stránky a e-shopy na míru s důrazem na SEO, GEO (AI vyhledávání) a GDPR. Návrh nového webu zdarma a nezávazně do 48 hodin.",
  "slogan": "Zdarma vám navrhneme nový web do 48 hodin. Potom se sami rozhodnete, zda budete chtít pokračovat.",
  "telephone": PHONE,
  "email": EMAIL,
  "identifier": {"@type": "PropertyValue", "propertyID": "IČO", "value": "29498511"},
  "address": {"@type": "PostalAddress", "addressLocality": "Praha", "addressCountry": "CZ"},
  "areaServed": [{"@type": "Country", "name": "Česká republika"}, {"@type": "Country", "name": "Slovensko"}],
  "availableLanguage": ["cs", "en"],
  "knowsAbout": ["Tvorba webových stránek", "Tvorba e-shopů", "Redesign webu", "SEO", "GEO – optimalizace pro AI vyhledávání", "GDPR a cookies", "Copywriting", "Konverzní optimalizace"],
  "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE, "email": EMAIL, "availableLanguage": ["Czech", "English"], "areaServed": "CZ"}],
  "sameAs": ["https://wa.me/420777611634"],
}

from services_data import SERVICES as _SERVICES
ORG["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": "Služby WebHunter", "itemListElement": [
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": _s["nav"], "url": SITE + "/sluzby/" + _s["slug"] + "/", "description": _s["desc"]}} for _s in _SERVICES]}

WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "WebHunter",
           "inLanguage": "cs-CZ", "publisher": {"@id": ORG_ID}}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '</script>'


def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}


def faq_ld(pairs):
    strip = lambda s: re.sub(r'<[^>]+>', '', s)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in pairs]}


def head_extras(path, title, desc, og_img='img/og.jpg', lang='cs', alt=None, robots='index, follow, max-image-preview:large, max-snippet:-1'):
    """canonical, hreflang, OG/Twitter. path = production path starting with '/'. alt = {'cs': '/x', 'en': '/en/x'}"""
    e = html.escape
    url = SITE + path
    out = [f'<link rel="canonical" href="{url}">', f'<meta name="robots" content="{robots}">']
    if alt:
        for k, v in alt.items():
            out.append(f'<link rel="alternate" hreflang="{k}" href="{SITE + v}">')
        out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE + alt.get("cs", path)}">')
    out += [
        '<meta property="og:type" content="website">', '<meta property="og:site_name" content="WebHunter">',
        f'<meta property="og:locale" content="{"cs_CZ" if lang == "cs" else "en_US"}">',
        f'<meta property="og:title" content="{e(title)}">', f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:url" content="{url}">', f'<meta property="og:image" content="{SITE}/{og_img}">',
        '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:image" content="{SITE}/{og_img}">',
        '<meta name="theme-color" content="#2b62c4">', '<meta name="format-detection" content="telephone=no">',
    ]
    return '\n'.join(out)
