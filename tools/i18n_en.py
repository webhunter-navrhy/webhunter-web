# -*- coding: utf-8 -*-
"""Czech -> English strings for the /en/ pages. Keys are text nodes / attribute values exactly as they appear
in the Czech HTML (non-breaking spaces normalised to plain spaces). gen_en.py reports anything left untranslated."""

# raw HTML blocks replaced before the text-node pass (word order differs too much for fragment translation)
BLOCKS = [
    ('Potom se sami rozhodnete, zda budete chtít pokračovat. Nemáte web? Stačí <a href="#kontakt" class="hero-alt" data-no-web>pár vět o&nbsp;firmě</a>.',
     'Then you decide whether to continue. No website yet? A <a href="#kontakt" class="hero-alt" data-no-web>few lines about your business</a> will do.'),
    ('''<span class="w"><span><em class="serif">Zdarma</em></span></span> <span class="w"><span>vám</span></span> <span class="w"><span>navrhneme</span></span><br>
        <span class="l2"><span class="w"><span>nový</span></span> <span class="w"><span>web</span></span> <span class="w"><span>do</span></span> <span class="w"><span>48&nbsp;hodin.</span></span></span>''',
     '''<span class="w"><span>Your</span></span> <span class="w"><span>new</span></span> <span class="w"><span>website,</span></span><br>
        <span class="l2"><span class="w"><span><em class="serif">free</em></span></span> <span class="w"><span>in</span></span> <span class="w"><span>48&nbsp;hours.</span></span></span>'''),
    ('<span class="w"><span>41</span></span> <span class="w"><span>webů.</span></span> <span class="w"><span>Každý</span></span> <span class="w"><span>jiný.</span></span><br><span class="l2"><span class="w"><span><em class="serif">Žádná</em></span></span> <span class="w"><span><em class="serif">šablona.</em></span></span></span>',
     '<span class="w"><span>41</span></span> <span class="w"><span>websites.</span></span> <span class="w"><span>Each</span></span> <span class="w"><span>different.</span></span><br><span class="l2"><span class="w"><span><em class="serif">Zero</em></span></span> <span class="w"><span><em class="serif">templates.</em></span></span></span>'),
]

T = {
    # ---------- nav / chrome ----------
    'Hlavní navigace': 'Main navigation', 'Realizace': 'Our work', 'Jak to funguje': 'How it works', 'Co dostanete': 'What you get',
    'AI vyhledávání': 'AI search', 'Tým': 'Team', 'Otázky': 'FAQ', 'Chci návrh zdarma': 'Get a free design', 'Menu': 'Menu',
    'Rychlá navigace': 'Quick navigation', 'Úvod': 'Home', 'Služby': 'Services',
    # ---------- hero ----------
    'Modrá obloha s mraky': 'Blue sky with clouds', 'Nezávazně · bez porad · do 48 hodin': 'No strings · no meetings · within 48 hours',
    'Odkaz na váš současný web': 'Link to your current website', 'vasefirma.cz': 'yourcompany.com',
    'Rychlost': 'Speed', 'Načtení': 'Load time', '0,8 s': '0.8 s', 'V pořádku': 'Passed', 'pozice': 'position',
    'stavební firma brno': 'builders near me', 'Rekonstrukce bytů v Brně': 'Apartment renovations in Brno', 'Naše realizace': 'Our projects',
    'Váš návrh': 'Your design', 'Připraveno': 'Ready', 'Nový web pro': 'A new website for', 'vaši firmu': 'your business',
    'Hotovo dřív, než uplynulo 48 hodin.': 'Done before the 48 hours were up.', 'zbývá': 'left', 'Zobrazit návrh': 'View design',
    'Krok 01': 'Step 01', 'Pošlete': 'Send a', 'odkaz': 'link', 'Návrh máte do 48 hodin.': 'Your design arrives within 48 hours.',
    'Odpověď AI': 'AI answer', 'Koho doporučuješ v Brně?': 'Who do you recommend in Brno?', 'Doporučuji': 'I recommend',
    'Vaši firmu': 'your business', '— jasné ceny a reference.': '— clear pricing and references.', 'Vaše': 'Your', 'soukromí': 'privacy',
    'Nezbytné': 'Necessary', 'Analytické': 'Analytics', 'Marketing': 'Marketing',
    # ---------- marquee ----------
    'Klienti, pro které jsme postavili web': 'Clients we have built websites for', 'Weby, které jsme postavili ·': 'Websites we have built ·',
    'všech 41 realizací →': 'all 41 projects →', 'Rodinný dům Píšť': 'Píšť Family Home', 'J2 Italské pece': 'J2 Italian Ovens',
    # ---------- manifest / bento ----------
    'Proč WebHunter': 'Why WebHunter', 'Web nemá jen dobře vypadat.': 'A website should do more than look good.',
    'Má přivádět nové': 'It should bring you new', 'zákazníky.': 'customers.', 'Expresní návrh': 'Express design',
    'Od zaslání odkazu k hotovému návrhu. Bez porad, briefů a dotazníků.': 'From your link to a finished design. No meetings, briefs or questionnaires.',
    'Návrh zdarma a nezávazně': 'Free, no-obligation design', 'Kč': 'CZK', 'Žádná záloha': 'No deposit', 'Žádná smlouva předem': 'No contract upfront',
    'Žádný závazek pokračovat': 'No obligation to continue', 'Nejdřív uvidíte svůj nový web.': 'First you see your new website.',
    'Až potom': 'Only then', 'se rozhodujete.': 'do you decide.', 'Dohledatelní na Googlu i v AI': 'Found on Google and in AI',
    'Weby stavíme tak, aby vás našel Google i ChatGPT, Perplexity nebo Gemini.': 'We build websites so that Google, ChatGPT, Perplexity and Gemini can all find you.',
    'S odborníky z': 'With the experts at', 'Cookies, souhlasy a osobní údaje nastavené správně od prvního dne.': 'Cookies, consents and personal data handled correctly from day one.',
    # ---------- process ----------
    'Modrá obloha se sluncem': 'Blue sky with sunshine', 'Tři kroky.': 'Three steps.', 'Žádné porady.': 'No meetings.',
    'Nemusíte chodit na schůzky ani vyplňovat technické zadání. O většinu práce se postaráme my — vy jen řeknete ano, nebo ne.':
        'No meetings, no technical specifications. We do most of the work — you just say yes or no.',
    'Krok 01 · 2 minuty': 'Step 01 · 2 minutes', 'Pošlete odkaz nebo pár vět': 'Send a link or a few lines',
    'Stačí adresa vašeho současného webu. Pokud žádný nemáte, napište nám stručně, čím se zabýváte.':
        'The address of your current website is enough. No website? Just tell us briefly what you do.',
    'Krok 02 · do 48 hodin': 'Step 02 · within 48 hours', 'Do 48 hodin máte návrh': 'Your design within 48 hours',
    'Konkrétní podoba vašeho nového webu. Ne prezentace ani cenová nabídka — skutečný návrh, který si proklikáte.':
        'A concrete look at your new website. Not a slide deck or a quote — a real design you can click through.',
    'Krok 03 · je to na vás': 'Step 03 · your call', 'Rozhodnete se sami': 'You decide',
    'Líbí se vám? Pustíme se do realizace. Nelíbí? Nic nám nedlužíte a nikdo vás nebude přemlouvat.':
        'Like it? We get to work. Don’t? You owe us nothing and nobody will try to talk you into it.',
    'Vás to stojí 2 minuty. Nás 48 hodin práce.': 'It costs you 2 minutes. It costs us 48 hours of work.',
    # ---------- services ----------
    'Web, který': 'A website that', 'vypadá dobře': 'looks good', 'a hlavně': 'and, above all,', 'prodává.': 'sells.',
    'Každý web řešíme od designu přes texty až po to, jak ho najde Google a umělá inteligence. Všechno pod jednou střechou.':
        'We handle every website end to end — design, copy, and how Google and AI find it. All under one roof.',
    'Původní web Reality Nekvinda z roku 2025': 'The original Reality Nekvinda website from 2025', 'Nový web Reality Nekvinda od WebHunter': 'The new Reality Nekvinda website by WebHunter',
    'Předtím · 2025': 'Before · 2025', 'Teď · náš web': 'Now · our website', 'Web na míru': 'Custom website',
    'Žádné šablony. Každý web navrhujeme pro konkrétní firmu, její zákazníky a cíle. Posuňte jezdcem: vlevo původní web klienta z internetového archivu, vpravo web, který jsme mu postavili.':
        'No templates. Every website is designed for a specific business, its customers and goals. Drag the slider: on the left, the client’s original website from the Internet Archive; on the right, the one we built.',
    'Vyberte klienta': 'Choose a client', 'Portál Výsluní': 'Výsluní Portal', 'rekonstrukce bytů brno': 'apartment renovation brno',
    'Pozice ve vyhledávání': 'Search position', 'Technicky čistý web, správná struktura a obsah, kterému Google rozumí.': 'A technically clean website, the right structure and content Google understands.',
    'Doporučuje': 'Recommends', 'Novinka': 'New', 'Optimalizace pro AI vyhledávání, aby vás doporučila i umělá inteligence.': 'Optimisation for AI search, so artificial intelligence recommends you too.',
    'Nabízíme kvalitní kovářské a zámečnické práce za příznivé ceny.': 'We offer quality blacksmithing and metalwork at affordable prices.',
    'Žádná sériová výroba,': 'No mass production,', 'žádné odlitky.': 'no castings.', 'Náš text pro kovotuk.cz ↗': 'Our copy for kovotuk.cz ↗',
    'Jasné sdělení': 'Clear message', 'Bez žargonu': 'No jargon', 'Texty, které prodávají': 'Copy that sells',
    'Víme, co návštěvníka přesvědčí zavolat nebo poptat. Píšeme jednoduše a konkrétně. Nahoře obecná věta, dole náš text pro kováře z Bruntálska.':
        'We know what makes a visitor call or send an enquiry. We write simply and specifically. Top: a generic sentence. Bottom: our copy for a blacksmith from the Bruntál region.',
    'Používáme cookies': 'We use cookies', 'Nezbytné cookies jsou vždy zapnuté. Ostatní jen s vaším souhlasem.': 'Necessary cookies are always on. Others only with your consent.',
    'Přijmout vše': 'Accept all', 'Nastavení': 'Settings', 'GDPR a cookies': 'GDPR & cookies',
    'Souhlasy a zpracování údajů řešíme s odborníky z': 'We handle consents and data processing with the experts at',
    'Stabilita': 'Stability', 'Odezva': 'Response', 'Rychlost a bezpečnost': 'Speed & security',
    'Moderní technologie a web, který vydrží roky bez starostí.': 'Modern technology and a website that runs worry-free for years.',
    'Všechno v jednom': 'All in one', 'Tohle všechno uvidíte v návrhu.': 'You will see all of this in your design.', 'Zdarma.': 'Free.', 'Chci návrh': 'Get my design',
    # ---------- reel ----------
    'Ukázky realizací': 'Selected projects', 'Web Papa Pech': 'Papa Pech website', 'Web Hasoběh': 'Hasoběh website', 'Web Farma Tájek': 'Farma Tájek website',
    'Web Rodinný dům Píšť': 'Píšť Family Home website', 'Web F-Fashion': 'F-Fashion website', 'Web Pension Maty': 'Pension Maty website',
    'Web Reality Centrum Praha': 'Reality Centrum Praha website', 'Web Alissa Beauté': 'Alissa Beauté website', 'Web Galenit': 'Galenit website',
    'Web Jakub Machala': 'Jakub Machala website', 'Web SportActive': 'SportActive website', 'Web Beka Bazar': 'Beka Bazar website', 'Web KovoTuk': 'KovoTuk website',
    'Web J2 Italské pece': 'J2 Italian Ovens website', 'Web Držíme ti palce': 'Držíme ti palce website', 'Web Axon Capital': 'Axon Capital website',
    'Web Comedy & Beat Circus': 'Comedy & Beat Circus website', 'Web Molver Group': 'Molver Group website',
    'Portfolio': 'Portfolio', '41 webů': '41 websites', 'od Krkonoš po Ostravu': 'across the Czech Republic',
    'Pro videomakery, fotografy, sportovní akce, farmy i e-shopy.': 'For videomakers, photographers, sports events, farms and online stores.',
    'Prohlédnout realizace': 'See our work',
    # ---------- GEO ----------
    'GEO · optimalizace pro AI': 'GEO · AI search optimisation', 'Zákazníci se už neptají jen Googlu.': 'Customers no longer ask only Google.', 'Ptají se AI.': 'They ask AI.',
    'Stále víc lidí hledá dodavatele přes ChatGPT, Perplexity nebo Gemini. Weby proto připravujeme tak, aby jim umělá inteligence rozuměla — a doporučila právě vás.':
        'More and more people find suppliers through ChatGPT, Perplexity or Gemini. So we build websites that AI understands — and recommends you.',
    'AI asistent': 'AI assistant', 'Ilustrační ukázka': 'Illustrative example',
    'Potřebuju v Olomouci někoho na rekonstrukci koupelny. Koho doporučuješ?': 'I need someone in Olomouc to renovate my bathroom. Who do you recommend?',
    'recenze': 'reviews', 'ceník': 'pricing', 'Takhle může AI doporučit vaši firmu': 'This is how AI can recommend your business',
    # ---------- team ----------
    'Kdo za tím stojí': 'Who we are', 'Nejsme jen vývojáři a designéři.': 'We are not just developers and designers.', 'Rozumíme obchodu.': 'We understand business.',
    'WebHunter je česká webová agentura. V týmu máme lidi s dlouholetou praxí v obchodě, marketingu, budování značek, práci se zákazníky a škálování firem — a samozřejmě designéry a vývojáře.':
        'WebHunter is a Czech web design agency. Our team brings years of experience in sales, marketing, branding, customer care and scaling businesses — plus, of course, designers and developers.',
    'Proto u každého webu neřešíme jen vzhled a technologie. Hlavně řešíme, jak z návštěvníka udělat zákazníka.':
        'That is why we never stop at looks and technology. Our focus is turning visitors into customers.',
    'Najeďte na obor a uvidíte, co přináší vašemu webu': 'Hover over a discipline to see what it brings to your website',
    'Obory v našem týmu': 'Disciplines in our team', 'Všechno míří sem': 'It all leads here', 'Váš web': 'Your website',
    'Šest oborů, jeden cíl: víc poptávek pro vaši firmu.': 'Six disciplines, one goal: more enquiries for your business.',
    'Obchod': 'Sales', 'Budování značky': 'Branding', 'Práce se zákazníky': 'Customer care', 'Škálování firem': 'Scaling businesses', 'Design a vývoj': 'Design & development',
    'Víme, co zákazníka přesvědčí zavolat, poptat nebo objednat. Každou sekci webu stavíme k tomuto kroku.': 'We know what convinces a customer to call, enquire or order. Every section is built towards that step.',
    'Web připravíme na kampaně a měření, aby bylo vidět, odkud poptávky chodí.': 'We prepare your website for campaigns and tracking, so you can see where enquiries come from.',
    'Jasné sdělení a jednotný vzhled, díky kterým si vás lidé zapamatují a začnou vám věřit.': 'A clear message and consistent look that make people remember and trust you.',
    'Víme, na co se lidé ptají, než se rozhodnou. Odpovědi dáváme na web dřív, než je napíšou.': 'We know what people ask before they decide, and we answer it on your website before they write to you.',
    'Web navrhujeme tak, aby rostl s vámi: nové služby, pobočky i jazyky bez předělávání.': 'We design websites that grow with you: new services, branches and languages without a rebuild.',
    'Moderní, rychlý a bezpečný web na míru. Žádná šablona, žádné zbytečné kompromisy.': 'A modern, fast and secure custom website. No template, no needless compromises.',
    'Nejdřív ukážeme, pak se bavíme': 'We show first, then we talk',
    'Návrh zdarma do 48 hodin. O spolupráci mluvíme až nad něčím konkrétním.': 'A free design within 48 hours. We only discuss working together over something concrete.',
    'Mluvíme lidsky': 'We speak plainly', 'Žádné agenturní fráze ani technický žargon. Na weby i v e-mailech.': 'No agency buzzwords or technical jargon. On websites and in emails.',
    'Web měříme poptávkami': 'We measure websites in enquiries', 'Hezký vzhled je začátek. Úspěch je, když vám web přivádí zákazníky.': 'Good looks are the start. Success is when your website brings you customers.',
    'GDPR bereme vážně': 'We take GDPR seriously', 'Cookies, souhlasy a osobní údaje řešíme s odborníky z': 'We handle cookies, consents and personal data with the experts at',
    # ---------- after launch ----------
    'Po spuštění': 'After launch', 'Web, který vás': 'A website that won’t', 'neomezí.': 'hold you back.',
    'Naše práce nekončí předáním webu. Co potřebujete, upravíte si sami. A když jde o něco složitějšího, máte nás po ruce.':
        'Our work doesn’t end at handover. Edit what you need yourself — and for anything more complex, we’re right here.',
    'Upravíte si ho sami': 'Edit it yourself',
    'Když ji potřebujete, dostanete přehlednou administraci. Texty, fotky nebo novinky změníte sami, bez psaní webaři.':
        'If you need it, you get a clear admin panel. Change texts, photos or news yourself, without emailing a developer.',
    'Rychlé úpravy do 1–2 dnů': 'Changes within 1–2 days',
    'Když je potřeba něco složitějšího, ozvěte se. Na vaše požadavky reagujeme do jednoho až dvou pracovních dnů.':
        'Need something more complex? Get in touch. We respond to your requests within one to two business days.',
    'Hosting u většiny webů zdarma': 'Free hosting for most websites',
    'Platí se jen u velkých projektů nebo rychlejších variant. Doménu si platíte přímo u jejího poskytovatele.':
        'You only pay for large projects or faster hosting plans. The domain is paid directly to its registrar.',
    'Postaráme se o všechno kolem': 'We handle everything around it',
    'Napojení na doménu, spuštění, SEO a GEO, cookies a GDPR, obchodní podmínky i napojení na mailing.':
        'Domain setup, launch, SEO and GEO, cookies and GDPR, terms and conditions, and email marketing integration.',
    'Záleží na rozsahu. Cenu vždy znáte předem: dostanete nabídku, ve které je přesně rozepsané, co obsahuje. Ještě než se rozhodnete, jestli do toho půjdete. Žádné skryté poplatky.':
        'It depends on the scope. You always know the price upfront: you get a quote that lists exactly what it includes, before you decide to go ahead. No hidden fees.',
    'Co všechno je v ceně?': 'What’s included in the price?',
    'Návrh, design, texty, technické řešení, SEO a GEO, cookies a GDPR, napojení na doménu i spuštění webu. Hosting je u většiny webů zdarma, platí se jen u velkých projektů nebo rychlejších variant hostingu. Doménu si platíte sami u jejího poskytovatele.':
        'The design, copy, technical build, SEO and GEO, cookies and GDPR, domain setup and launch. Hosting is free for most websites; you only pay for large projects or faster hosting plans. You pay for the domain yourself, directly to its registrar.',
    'Můžu si web upravovat sám?': 'Can I edit the website myself?',
    'Ano. Když ji potřebujete, dostanete administraci, ve které si texty, fotky nebo novinky změníte sami. Složitější úpravy za vás rádi uděláme, na požadavky reagujeme do jednoho až dvou pracovních dnů.':
        'Yes. If you need it, you get an admin panel where you can change texts, photos or news yourself. We’re happy to handle more complex changes and respond within one to two business days.',
    'Cenu znáte předem, bez skrytých poplatků': 'Price known upfront, no hidden fees',
    # ---------- FAQ ----------
    'Časté otázky': 'FAQ', 'Máte otázku?': 'Got a question?', 'Tady je odpověď.': 'Here is the answer.',
    'A když ne, zavolejte nebo napište. Odpovídáme lidsky a rychle.': 'And if not, call or message us. We reply quickly and in plain words.',
    'Raději zavoláte?': 'Prefer to call?', 'Zavolat': 'Call', 'Je návrh opravdu zdarma?': 'Is the design really free?',
    'Ano. Návrh vás nic nestojí a k ničemu vás nezavazuje. Platíte až za realizaci — a jen pokud se pro ni sami rozhodnete.':
        'Yes. The design costs you nothing and commits you to nothing. You only pay for the build — and only if you decide to go ahead.',
    'Co od vás potřebujeme?': 'What do you need from me?',
    'Odkaz na váš současný web. Pokud žádný nemáte, stačí pár vět o tom, co děláte a pro koho. Víc není potřeba.':
        'A link to your current website. If you don’t have one, a few lines about what you do and for whom. That’s all.',
    'Co když se mi návrh nebude líbit?': 'What if I don’t like the design?',
    'Pak nemusíte pokračovat. Nebo nám řeknete, co by mělo být jinak, a návrh upravíme.': 'Then you don’t have to continue. Or tell us what should be different and we’ll adjust it.',
    'Kolik stojí realizace webu?': 'How much does a website cost?',
    'Záleží na rozsahu. Cenu vždy znáte předem — ještě než se rozhodnete, jestli do toho půjdete.': 'It depends on the scope. You always know the price upfront — before you decide to go ahead.',
    'Co je GEO a proč ho potřebuji?': 'What is GEO and why do I need it?',
    'GEO je optimalizace pro AI vyhledávání. Lidé se čím dál častěji ptají ChatGPT nebo Gemini, koho si mají vybrat. Připravujeme weby tak, aby je umělá inteligence dobře pochopila a mohla vás doporučit.':
        'GEO (generative engine optimisation) is optimisation for AI search. People increasingly ask ChatGPT or Gemini whom to choose. We build websites that AI understands well and can recommend.',
    'Řešíte i GDPR a cookies?': 'Do you handle GDPR and cookies too?', 'Ano, a bereme to vážně. Spolupracujeme s odborníky z': 'Yes, and we take it seriously. We work with the experts at',
    ', takže cookies, souhlasy i zpracování osobních údajů jsou nastavené správně.': ', so cookies, consents and personal data processing are set up correctly.',
    'Můžu vidět weby, které jste už udělali?': 'Can I see websites you have built?', 'Jasně. Na stránce': 'Sure. On our',
    'najdete 41 webů — třeba osobní značku videomakera Papa Pecha, svatebního fotografa Jakuba Machalu nebo běžecký závod Hasoběh. Každý si můžete rovnou proklikat.':
        'page you will find 41 websites — such as videomaker Papa Pech’s personal brand, wedding photographer Jakub Machala or the Hasoběh running race. You can click through each one.',
    'Uděláte i e-shop, rezervace nebo registrace?': 'Can you build online stores, bookings or registrations?',
    'Ano. Stavíme e-shopy (Beka Bazar), prodej online kurzů (Papa Pech), rezervace lekcí (SportActive), registrace na akce s platbou (Hasoběh) i měsíční příspěvky (Držíme ti palce). V návrhu rovnou uvidíte, jak by to fungovalo u vás.':
        'Yes. We build online stores (Beka Bazar), online course sales (Papa Pech), class bookings (SportActive), paid event registrations (Hasoběh) and monthly donations (Držíme ti palce). Your design will show how it would work for you.',
    # ---------- contact ----------
    'Mraky na modré obloze': 'Clouds in a blue sky', 'Začněte tady': 'Start here', 'Pošlete odkaz.': 'Send a link.', 'Za 48 hodin': 'In 48 hours',
    'uvidíte svůj nový web.': 'you’ll see your new website.', 'Zdarma a nezávazně. Potom se sami rozhodnete, zda budete chtít pokračovat.': 'Free and with no obligation. Then you decide whether to continue.',
    'Žádné schůzky ani technické zadání': 'No meetings or technical specs', 'Konkrétní návrh, ne obecná nabídka': 'A concrete design, not a generic offer',
    'Nic nám nedlužíte, ani když nepokračujete': 'You owe us nothing, even if you don’t continue',
    'Přidejte se k Papa Pechovi, Jakubu Machalovi, Hasoběhu a dalším 38 klientům.': 'Join Papa Pech, Jakub Machala, Hasoběh and 38 other clients.',
    'Vyplnění zabere asi minutu.': 'Takes about a minute.', 'Jméno a příjmení': 'Full name', 'Jan Novák': 'Jane Smith', 'Odkaz na současný web': 'Link to your current website',
    'www.vasefirma.cz': 'www.yourcompany.com', 'Nebo pár vět o projektu': 'Or a few lines about your project', 'Čím se zabýváte a pro koho…': 'What you do and for whom…',
    'E-mail': 'Email', 'vas@email.cz': 'you@email.com', 'Telefon (nepovinné)': 'Phone (optional)',
    'Beru na vědomí, že WebHunter s.r.o. zpracuje mé údaje za účelem přípravy návrhu a odpovědi na poptávku podle': 'I acknowledge that WebHunter s.r.o. will process my data to prepare the design and reply to my enquiry in line with the',
    'zásad ochrany osobních údajů': 'privacy policy', 'Odeslat a získat návrh': 'Send and get my design', 'Díky, máme to!': 'Thanks, got it!',
    'Do 48 hodin vám pošleme návrh vašeho nového webu.': 'We’ll send you the design of your new website within 48 hours.',
    # ---------- footer ----------
    'Weby na míru pro firmy, podnikatele a organizace. Návrh zdarma do 48 hodin.': 'Custom websites for companies, entrepreneurs and organisations. Free design within 48 hours.',
    'Navigace': 'Navigation', 'Kontakt': 'Contact', 'Firma': 'Company', 'IČO: 29498511': 'Company ID: 29498511', 'IČO 29498511': 'Company ID 29498511',
    'Zásady ochrany osobních údajů': 'Privacy policy', 'Obchodní podmínky': 'Terms & conditions (CZ)', 'Blog': 'Blog (CZ)', 'Nastavení cookies': 'Cookie settings',
    # ---------- work page ----------
    'Videomakeři, fotografové, sportovní akce, farmy, e-shopy i realitní makléři. Každý web jsme navrhli pro konkrétní firmu a to, co mají její zákazníci udělat — zavolat, poptat nebo koupit.':
        'Videomakers, photographers, sports events, farms, online stores and real estate agents. We designed each website for a specific business and what its customers should do — call, enquire or buy.',
    'realizací': 'projects', 'oborů': 'industries', 'jazyky webů': 'website languages', 'Vybrané realizace': 'Selected work',
    'Dvanáct webů, na které jsme': 'Twelve websites we are', 'nejvíc hrdí.': 'proudest of.', 'Vybrané realizace ·': 'Selected work ·', 'Předchozí': 'Previous', 'Další': 'Next',
    'Videomaker': 'Videomaker', 'Osobní značka, která prodává kurzy': 'A personal brand that sells courses',
    'Režisér a influencer se 40M+ zhlédnutími pro klienty. Web spojuje osobní značku, zakázkovou produkci a e-shop s online kurzy Videomástr — v jeho vlastním, hravém tónu.':
        'A director and influencer with 40M+ views for clients. The website combines his personal brand, commissioned production and the Videomástr online course store — in his own playful voice.',
    'E-shop s kurzy': 'Course store', 'Zakázková produkce': 'Commissioned production', 'Osobní značka': 'Personal brand', 'Otevřít papapech.cz': 'Open papapech.cz',
    'Svatební fotograf': 'Wedding photographer', 'Filmová estetika na každém scrollu': 'Cinematic look on every scroll',
    'Černobílé portréty, světelná stopa, která se kreslí při scrollování, a galerie, díky které si páry fotografa vyberou dřív, než mu napíšou.':
        'Black-and-white portraits, a light trail that draws itself as you scroll, and a gallery that makes couples choose him before they even write.',
    'Animovaná světelná stopa': 'Animated light trail', 'Galerie': 'Gallery', 'Ceník a termíny': 'Prices & dates', 'Otevřít jakubmachalaphoto.cz': 'Open jakubmachalaphoto.cz',
    'Běžecký závod': 'Running race', 'Od odpočtu po výsledky': 'From countdown to results',
    'Web pro letní běžecký závod pod Karlštejnem: odpočet do startu, kategorie, harmonogram, online registrace s platbou i výsledky. Všechno na jednom místě.':
        'A website for a summer running race below Karlštejn Castle: countdown to the start, categories, schedule, online registration with payment and results. All in one place.',
    'Online registrace': 'Online registration', 'Platba startovného': 'Entry fee payment', 'Výsledky a galerie': 'Results & gallery', 'Otevřít hasobeh.cz': 'Open hasobeh.cz',
    'Pilates': 'Pilates', 'Pohyb, který tělo skutečně potřebuje': 'Movement your body really needs',
    'Lekce pilates a zdravých zad s Oľgou Königovou. Web vede k jedinému kroku — rezervaci lekce — a nabízí rozvrh, místa cvičení, členství i videa na cvičení doma.':
        'Pilates and healthy-back classes with Oľga Königová. The website leads to one step — booking a class — and offers a timetable, locations, memberships and home workout videos.',
    'Rezervace lekcí': 'Class booking', 'Rozvrh': 'Timetable', 'Členství a videa': 'Memberships & videos', 'Otevřít sport-active.cz': 'Open sport-active.cz',
    'Chov skotu': 'Cattle breeding', 'Rodinná farma, která působí světově': 'A family farm with a world-class feel',
    '150 krav a jalovic na 260 hektarech. Web staví na krajině a fotkách stáda, představí tři plemena — Charolais, Parthenais a Limousine — a vede k prodeji plemenných býků.':
        '150 cows and heifers on 260 hectares. The website builds on the landscape and photos of the herd, presents three breeds — Charolais, Parthenais and Limousine — and leads to breeding bull sales.',
    'Býci na prodej': 'Bulls for sale', '3 plemena': '3 breeds', 'Galerie farmy': 'Farm gallery', 'Otevřít charolais.cz': 'Open charolais.cz',
    'E-shop': 'Online store', 'Největší bazar kancelářského nábytku': 'The largest used office furniture store',
    'E-shop s použitým nábytkem světových značek jako Steelcase nebo Kinnarps. Katalog v kategoriích, košík, ceny v korunách i eurech a k tomu výkup a pronájem nábytku.':
        'An online store for used furniture from global brands such as Steelcase and Kinnarps. Categorised catalogue, cart, prices in CZK and EUR, plus furniture buy-back and rental.',
    'E-shop s košíkem': 'Store with cart', 'Česky, slovensky, anglicky': 'Czech, Slovak, English', 'Výkup a pronájem': 'Buy-back & rental', 'Otevřít bekabazar.cz': 'Open bekabazar.cz',
    'Prodej nemovitosti': 'Property sale', 'Jedna nemovitost, vlastní web': 'One property, its own website',
    'Dům za 20,99 mil. Kč dostal šest kapitol — dům, technologie, zahradu, půdorysy, lokalitu a 66 fotografií. Na každé stránce je po ruce tlačítko pro domluvení prohlídky.':
        'A CZK 20.99M house got six chapters — the house, technology, garden, floor plans, location and 66 photos. A button to book a viewing is on every page.',
    'Web pro 1 nemovitost': 'Single-property website', '66 fotografií': '66 photos', 'Půdorysy a lokalita': 'Floor plans & location', 'Otevřít ratiborska.jandemelreality.cz': 'Open ratiborska.jandemelreality.cz',
    'Kovářství': 'Blacksmith', 'Žár výhně i na webu': 'The heat of the forge, online',
    'Žádná sériová výroba — a web tomu odpovídá. Tmavá dílna, oheň a galerie kusů, které lidem doma slouží. Každá sekce vede k jedinému cíli: poptat výrobu.':
        'No mass production — and the website shows it. A dark workshop, fire and a gallery of pieces that serve people at home. Every section leads to one goal: ordering a piece.',
    'Galerie výrobků': 'Product gallery', 'Poptávka výroby': 'Custom orders', 'Dílna od roku 2011': 'Workshop since 2011', 'Otevřít kovotuk.cz': 'Open kovotuk.cz',
    'Dámská móda': 'Women’s fashion', 'Elegance bez kompromisů': 'Elegance without compromise',
    'Rodinná firma s téměř dvacetiletou tradicí a čtyřmi prodejnami v Praze. Web stojí na silné fotografii a redakčním layoutu, aby zákaznice hned věděly, kam si pro nový kousek dojít.':
        'A family business with almost twenty years of tradition and four stores in Prague. The website relies on strong photography and an editorial layout, so customers instantly know where to find their next piece.',
    'Redakční design': 'Editorial design', '4 prodejny': '4 stores', 'Příběh značky': 'Brand story', 'Otevřít f-fashion.cz': 'Open f-fashion.cz',
    'Výhradní distributor Goti': 'Exclusive Goti distributor', 'Řemeslo, které se nedá uspěchat': 'Craft that can’t be rushed',
    'Ručně vyráběné pece z Florencie od roku 1973. Web vypráví, jak pec vzniká během pěti dní v ohni, představí dvanáct modelů a dovede k nezávazné poptávce.':
        'Handmade ovens from Florence since 1973. The website tells how an oven is made over five days in the fire, presents twelve models and leads to a no-obligation enquiry.',
    'Katalog 12 modelů': '12-model catalogue', 'Příběh výroby': 'Making-of story', 'Galerie instalací': 'Installation gallery', 'Otevřít pecezitalie.cz': 'Open pecezitalie.cz',
    'Ubytování': 'Accommodation', 'Dovolená začíná už na webu': 'The holiday starts on the website',
    'Rodinný penzion v Horní Tříči u Vysokého nad Jizerou. Letecký záběr, wellness, pokoje a ceník přehledně na jednom místě — a tlačítko Zarezervovat pobyt je vždy po ruce. Česky i německy.':
        'A family guesthouse in Horní Tříč near Vysoké nad Jizerou. Aerial footage, wellness, rooms and prices in one place — and the Book a stay button is always at hand. In Czech and German.',
    'Rezervace pobytu': 'Stay booking', 'Wellness a okolí': 'Wellness & surroundings', 'Česky i německy': 'Czech & German', 'Otevřít pension-maty.cz': 'Open pension-maty.cz',
    'Charitativní platforma': 'Charity platform', 'Pomoc, která drží palce oběma stranám': 'Help that keeps its fingers crossed for both sides',
    'Podporovatel si vybere ambasadora — sportovce nebo umělce — a měsíčním příspěvkem pomáhá dětem s onkologickým onemocněním a mladým lidem na vozíčku. Princip web vysvětlí ve třech krocích.':
        'Supporters choose an ambassador — an athlete or artist — and with a monthly donation help children with cancer and young wheelchair users. The website explains it in three steps.',
    'Výběr ambasadora': 'Choosing an ambassador', 'Měsíční příspěvek': 'Monthly donation', 'Transparentní dopad': 'Transparent impact', 'Otevřít drzimetipalce.cz': 'Open drzimetipalce.cz',
    'Živý web': 'Live website', 'Najeďte pro pauzu': 'Hover to pause', 'Mobilní verze webu Papa Pech': 'Mobile version of the Papa Pech website',
    'Všech 41 realizací.': 'All 41 projects.', 'Najeďte a projeďte si je.': 'Hover and scroll through them.',
    'Reality a bydlení': 'Real estate & housing', 'Řemesla a firmy': 'Trades & companies', 'Obchod a e-shopy': 'Retail & online stores', 'Zdraví a péče': 'Health & care',
    'Byznys a finance': 'Business & finance', 'Zážitky, kreativa a komunity': 'Experiences, creative & communities', 'Vybraná': 'Featured', 'Vše': 'All',
    'Režisér a videomaker. Osobní značka, zakázková produkce a e-shop s online kurzy.': 'Director and videomaker. Personal brand, commissioned production and an online course store.',
    'Svatební a portrétní fotograf. Filmová estetika a světelná stopa, která se kreslí při scrollování.': 'Wedding and portrait photographer. A cinematic look and a light trail drawn as you scroll.',
    'Letní běžecký závod pod Karlštejnem. Odpočet do startu, online registrace s platbou a výsledky.': 'A summer running race below Karlštejn. Countdown, online registration with payment and results.',
    'Pilates a zdravá záda v Bystřici nad Pernštejnem. Rozvrh lekcí, rezervace a cvičení doma.': 'Pilates and healthy back classes in Bystřice nad Pernštejnem. Timetable, booking and home workouts.',
    'Rodinná farma v jižních Čechách. Chov plemenného skotu, býci na prodej a život na 260 hektarech.': 'A family farm in South Bohemia. Pedigree cattle breeding, bulls for sale and life on 260 hectares.',
    'E-shop největšího bazaru kancelářského nábytku v ČR a SR včetně výkupu a pronájmu.': 'Online store of the largest used office furniture dealer in Czechia and Slovakia, incl. buy-back and rental.',
    'Prodejní web pro jeden rodinný dům: šest kapitol, půdorysy, lokalita a 66 fotografií.': 'A sales website for one family house: six chapters, floor plans, location and 66 photos.',
    'Kovářská dílna z Bruntálska. Galerie ručně kovaných kusů a poptávka výroby.': 'A blacksmith workshop from the Bruntál region. Gallery of hand-forged pieces and custom orders.',
    'Elegantní dámská móda s téměř dvacetiletou tradicí a čtyřmi prodejnami v Praze.': 'Elegant women’s fashion with almost twenty years of tradition and four stores in Prague.',
    'Výhradní distributor ručně vyráběných pecí Goti z Florencie. Katalog 12 modelů a poptávka.': 'Exclusive distributor of handmade Goti ovens from Florence. 12-model catalogue and enquiries.',
    'Rodinný penzion v Krkonoších s wellness, ceníkem a rezervací pobytu. Česky i německy.': 'A family guesthouse in the Giant Mountains with wellness, prices and booking. In Czech and German.',
    'Charitativní platforma: vyberte si ambasadora a podpořte děti s onkologickým onemocněním.': 'Charity platform: choose an ambassador and support children with cancer.',
    'Prémiové reality v Praze od roku 1997. Nabídka nemovitostí, služby a osobní přístup makléře.': 'Premium real estate in Prague since 1997. Listings, services and a personal approach.',
    'Kosmetické studio ve Žďáře nad Sázavou. Ošetření, přístroje, ceník a reálné výsledky klientek.': 'A beauty studio in Žďár nad Sázavou. Treatments, devices, prices and real client results.',
    'Elektroinstalace pro firmy i domácnosti. Přehled služeb, vybrané realizace a nezávazná poptávka.': 'Electrical installations for businesses and homes. Services, selected projects and enquiries.',
    'Investiční holding a ekosystém pěti pilířů. Složitá struktura převedená do srozumitelného příběhu.': 'An investment holding and five-pillar ecosystem. A complex structure turned into a clear story.',
    'Jediný cirkusový band v Česku. Neonový svět, koncerty a show pro děti — ve třech jazycích.': 'The only circus band in Czechia. A neon world, concerts and kids’ shows — in three languages.',
    'Zámečnické a svařovací práce po celé ČR i Evropě. Česky, anglicky a německy.': 'Metalwork and welding across Czechia and Europe. In Czech, English and German.',
    'Dovoz prověřených vozů z Německa. Auta skladem i dovoz na objednávku ve čtyřech krocích.': 'Imports of verified cars from Germany. Cars in stock and made-to-order imports in four steps.',
    'Správa pronájmu bytů s kalkulačkou výnosu hned pod úvodem a garancí nájmu až 600 000 Kč.': 'Rental property management with a yield calculator right below the hero and a rent guarantee of up to CZK 600,000.',
    'Anglický web pro enterprise zákaznickou podporu s živými metrikami a jasnou nabídkou služeb.': 'An English website for enterprise customer support with live metrics and a clear service offer.',
    'Kamionová spedice mezi Evropou a Asií od roku 1993. Poptávka přepravy vyplněná za 30 sekund.': 'Truck freight forwarding between Europe and Asia since 1993. A transport quote request in 30 seconds.',
    'Volební web koalice pro komunální volby 2026. Program, kandidáti a aktuality z kampaně.': 'An election website for a coalition in the 2026 municipal elections. Programme, candidates and campaign news.',
    'Galerie a e-shop energetických obrazů, reprodukcí a obrazů na přání. Česky i anglicky.': 'A gallery and store of energy paintings, prints and commissions. In Czech and English.',
    'Servis osobních i nákladních vozidel v Kladně a Praze. Více než 14 značek pod jednou střechou.': 'Car and truck service in Kladno and Prague. Over 14 brands under one roof.',
    'Psychoterapeut pro jednotlivce, páry i rodiny. Klidný web s ceníkem a online rezervací.': 'A psychotherapist for individuals, couples and families. A calm website with prices and online booking.',
    'Osobní web realitního poradce. Nabídka, služby a reference na jednom místě.': 'A real estate adviser’s personal website. Listings, services and references in one place.',
    'Nezávislý finanční poradce. Rozcestník podle typu klienta, orientační kalkulačky a reference.': 'An independent financial adviser. Paths by client type, calculators and references.',
    'Rozcestník realitní kanceláře: reality, odhady a hypotéky na jednom místě.': 'A real estate agency hub: properties, valuations and mortgages in one place.',
    'Kampaňová stránka pro diskrétní prodej nemovitostí v Týništi — bez veřejné inzerce.': 'A campaign page for discreet property sales in Týniště — without public listings.',
    'Poradenství při rozvodu a péči o děti. Důvěryhodný web s jasným postupem spolupráce.': 'Counselling on divorce and childcare. A trustworthy website with a clear process.',
    'Výkonnostní marketing pro e-shopy. Výsledky klientů, případové studie a audit zdarma.': 'Performance marketing for online stores. Client results, case studies and a free audit.',
    'Zámečnická pohotovost Kladno 24/7. Web postavený na jediném cíli — aby lidé hned zavolali.': '24/7 locksmith emergency service in Kladno. A website built for one goal — an immediate call.',
    'Rodinná firma pro správu nemovitostí a vedení účetnictví domů a SVJ.': 'A family company for property management and accounting for buildings and owners’ associations.',
    'Členský portál bytového družstva v Neratovicích. Aktuality, schůze, dokumenty a hlášení závad.': 'A members’ portal for a housing cooperative in Neratovice. News, meetings, documents and fault reports.',
    'Anglická soutěž pro řešitele těžkých problémů s žebříčkem a hlavní cenou v San Franciscu.': 'An English-language competition for hard-problem solvers with a leaderboard and a grand prize in San Francisco.',
    'Místní pošta v Havířově. Služby, otevírací doba a cesta k nově otevřené pobočce.': 'A local post office in Havířov. Services, opening hours and directions to the new branch.',
    'E-shop s rozvozem pramenité vody v barelech, výdejníky a servisem pro firmy i domácnosti.': 'An online store delivering spring water in bottles, with dispensers and service for businesses and homes.',
    'Byt Vršovická': 'Vršovická Apartment',
    'Prodejní web pro jeden byt 3+1 v Praze 10. Galerie, videoprohlídka a orientační splátka hypotéky.': 'A sales website for one 3-bedroom flat in Prague 10. Gallery, video tour and an estimated mortgage payment.',
    'Nezávislá produkce comedy formátů. Výsledky, tři vlastní formáty a nabídka spolupráce pro značky.': 'Independent comedy production. Results, three original formats and partnerships for brands.',
    'Privátní klub majitelů firem a investorů. Co členství řeší, jak funguje vstup a přihláška do klubu.': 'A private club for business owners and investors. What membership offers, how joining works and the application.',
    'Zobrazit všech 41 realizací': 'Show all 41 projects', 'Váš web může být další': 'Your website could be next', 'Návrh zdarma.': 'Free design.', 'Do 48 hodin.': 'Within 48 hours.',
    'Pošlete odkaz na současný web nebo pár vět o firmě. Potom se sami rozhodnete, zda budete chtít pokračovat.': 'Send a link to your current website or a few lines about your business. Then you decide whether to continue.',
    # ---------- privacy ----------
    'Ochrana osobních údajů': 'Privacy policy', 'a cookies': 'and cookies', 'Platnost od 24. 9. 2026 · WebHunter s.r.o., IČO 29498511': 'Effective from 24 September 2026 · WebHunter s.r.o., Company ID 29498511',
    'Obsah': 'Contents', '1. Správce': '1. Controller', '2. Jaké údaje': '2. What data', '3. Účely a právní základ': '3. Purposes and legal basis', '4. Doba uložení': '4. Retention',
    '5. Příjemci a zpracovatelé': '5. Recipients and processors', '6. Vaše práva': '6. Your rights', '7. Cookies': '7. Cookies', '8. Změny': '8. Changes',
    '1. Správce osobních údajů': '1. Data controller', 'Správcem je': 'The controller is',
    ', IČO 29498511, se sídlem v Praze, Česká republika. Ve věcech ochrany osobních údajů nás kontaktujte na': ', Company ID 29498511, based in Prague, Czech Republic. For data protection matters, contact us at',
    'nebo na telefonu': 'or by phone at', '. Na oblast GDPR spolupracujeme s odborníky z': '. For GDPR matters we work with the experts at',
    '2. Jaké osobní údaje zpracováváme': '2. What personal data we process',
    'jméno, příjmení, e-mail a telefon z kontaktního formuláře,': 'name, surname, email and phone number from the contact form,',
    'odkaz na váš současný web, název firmy a obsah zprávy, kterou nám pošlete,': 'the link to your current website, company name and the content of your message,',
    'technické údaje nutné pro provoz a bezpečnost webu (například IP adresa a typ prohlížeče v záznamech poskytovatele hostingu),': 'technical data needed to run and secure the website (e.g. IP address and browser type in the hosting provider’s logs),',
    'údaje o návštěvnosti (navštívené stránky, zdroj návštěvy, typ zařízení, doba a hloubka procházení, kliknutí na prvky webu) — pouze s vaším souhlasem s analytickými cookies,':
        'visit data (pages visited, traffic source, device type, time on site and scroll depth, clicks on page elements) — only with your consent to analytics cookies,',
    'údaje pro měření reklam na Facebooku a Instagramu (Meta Pixel) — pouze s vaším souhlasem s marketingovými cookies.': 'data for measuring ads on Facebook and Instagram (Meta Pixel) — only with your consent to marketing cookies.',
    'Údaje o návštěvnosti nepropojujeme s vaším jménem ani e-mailem a nepoužíváme je k automatizovanému rozhodování.': 'We do not link visit data to your name or email and do not use it for automated decision-making.',
    '3. Účely a právní základ zpracování': '3. Purposes and legal basis of processing', 'Účel': 'Purpose', 'Právní základ': 'Legal basis',
    'Příprava návrhu webu a odpověď na vaši poptávku': 'Preparing a website design and replying to your enquiry',
    'Opatření před uzavřením smlouvy na vaši žádost (čl. 6 odst. 1 písm. b) GDPR)': 'Pre-contractual steps at your request (Art. 6(1)(b) GDPR)',
    'Realizace a fakturace zakázky': 'Delivering and invoicing the project', 'Plnění smlouvy a právních povinností (čl. 6 odst. 1 písm. b) a c) GDPR)': 'Performance of a contract and legal obligations (Art. 6(1)(b) and (c) GDPR)',
    'Provoz a zabezpečení webu': 'Running and securing the website', 'Oprávněný zájem (čl. 6 odst. 1 písm. f) GDPR)': 'Legitimate interest (Art. 6(1)(f) GDPR)',
    'Statistika návštěvnosti a zlepšování webu': 'Visit statistics and improving the website', 'Váš souhlas (čl. 6 odst. 1 písm. a) GDPR)': 'Your consent (Art. 6(1)(a) GDPR)',
    'Měření a cílení reklam (Meta Pixel)': 'Ad measurement and targeting (Meta Pixel)', '4. Jak dlouho údaje uchováváme': '4. How long we keep data',
    'Údaje z poptávkových formulářů uchováváme po dobu nezbytnou k vyřízení poptávky, nejdéle 2 roky od posledního kontaktu. Pokud uzavřeme smlouvu, uchováváme údaje po dobu jejího trvání a poté po dobu stanovenou právními předpisy. Údaje ze statistiky návštěvnosti a cookies uchováváme po dobu platnosti vašeho souhlasu, nejdéle 13 měsíců.':
        'We keep enquiry form data for as long as needed to handle the enquiry, at most 2 years from the last contact. If we sign a contract, we keep data for its duration and then for the period required by law. We keep visit statistics and cookie data while your consent is valid, at most 13 months.',
    '5. Komu údaje předáváme': '5. Who we share data with',
    'Údaje předáváme pouze prověřeným zpracovatelům, kteří nám pomáhají s provozem webu:': 'We only share data with vetted processors who help us run the website:',
    '— aplikační platforma, na které běží databáze poptávek, odesílání formulářů a statistika návštěvnosti,': '— the application platform running the enquiry database, form submissions and visit statistics,',
    '— hosting webových stránek,': '— website hosting,', '— měření reklam, pouze s vaším souhlasem s marketingovými cookies,': '— ad measurement, only with your consent to marketing cookies,',
    'poskytovatel e-mailových služeb, přes kterého s vámi komunikujeme.': 'the email provider we use to communicate with you.',
    'Někteří z těchto poskytovatelů mohou údaje zpracovávat i mimo Evropskou unii. V takovém případě se tak děje na základě standardních smluvních doložek schválených Evropskou komisí nebo rámce EU-US Data Privacy Framework. Písma na webu hostujeme sami, při návštěvě proto nepředáváme vaši IP adresu společnosti Google.':
        'Some of these providers may process data outside the European Union. In that case, this is based on standard contractual clauses approved by the European Commission or the EU-US Data Privacy Framework. We host the website fonts ourselves, so your IP address is not passed to Google when you visit.',
    '6. Jaká máte práva': '6. Your rights', 'Máte právo:': 'You have the right to:', 'vyžádat si přístup ke svým osobním údajům,': 'request access to your personal data,',
    'požadovat opravu nesprávných údajů,': 'request correction of inaccurate data,', 'požadovat výmaz údajů („právo být zapomenut“),': 'request erasure of your data (“right to be forgotten”),',
    'požadovat omezení zpracování,': 'request restriction of processing,', 'vznést námitku proti zpracování založenému na oprávněném zájmu,': 'object to processing based on legitimate interest,',
    'požadovat přenositelnost údajů,': 'request data portability,', 'kdykoli odvolat souhlas — odvolání nemá vliv na zpracování před ním,': 'withdraw your consent at any time — this does not affect processing before withdrawal,',
    'podat stížnost u Úřadu pro ochranu osobních údajů (': 'lodge a complaint with the Czech Office for Personal Data Protection (',
    'Svá práva uplatníte na e-mailu': 'To exercise your rights, email', '. Odpovíme nejpozději do jednoho měsíce.': '. We will reply within one month at the latest.',
    '7. Cookies a podobné technologie': '7. Cookies and similar technologies',
    'Nezbytné cookies a úložiště zajišťují základní fungování webu a nevyžadují souhlas. Analytické a marketingové spouštíme až po vašem souhlasu v cookies liště. Souhlas můžete kdykoli změnit nebo odvolat tlačítkem níže nebo odkazem „Nastavení cookies“ v patičce webu.':
        'Necessary cookies and storage keep the website running and do not require consent. We only enable analytics and marketing cookies after you consent in the cookie banner. You can change or withdraw your consent at any time with the button below or the “Cookie settings” link in the footer.',
    'Změnit nastavení cookies': 'Change cookie settings', 'Název': 'Name', 'Kategorie': 'Category', 'Platnost': 'Expiry',
    'Uložení vaší volby v cookies liště': 'Stores your cookie banner choice', 'do odvolání, nejdéle 12 měsíců': 'until withdrawn, at most 12 months',
    'Rozlišení jedné návštěvy (relace)': 'Identifies a single visit (session)', 'do zavření prohlížeče': 'until the browser is closed',
    'Anonymní rozlišení nového a vracejícího se návštěvníka': 'Anonymously distinguishes new and returning visitors', '13 měsíců': '13 months',
    'Marketingové': 'Marketing', 'Meta Pixel — měření a cílení reklam': 'Meta Pixel — ad measurement and targeting', '3 měsíce': '3 months',
    '8. Změny těchto zásad': '8. Changes to this policy', 'Tyto zásady můžeme aktualizovat. Aktuální znění je vždy k dispozici na této stránce.': 'We may update this policy. The current version is always available on this page.',
}
