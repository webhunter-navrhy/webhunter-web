# -*- coding: utf-8 -*-
"""Generates the white-label partner page for agencies: /partneri/ (cs) and /partneri/sk/ (sk).
Chrome (nav, footer, sprite, fonts) comes from gen_pages, so it always matches the rest of the site.
Run: python3 tools/gen_partneri.py  (build.sh runs it after gen_pages.py)"""
import os, re, sys, html
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from gen_pages import ROOT, FAVICON, FONTS, SPRITE, NAV, FOOTER, FX, obj, relink, words
from seo import SITE, ORG, EMAIL, ld, breadcrumb, faq_ld, head_extras

E = html.escape
ALT = {'cs': '/partneri/', 'sk': '/partneri/sk/'}

C = {
  'cs': {
    'title': 'White-label tvorba webů pro agentury | WebHunter',
    'desc': 'Weby na míru pro klienty marketingových, PPC, SEO a reklamních agentur pod vaší značkou. Klient o nás neví. Zkušební zakázka zdarma, návrh ještě týž den.',
    'crumbs': ('Úvod', 'Pro agentury'),
    'kicker': 'White-label pro agentury',
    'h1': 'Weby pro vaše klienty. <span class="serif">Pod vaší značkou.</span>',
    'lead': 'Web prodáváte pod svým jménem, my ho navrhneme a postavíme. Klient o nás neví. Vyzkoušejte si nás na jedné zakázce zdarma, návrh máte ještě týž den.',
    'btn': 'Poslat zkušební zadání', 'alt1': 'Jak spolupráce probíhá', 'alt2': 'Co se klient nedozví',
    'chip': 'White-label', 'mock_url': 'web-vaseho-klienta.cz', 'slot': 'Logo vaší agentury',
    'credit': 'Web vytvořila', 'credit_old': 'WebHunter', 'credit_new': 'vaše agentura',
    'hstats': [('Týž den', 'návrh'), ('0 Kč', 'zkouška'), ('NDA', 'na přání')],
    'subject': 'Partnerství – zkušební zakázka',
    'body': 'Dobrý den,\n\nposílám zkušební zadání.\n\nAgentura:\nKlient (obor, město):\nOdkaz na současný web klienta, nebo pár vět o firmě:\nCo má nový web přinést:\n\nDěkuji',
    'answer': 'WebHunter s.r.o. tvoří pro marketingové, PPC, SEO, social a reklamní agentury weby na míru pod jejich značkou. Agentura drží vztah s klientem i fakturaci, my zajistíme návrh, vývoj, SEO a GEO i spuštění. Partnerské projekty nikdy neukazujeme v našem portfoliu.',
    'answer_label': 'Ve zkratce',
    'vals': [
      ('bnv-dark', 'shield', 'Vaše značka, ne naše', 'Žádné naše logo, patička ani podpis v kódu. Náhledy posíláme na neutrální adrese.'),
      ('bnv-blue', 'bolt', 'Návrh ještě týž den', 'Zadání v pracovní den do 12:00 znamená hotový návrh do večera. Klientovi odpovíte dřív než konkurence.'),
      ('bnv-sky', 'cursor', 'Na míru, ne šablona', 'Každý web navrhujeme od nuly pro konkrétního klienta, jeho obor a zákazníky.'),
      ('bnv-lime', 'magnifier', 'SEO a GEO v základu', 'Struktura, rychlost a strukturovaná data pro Google i AI vyhledávače jako ChatGPT.'),
    ],
    'trial_label': 'Zkušební zakázka zdarma',
    'trial_h2': 'Pošlete nám jednoho klienta. <span class="serif">Zbytek je na nás.</span>',
    'trial_p': 'Nejlepší způsob, jak zjistit, jestli si sedneme, je jedna skutečná zakázka. Pošlete zadání jednoho svého klienta a my vám připravíme hotový návrh webu, který mu rovnou můžete ukázat. Zdarma a nezávazně.',
    'trial_need': 'Co nám stačí',
    'trial_list': ['Odkaz na současný web klienta, nebo pár vět o firmě', 'Pro koho web je a co má přinést: poptávky, prodej, rezervace', 'Logo a barvy, pokud je máte', 'Kdy potřebujete klientovi něco ukázat'],
    'trial_time': [('Do 12:00', 'pošlete zadání'), ('Týž den', 'máte návrh')],
    'trial_note': 'Platí pro pracovní dny. Zadání, které dorazí odpoledne, máte jako návrh do konce následujícího pracovního dne. Když se návrh nebude líbit vám nebo klientovi, nic neplatíte.',
    'wl_label': 'White-label', 'wl_h2': 'Klient vidí vás. <span class="serif">Nás ne.</span>',
    'wl_see': 'Co klient uvidí',
    'wl_see_list': ['Vaši značku a vaše jméno v celé komunikaci', 'Fakturu od vás, s vaší cenou', 'Náhled webu na neutrální adrese bez našeho jména', 'Hotový web na své vlastní doméně'],
    'wl_not': 'Co se nedozví',
    'wl_not_list': ['Že web postavil WebHunter', 'Naše logo, patičku „vytvořil…“ ani podpis v kódu a metadatech', 'Naši partnerskou cenu', 'Svůj web v našem portfoliu. Partnerské projekty nikde neukazujeme'],
    'wl_nda': 'Na přání podepíšeme smlouvu o mlčenlivosti (NDA) ještě před prvním zadáním.',
    'what_label': 'Co pro vaše klienty postavíme', 'what_h2': 'Celý web od návrhu <span class="serif">po spuštění.</span>',
    'blocks': [
      ('Weby a redesigny na míru', 'Firemní prezentace, landing pages pro kampaně i redesign zastaralého webu. Navrhujeme od nuly, žádné šablony.',
       ['Návrh designu podle oboru a značky klienta', 'Responzivní web pro mobil, tablet i počítač', 'Texty a struktura stránek, které vedou k poptávce', 'Napojení na analytiku, Meta Pixel a formuláře']),
      ('E-shopy, administrace a rezervace', 'Když klient potřebuje víc než prezentaci: prodávat, spravovat obsah nebo přijímat rezervace.',
       ['E-shopy na míru', 'Administrace, ve které si klient sám upraví obsah', 'Rezervační a poptávkové systémy', 'Napojení na služby, které klient už používá']),
      ('SEO, GEO, GDPR a rychlost v základu', 'Web, na který můžete rovnou navázat svou kampaní, SEO nebo správou sociálních sítí.',
       ['Technické SEO a strukturovaná data', 'GEO: příprava pro AI vyhledávače jako ChatGPT a Gemini', 'Cookie lišta a zásady ochrany osobních údajů', 'Rychlé načítání a moderní, bezpečné technologie']),
      ('Hosting zdarma, nebo předání', 'Web můžeme provozovat na našem hostingu zdarma, nebo ho předáme na hosting agentury či klienta, včetně zdrojového kódu a přístupů.', []),
    ],
    'steps_label': 'Jak spolupráce probíhá', 'steps_h2': 'Pět kroků. <span class="serif">Všechno e-mailem.</span>',
    'steps': [
      ('Zadání', 'Pošlete e-mailem odkaz na současný web klienta, nebo pár vět o firmě.'),
      ('Návrh týž den', 'Hotový návrh na neutrální adrese, který můžete klientovi rovnou přeposlat.'),
      ('Připomínky', 'Zapracujeme vaše i klientovy připomínky. Rozsah revizí domluvíme předem.'),
      ('Spuštění', 'Web spustíme na doméně klienta, na našem hostingu, nebo na vašem.'),
      ('Podpora a úpravy', 'Úpravy obsahu, rozšíření a technickou péči řešíte s námi, klient s vámi.'),
    ],
    'aud_label': 'Pro koho', 'aud': ['Marketingové agentury', 'PPC a výkonnostní agentury', 'SEO agentury', 'Social media agentury', 'Reklamní a kreativní studia'],
    'price_label': 'Cena', 'price_h2': 'Partnerská cena. <span class="serif">Individuálně a vždy předem.</span>',
    'price_p': 'Ceník nezveřejňujeme, každá zakázka je jiná. Partnerskou cenu stanovíme individuálně podle zadání, vždy předem, a necháváme prostor pro vaši marži. Fakturujeme agentuře, klient s námi nic neřeší.',
    'faq_label': 'Časté otázky', 'faq_h2': 'Na co se agentury <span class="serif">ptají.</span>',
    'faq_p': 'Nenašli jste odpověď? Napište nám, odpovídáme e-mailem a rychle.',
    'mail_card': 'Napište nám', 'mail_btn': 'Napsat e-mail',
    'faq': [
      ('Dozví se klient, že web stavěl někdo jiný?', 'Ne. Na webu není naše logo, patička ani podpis v kódu nebo metadatech a náhledy posíláme na neutrální adrese. Projekty partnerů nikdy nedáváme do našeho portfolia ani referencí. Na přání podepíšeme smlouvu o mlčenlivosti.'),
      ('Komu patří autorská práva a zdrojový kód?', 'Po zaplacení převádíme práva k webu na agenturu, nebo rovnou na klienta, jak se domluvíme. Zdrojový kód i přístupy předáme.'),
      ('Jak spolu komunikujeme?', 'E-mailem a jen s vámi. S klientem nekomunikujeme, pokud si to výslovně nepřejete.'),
      ('Jak probíhá fakturace?', 'Fakturujeme agentuře, fakturu vystavuje WebHunter s.r.o. Cenu pro klienta si určujete sami.'),
      ('Co když se klientovi návrh nelíbí?', 'Připomínky zapracujeme. U zkušební zakázky neplatíte nic, ani když se nakonec nedomluvíte.'),
      ('Na jakých technologiích weby stavíte?', 'Většinou čisté HTML, CSS a JavaScript, takže jsou weby rychlé a bezpečné. Když klient potřebuje sám upravovat obsah, přidáme administraci.'),
      ('Můžeme klientovi předat přístupy?', 'Ano. Web, kód i přístupy předáme agentuře nebo klientovi. Případně ho dál provozujeme na našem hostingu zdarma.'),
    ],
    'cta_label': 'Začněte jednou zakázkou', 'cta_h2': 'Vyzkoušejte nás na jednom klientovi. <span class="serif">Ještě dnes.</span>',
    'cta_p': 'Pošlete zadání e-mailem. Zkušební zakázka je zdarma a k ničemu vás nezavazuje.',
    'm_cta': 'Poslat zadání', 'nav_cta': 'Poslat zadání',
    'svc_name': 'White-label tvorba webů pro agentury',
  },
  'sk': {
    'title': 'White-label tvorba webov pre agentúry | WebHunter',
    'desc': 'Weby na mieru pre klientov marketingových, PPC, SEO a reklamných agentúr pod vašou značkou. Klient o nás nevie. Skúšobná zákazka zadarmo, návrh ešte v ten istý deň.',
    'crumbs': ('Úvod', 'Pre agentúry'),
    'kicker': 'White-label pre agentúry',
    'h1': 'Weby pre vašich klientov. <span class="serif">Pod vašou značkou.</span>',
    'lead': 'Web predávate pod svojím menom, my ho navrhneme a postavíme. Klient o nás nevie. Vyskúšajte si nás na jednej zákazke zadarmo, návrh máte ešte v ten istý deň.',
    'btn': 'Poslať skúšobné zadanie', 'alt1': 'Ako spolupráca prebieha', 'alt2': 'Čo sa klient nedozvie',
    'chip': 'White-label', 'mock_url': 'web-vasho-klienta.sk', 'slot': 'Logo vašej agentúry',
    'credit': 'Web vytvorila', 'credit_old': 'WebHunter', 'credit_new': 'vaša agentúra',
    'hstats': [('V ten deň', 'návrh'), ('Zadarmo', 'skúška'), ('NDA', 'na želanie')],
    'subject': 'Partnerstvo – skúšobná zákazka',
    'body': 'Dobrý deň,\n\nposielam skúšobné zadanie.\n\nAgentúra:\nKlient (odbor, mesto):\nOdkaz na súčasný web klienta alebo pár viet o firme:\nČo má nový web priniesť:\n\nĎakujem',
    'answer': 'WebHunter s.r.o. tvorí pre marketingové, PPC, SEO, social a reklamné agentúry weby na mieru pod ich značkou. Agentúra drží vzťah s klientom aj fakturáciu, my zabezpečíme návrh, vývoj, SEO a GEO aj spustenie. Partnerské projekty nikdy neukazujeme v našom portfóliu.',
    'answer_label': 'V skratke',
    'vals': [
      ('bnv-dark', 'shield', 'Vaša značka, nie naša', 'Žiadne naše logo, päta ani podpis v kóde. Náhľady posielame na neutrálnej adrese.'),
      ('bnv-blue', 'bolt', 'Návrh ešte v ten deň', 'Zadanie v pracovný deň do 12:00 znamená hotový návrh do večera. Klientovi odpoviete skôr ako konkurencia.'),
      ('bnv-sky', 'cursor', 'Na mieru, nie šablóna', 'Každý web navrhujeme od nuly pre konkrétneho klienta, jeho odbor a zákazníkov.'),
      ('bnv-lime', 'magnifier', 'SEO a GEO v základe', 'Štruktúra, rýchlosť a štruktúrované dáta pre Google aj AI vyhľadávače ako ChatGPT.'),
    ],
    'trial_label': 'Skúšobná zákazka zadarmo',
    'trial_h2': 'Pošlite nám jedného klienta. <span class="serif">Zvyšok je na nás.</span>',
    'trial_p': 'Najlepší spôsob, ako zistiť, či si sadneme, je jedna skutočná zákazka. Pošlite zadanie jedného svojho klienta a my vám pripravíme hotový návrh webu, ktorý mu môžete rovno ukázať. Zadarmo a nezáväzne.',
    'trial_need': 'Čo nám stačí',
    'trial_list': ['Odkaz na súčasný web klienta alebo pár viet o firme', 'Pre koho je web a čo má priniesť: dopyty, predaj, rezervácie', 'Logo a farby, ak ich máte', 'Kedy potrebujete klientovi niečo ukázať'],
    'trial_time': [('Do 12:00', 'pošlete zadanie'), ('V ten deň', 'máte návrh')],
    'trial_note': 'Platí pre pracovné dni. Zadanie, ktoré príde popoludní, máte ako návrh do konca nasledujúceho pracovného dňa. Ak sa návrh nebude páčiť vám alebo klientovi, nič neplatíte.',
    'wl_label': 'White-label', 'wl_h2': 'Klient vidí vás. <span class="serif">Nás nie.</span>',
    'wl_see': 'Čo klient uvidí',
    'wl_see_list': ['Vašu značku a vaše meno v celej komunikácii', 'Faktúru od vás, s vašou cenou', 'Náhľad webu na neutrálnej adrese bez nášho mena', 'Hotový web na svojej vlastnej doméne'],
    'wl_not': 'Čo sa nedozvie',
    'wl_not_list': ['Že web postavil WebHunter', 'Naše logo, pätu „vytvoril…“ ani podpis v kóde a metadátach', 'Našu partnerskú cenu', 'Svoj web v našom portfóliu. Partnerské projekty nikde neukazujeme'],
    'wl_nda': 'Na želanie podpíšeme zmluvu o mlčanlivosti (NDA) ešte pred prvým zadaním.',
    'what_label': 'Čo pre vašich klientov postavíme', 'what_h2': 'Celý web od návrhu <span class="serif">po spustenie.</span>',
    'blocks': [
      ('Weby a redizajny na mieru', 'Firemné prezentácie, landing pages pre kampane aj redizajn zastaraného webu. Navrhujeme od nuly, žiadne šablóny.',
       ['Návrh dizajnu podľa odboru a značky klienta', 'Responzívny web pre mobil, tablet aj počítač', 'Texty a štruktúra stránok, ktoré vedú k dopytu', 'Napojenie na analytiku, Meta Pixel a formuláre']),
      ('E-shopy, administrácia a rezervácie', 'Keď klient potrebuje viac ako prezentáciu: predávať, spravovať obsah alebo prijímať rezervácie.',
       ['E-shopy na mieru', 'Administrácia, v ktorej si klient sám upraví obsah', 'Rezervačné a dopytové systémy', 'Napojenie na služby, ktoré klient už používa']),
      ('SEO, GEO, GDPR a rýchlosť v základe', 'Web, na ktorý môžete rovno nadviazať svojou kampaňou, SEO alebo správou sociálnych sietí.',
       ['Technické SEO a štruktúrované dáta', 'GEO: príprava pre AI vyhľadávače ako ChatGPT a Gemini', 'Cookie lišta a zásady ochrany osobných údajov', 'Rýchle načítanie a moderné, bezpečné technológie']),
      ('Hosting zadarmo, alebo odovzdanie', 'Web môžeme prevádzkovať na našom hostingu zadarmo, alebo ho odovzdáme na hosting agentúry či klienta, vrátane zdrojového kódu a prístupov.', []),
    ],
    'steps_label': 'Ako spolupráca prebieha', 'steps_h2': 'Päť krokov. <span class="serif">Všetko e-mailom.</span>',
    'steps': [
      ('Zadanie', 'Pošlite e-mailom odkaz na súčasný web klienta alebo pár viet o firme.'),
      ('Návrh v ten deň', 'Hotový návrh na neutrálnej adrese, ktorý môžete klientovi rovno preposlať.'),
      ('Pripomienky', 'Zapracujeme vaše aj klientove pripomienky. Rozsah revízií dohodneme vopred.'),
      ('Spustenie', 'Web spustíme na doméne klienta, na našom hostingu alebo na vašom.'),
      ('Podpora a úpravy', 'Úpravy obsahu, rozšírenia a technickú starostlivosť riešite s nami, klient s vami.'),
    ],
    'aud_label': 'Pre koho', 'aud': ['Marketingové agentúry', 'PPC a výkonnostné agentúry', 'SEO agentúry', 'Social media agentúry', 'Reklamné a kreatívne štúdiá'],
    'price_label': 'Cena', 'price_h2': 'Partnerská cena. <span class="serif">Individuálne a vždy vopred.</span>',
    'price_p': 'Cenník nezverejňujeme, každá zákazka je iná. Partnerskú cenu stanovíme individuálne podľa zadania, vždy vopred, a nechávame priestor pre vašu maržu. Fakturujeme agentúre, klient s nami nič nerieši.',
    'faq_label': 'Časté otázky', 'faq_h2': 'Na čo sa agentúry <span class="serif">pýtajú.</span>',
    'faq_p': 'Nenašli ste odpoveď? Napíšte nám, odpovedáme e-mailom a rýchlo.',
    'mail_card': 'Napíšte nám', 'mail_btn': 'Napísať e-mail',
    'faq': [
      ('Dozvie sa klient, že web staval niekto iný?', 'Nie. Na webe nie je naše logo, päta ani podpis v kóde alebo metadátach a náhľady posielame na neutrálnej adrese. Projekty partnerov nikdy nedávame do nášho portfólia ani referencií. Na želanie podpíšeme zmluvu o mlčanlivosti.'),
      ('Komu patria autorské práva a zdrojový kód?', 'Po zaplatení prevádzame práva k webu na agentúru alebo rovno na klienta, ako sa dohodneme. Zdrojový kód aj prístupy odovzdáme.'),
      ('Ako spolu komunikujeme?', 'E-mailom a len s vami. S klientom nekomunikujeme, pokiaľ si to výslovne neželáte.'),
      ('Ako prebieha fakturácia?', 'Fakturujeme agentúre, faktúru vystavuje WebHunter s.r.o. Cenu pre klienta si určujete sami.'),
      ('Čo ak sa klientovi návrh nepáči?', 'Pripomienky zapracujeme. Pri skúšobnej zákazke neplatíte nič, ani keď sa nakoniec nedohodnete.'),
      ('Na akých technológiách weby staviate?', 'Väčšinou čisté HTML, CSS a JavaScript, takže sú weby rýchle a bezpečné. Keď klient potrebuje sám upravovať obsah, pridáme administráciu.'),
      ('Môžeme klientovi odovzdať prístupy?', 'Áno. Web, kód aj prístupy odovzdáme agentúre alebo klientovi. Prípadne ho ďalej prevádzkujeme na našom hostingu zadarmo.'),
    ],
    'cta_label': 'Začnite jednou zákazkou', 'cta_h2': 'Vyskúšajte nás na jednom klientovi. <span class="serif">Ešte dnes.</span>',
    'cta_p': 'Pošlite zadanie e-mailom. Skúšobná zákazka je zadarmo a k ničomu vás nezaväzuje.',
    'm_cta': 'Poslať zadanie', 'nav_cta': 'Poslať zadanie',
    'svc_name': 'White-label tvorba webov pre agentúry',
  },
}

# Slovak chrome: only the visible labels of nav + footer (cookie bar etc. stay as they are in site.js)
SK_CHROME = [
  ('>Realizace<', '>Realizácie<'), ('>Jak to funguje<', '>Ako to funguje<'), ('>Služby<', '>Služby<'), ('>AI vyhledávání<', '>AI vyhľadávanie<'),
  ('>Otázky<', '>Otázky<'), ('>Co dostanete<', '>Čo dostanete<'), ('>Navigace<', '>Navigácia<'),
  ('Weby na míru pro firmy, podnikatele a organizace. Návrh zdarma do 48 hodin.', 'Weby na mieru pre firmy, podnikateľov a organizácie. Návrh zadarmo do 48 hodín.'),
  ('>Tvorba webu na míru<', '>Tvorba webu na mieru<'), ('>Redesign webu<', '>Redizajn webu<'), ('>Tvorba e-shopů<', '>Tvorba e-shopov<'),
  ('>GEO pro AI vyhledávání<', '>GEO pre AI vyhľadávanie<'), ('>Pro agentury<', '>Pre agentúry<'),
  ('>Zásady ochrany osobních údajů<', '>Zásady ochrany osobných údajov<'), ('>Obchodní podmínky<', '>Obchodné podmienky<'), ('>Nastavení cookies<', '>Nastavenia cookies<'),
  ('aria-label="Hlavní navigace"', 'aria-label="Hlavná navigácia"'),
]


def mailto(c):
    return f'mailto:{EMAIL}?subject={quote(c["subject"])}&amp;body={quote(c["body"])}'


def checks(items):
    return ''.join(f'<li><i><svg><use href="#i-check"/></svg></i>{E(x)}</li>' for x in items)


def body(lang, c):
    mt = mailto(c)
    other = 'sk' if lang == 'cs' else 'cs'
    stats = ''.join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in c['hstats'])
    hero = f'''<section class="sub-hero svc-hero pt-hero" id="top">
  <div class="sub-frame">
    <div class="sub-bg"><img decoding="async" class="sky-par" src="img/hero-sky-1400.webp" srcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" sizes="100vw" alt="" fetchpriority="high"></div>
    <div class="sub-copy">
      <div class="crumbs mono"><a href="index.html">{E(c['crumbs'][0])}</a> <span>/</span> {E(c['crumbs'][1])}</div>
      <span class="svc-kicker mono">{E(c['kicker'])}</span>
      <h1>{words(c['h1'])}</h1>
      <p>{E(c['lead'])}</p>
      <div class="pt-hero-btns"><a href="{mt}" class="btn btn--lime">{E(c['btn'])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a></div>
      <div class="svc-alt"><a href="#postup">{E(c['alt1'])}</a><span aria-hidden="true">·</span><a href="#white-label">{E(c['alt2'])}</a></div>
    </div>
    <div class="svc-hcard pt-hcard bnx bnv-lime" aria-hidden="true">{FX.format('')}
      <span class="bn-chip dark">{E(c['chip'])}</span>
      <div class="pt-mock">
        <div class="pt-bar"><i></i><i></i><i></i><span>{E(c['mock_url'])}</span></div>
        <div class="pt-mock-body">
          <div class="pt-mock-nav"><span class="pt-slot">{E(c['slot'])}</span><span class="pt-lines"><i></i><i></i><i></i></span></div>
          <div class="pt-mock-hero"><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="b"></i></div>
          <div class="pt-mock-foot">{E(c['credit'])} <span class="pt-swap"><s>{E(c['credit_old'])}</s><em>{E(c['credit_new'])}</em></span></div>
        </div>
      </div>
      <div class="svc-hstats">{stats}</div>
    </div>
  </div>
</section>'''

    vals = ''.join(
        f'<div class="val bnx {v} reveal-item tilt">{FX.format(obj(o, "float-a ob-val"))}<span class="n-chip">0{i + 1}</span><b>{E(t)}</b><p>{E(d)}</p></div>'
        for i, (v, o, t, d) in enumerate(c['vals']))
    intro = f'''<section class="svc-intro">
  <div class="container">
    <div class="svc-answer reveal"><span class="label">{E(c['answer_label'])}</span><p>{E(c['answer'])}</p></div>
    <div class="vals svc-vals reveal-group">{vals}</div>
  </div>
</section>'''

    times = ''.join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in c['trial_time'])
    trial = f'''<section class="pt-trial bnx bnv-dark" id="zkouska">{FX.format(obj('bolt', 'float-a pt-trial-obj', '(max-width: 767px) 110px, 180px'))}
  <div class="container pt-trial-grid">
    <div class="pt-trial-copy">
      <span class="label reveal">{E(c['trial_label'])}</span>
      <h2 class="reveal">{c['trial_h2']}</h2>
      <p class="reveal">{E(c['trial_p'])}</p>
      <div class="pt-time reveal">{times}</div>
      <a href="{mt}" class="btn btn--lime reveal">{E(c['btn'])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a>
    </div>
    <div class="pt-need reveal">
      <span class="mono">{E(c['trial_need'])}</span>
      <ul class="pt-checks">{checks(c['trial_list'])}</ul>
      <p>{E(c['trial_note'])}</p>
    </div>
  </div>
</section>'''

    wl = f'''<section class="pt-wl" id="white-label">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">{E(c['wl_label'])}</span><h2 class="reveal">{c['wl_h2']}</h2></div>
    <div class="pt-wl-grid reveal-group">
      <div class="pt-wl-card pt-see reveal-item"><span class="mono">{E(c['wl_see'])}</span><ul class="pt-checks">{checks(c['wl_see_list'])}</ul></div>
      <div class="pt-wl-card pt-not reveal-item"><span class="mono">{E(c['wl_not'])}</span><ul class="pt-checks pt-x">{''.join(f'<li><i></i>{E(x)}</li>' for x in c['wl_not_list'])}</ul></div>
    </div>
    <p class="pt-nda reveal"><svg aria-hidden="true"><use href="#i-shield"/></svg>{E(c['wl_nda'])}</p>
  </div>
</section>'''

    blocks = ''
    for n, (h2, p, items) in enumerate(c['blocks']):
        lst = f'<ul class="svc-list">{checks(items)}</ul>' if items else ''
        blocks += f'<article class="svc-block reveal"><span class="svc-no mono">0{n + 1}</span><div><h2>{E(h2)}</h2><p>{E(p)}</p>{lst}</div></article>'
    what = f'''<section class="svc-content pt-what">
  <div class="container">
    <div class="svc-sechead"><span class="label reveal">{E(c['what_label'])}</span><h2 class="reveal">{c['what_h2']}</h2></div>
    <div class="svc-blocks">{blocks}</div>
  </div>
</section>'''

    steps = ''.join(f'<li class="pt-step reveal-item"><span class="pt-step-n">0{i + 1}</span><b>{E(t)}</b><p>{E(d)}</p></li>' for i, (t, d) in enumerate(c['steps']))
    process = f'''<section class="pt-proc" id="postup">
  <div class="pt-proc-frame">
    <div class="pt-proc-bg"><img decoding="async" class="sky-par" src="img/hero-sky-1400.webp" srcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" sizes="100vw" alt="" loading="lazy"></div>
    <div class="container">
      <span class="label reveal">{E(c['steps_label'])}</span>
      <h2 class="reveal">{c['steps_h2']}</h2>
      <ol class="pt-steps reveal-group">{steps}</ol>
    </div>
  </div>
</section>'''

    price = f'''<section class="pt-price">
  <div class="container pt-price-grid">
    <div class="pt-aud reveal"><span class="label">{E(c['aud_label'])}</span><ul>{''.join(f'<li>{E(a)}</li>' for a in c['aud'])}</ul></div>
    <div class="pt-price-card reveal"><span class="label">{E(c['price_label'])}</span><h2>{c['price_h2']}</h2><p>{E(c['price_p'])}</p></div>
  </div>
</section>'''

    faq = ''.join(
        f'<div class="qa{" open" if i == 0 else ""} reveal-item"><button class="q" aria-expanded="{"true" if i == 0 else "false"}"><span class="n">0{i + 1}</span>{E(q)}<span class="pm"></span></button><div class="a"><div><p>{E(a)}</p></div></div></div>'
        for i, (q, a) in enumerate(c['faq']))
    faqsec = f'''<section class="faq" id="faq">
  <div class="faq-panel">
    <div class="faq-deco" aria-hidden="true">?</div>
    <div class="container faq-grid">
      <div class="faq-side">
        <span class="label reveal">{E(c['faq_label'])}</span>
        <h2 class="reveal">{c['faq_h2']}</h2>
        <p class="reveal">{E(c['faq_p'])}</p>
        <div class="call-card pt-mail-card reveal"><span class="mono">{E(c['mail_card'])}</span><a class="tel" href="{mt}">{E(EMAIL)}</a><div class="row"><a href="{mt}" class="btn btn--lime">{E(c['mail_btn'])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a></div></div>
      </div>
      <div class="faq-list reveal-group">{faq}</div>
    </div>
  </div>
</section>'''

    cta = f'''<section class="cta-band pt-cta">
  <div class="container cb-grid">
    <div><span class="label reveal">{E(c['cta_label'])}</span><h2 class="reveal">{c['cta_h2']}</h2><p class="reveal">{E(c['cta_p'])}</p></div>
    <div class="cb-actions reveal"><a href="{mt}" class="btn btn--lime">{E(c['btn'])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a><a class="cb-tel" href="{mt}"><svg aria-hidden="true"><use href="#i-mail"/></svg>{E(EMAIL)}</a></div>
  </div>
</section>'''
    return '\n\n'.join([hero, intro, trial, wl, what, process, price, faqsec, cta])


def build(lang):
    c = C[lang]
    path = ALT[lang]
    R = '../' if lang == 'cs' else '../../'
    mt = mailto(c)
    lds = [ORG, breadcrumb([(c['crumbs'][0], '/'), (c['crumbs'][1], path)]),
           {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + '#service', "name": c['svc_name'],
            "serviceType": "White-label web design", "description": c['desc'], "url": SITE + path, "provider": {"@id": SITE + '/#org'},
            "audience": {"@type": "BusinessAudience", "audienceType": ', '.join(c['aud'])},
            "areaServed": [{"@type": "Country", "name": "Česká republika"}, {"@type": "Country", "name": "Slovensko"}],
            "inLanguage": lang,
            "offers": {"@type": "Offer", "name": c['trial_label'], "price": "0", "priceCurrency": "CZK" if lang == 'cs' else 'EUR', "description": c['trial_note']}},
           faq_ld(c['faq'])]
    nav = NAV.replace('<a href="index.html#sluzby">Co dostanete</a>', '<a href="sluzby/">Služby</a><a href="blog/">Blog</a>').replace('<a href="index.html#podpora">Po spuštění</a>', '')
    sw = ('<a href="partneri/sk/" class="lang-sw" hreflang="sk" lang="sk" aria-label="SK – slovenská verzia">SK</a>' if lang == 'cs'
          else '<a href="partneri/" class="lang-sw" hreflang="cs" lang="cs" aria-label="CZ – česká verze">CZ</a>')
    nav = re.sub(r'<a href="[^"]*" class="lang-sw"[^>]*>[A-Z]{2}</a>', sw, nav, count=1)
    nav = re.sub(r'<a href="[^"]*#kontakt" class="btn btn--lime">.*?</a>', f'<a href="{mt}" class="btn btn--lime">{E(c["nav_cta"])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a>', nav, count=1, flags=re.S)
    mcta = f'<a href="{mt}" class="m-cta" data-m-cta>{E(c["m_cta"])} <span class="arr"><svg><use href="#i-arrow"/></svg></span></a>'
    footer = FOOTER
    if lang == 'sk':
        for a, b in SK_CHROME:
            nav, footer = nav.replace(a, b), footer.replace(a, b)
    head = head_extras(path, c['title'], c['desc'], lang=lang, alt=ALT)
    if lang == 'sk':
        head = head.replace('content="cs_CZ"', 'content="sk_SK"')
    out = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{E(c['title'])}</title>
<meta name="description" content="{E(c['desc'])}">
{head}
{FAVICON}

{FONTS}

<script src="assets/vendor/gsap.min.js" defer></script>

<link rel="preload" as="image" href="img/hero-sky-1400.webp" imagesrcset="img/hero-sky-800.webp 800w, img/hero-sky-1400.webp 1400w, img/hero-sky-2000.webp 2000w" imagesizes="100vw" fetchpriority="high">
<link rel="stylesheet" href="assets/site.min.css?v=1">
{chr(10).join(ld(x) for x in lds)}
</head>
<body class="page-sub page-svc page-partneri">

<div class="scroll-progress"></div>
{SPRITE}

{nav}

<main>
{body(lang, c)}
</main>

{footer}

{mcta}
<script src="assets/site.min.js?v=1" defer></script>
</body>
</html>
'''
    dest = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(relink(out, R))


if __name__ == '__main__':
    for lang in C:
        build(lang)
    print('generated partneri (cs, sk)')
