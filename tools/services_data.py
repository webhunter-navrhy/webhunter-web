# -*- coding: utf-8 -*-
"""Content of the service subpages (/sluzby/<slug>/). Edit texts here, then run: python3 tools/gen_pages.py"""

SERVICES = [
  {
    'slug': 'tvorba-webu',
    'nav': 'Tvorba webu na míru',
    'title': 'Tvorba webových stránek na míru, návrh zdarma | WebHunter',
    'desc': 'Tvorba webových stránek na míru pro firmy a podnikatele. Návrh nového webu zdarma do 48 hodin, moderní design, SEO, GEO a GDPR v ceně. Nejdřív uvidíte, pak se rozhodnete.',
    'label': 'Tvorba webu',
    'h1': 'Tvorba webových stránek <span class="serif">na míru.</span>',
    'lead': 'Navrhneme a postavíme web, který vypadá skvěle a hlavně přivádí poptávky. Návrh vašeho nového webu máte zdarma do 48 hodin — ještě než cokoli podepíšete.',
    'obj': 'cursor',
    'answer': 'WebHunter je česká webová agentura, která tvoří webové stránky na míru pro firmy, podnikatele a organizace. Každý klient dostane nejdřív zdarma a nezávazně konkrétní návrh nového webu do 48 hodin. Teprve potom se rozhodne, jestli chce pokračovat v realizaci.',
    'benefits': [
      ('bnv-blue', 'stopwatch', 'Návrh do 48 hodin', 'Pošlete odkaz nebo pár vět o firmě. Do dvou dnů máte hotový návrh, ne prezentaci.'),
      ('bnv-sky', 'cursor', 'Design, který prodává', 'Každou sekci stavíme k jedinému cíli: aby návštěvník zavolal, poptal nebo koupil.'),
      ('bnv-lime', 'magnifier', 'SEO a GEO v základu', 'Web připravíme tak, aby vás našel Google i ChatGPT, Perplexity nebo Gemini.'),
      ('bnv-dark', 'shield', 'GDPR bez starostí', 'Cookies, souhlasy a osobní údaje nastavené s odborníky z Compliance Partner.'),
    ],
    'sections': [
      ('Co je v tvorbě webu zahrnuto', [
        'Každý web navrhujeme od nuly pro konkrétní firmu. Žádné šablony, žádné kompromisy v designu. Postaráme se o strukturu stránek, texty, fotografie, technické řešení i napojení na formuláře, rezervace nebo e-shop.',
        ['Návrh designu na míru a jeho úpravy podle vás', 'Texty psané tak, aby přesvědčily zákazníka', 'Responzivní web pro mobily, tablety i počítače', 'Rychlé načítání a moderní, bezpečné technologie', 'Základní SEO, GEO a strukturovaná data', 'Cookie lišta a zásady ochrany osobních údajů', 'Napojení na analytiku, Meta Pixel a formuláře'],
      ]),
      ('Pro koho weby děláme', [
        'Pro firmy, řemeslníky, poradce, realitní makléře, ubytování, sportovní akce, farmy, e-shopy i investiční kluby. Máme za sebou přes 40 realizací z nejrůznějších oborů — od kovářské dílny po privátní business klub.',
      ]),
      ('Kolik stojí tvorba webu', [
        'Cena záleží na rozsahu webu a funkcích, které potřebujete. Přesnou částku znáte vždy předem — ještě než se rozhodnete pokračovat. Návrh je zdarma a k ničemu vás nezavazuje.',
      ]),
    ],
    'work': ['papapech-cz', 'jakubmachalaphoto-cz', 'charolais-cz'],
    'faq': [
      ('Jak dlouho trvá tvorba webu?', 'Návrh máte do 48 hodin. Samotná realizace menšího firemního webu obvykle trvá 1 až 3 týdny podle rozsahu a toho, jak rychle se domluvíme na podkladech.'),
      ('Musím dodat texty a fotky?', 'Nemusíte. Texty vám rádi napíšeme a fotky můžeme zajistit nebo použít ty, které už máte. Stačí nám odkaz na současný web nebo pár vět o firmě.'),
      ('Budu si moct web sám upravovat?', 'Ano, pokud o to stojíte, připravíme web tak, abyste si jednoduše upravili texty, fotky nebo novinky. Změny za vás ale rádi uděláme i my.'),
      ('Co když se mi návrh nebude líbit?', 'Pak nemusíte pokračovat a nic nám nedlužíte. Nebo nám řeknete, co by mělo být jinak, a návrh upravíme.'),
    ],
  },
  {
    'slug': 'redesign-webu',
    'nav': 'Redesign webu',
    'title': 'Redesign webu — modernizace webu, návrh zdarma | WebHunter',
    'desc': 'Redesign a modernizace zastaralého webu. Podívejte se na skutečné weby našich klientů předtím a teď. Návrh nového vzhledu zdarma do 48 hodin.',
    'label': 'Redesign webu',
    'h1': 'Redesign webu. <span class="serif">Ze starého nový.</span>',
    'lead': 'Máte web, za který se trochu stydíte? Pošlete nám na něj odkaz. Do 48 hodin uvidíte, jak by mohl vypadat, a na mobilu fungovat úplně jinak.',
    'obj': 'spark',
    'answer': 'Redesign webu je kompletní modernizace vzhledu, textů a technologie stávajícího webu. WebHunter připraví zdarma návrh nové podoby vašeho webu do 48 hodin — stačí poslat odkaz na současný web. Obsah, který funguje, zachováme a vylepšíme.',
    'benefits': [
      ('bnv-blue', 'spark', 'Moderní vzhled', 'Web, který působí důvěryhodně a odpovídá tomu, jak kvalitní služby nabízíte.'),
      ('bnv-sky', 'cursor', 'Víc poptávek', 'Jasné sdělení, výrazné výzvy k akci a formuláře, které se dají vyplnit za minutu.'),
      ('bnv-lime', 'bolt', 'Rychlost a mobil', 'Většina lidí přichází z telefonu. Nový web se načte rychle a na mobilu vypadá skvěle.'),
      ('bnv-dark', 'magnifier', 'Zachované SEO', 'Staré adresy přesměrujeme, aby web o pozice ve vyhledávání nepřišel.'),
    ],
    'ba': True,
    'sections': [
      ('Kdy je čas na redesign', [
        'Pokud je web starší než pět let, na mobilu se špatně ovládá, pomalu se načítá nebo z něj nechodí poptávky, je čas na změnu. Zastaralý web odrazuje zákazníky dřív, než si přečtou, co nabízíte.',
        ['Web nevypadá dobře na mobilu', 'Z webu nechodí poptávky ani telefonáty', 'Design neodpovídá kvalitě vašich služeb', 'Web se pomalu načítá', 'Chybí cookie lišta a zásady GDPR', 'Informace na webu jsou zastaralé'],
      ]),
      ('Jak redesign probíhá', [
        'Projdeme váš současný web, zachováme to, co funguje, a navrhneme novou strukturu, texty i vzhled. Po schválení web postavíme, přesměrujeme staré adresy a spustíme ho bez výpadku.',
      ]),
    ],
    'work': ['realitynekvinda-cz', 'alissabeaute-ks-cz', 'obrazy-z-nitra-cz'],
    'faq': [
      ('Přijdu redesignem o pozice ve vyhledávání?', 'Ne. Staré adresy přesměrujeme na nové stránky a zachováme obsah, který Google zná. Nový web bývá rychlejší a lépe strukturovaný, což pozicím pomáhá.'),
      ('Můžu si nechat logo a barvy?', 'Samozřejmě. Pokud máte zavedenou značku, navrhneme nový web v jejím duchu. Pokud chcete, pomůžeme vám značku i osvěžit.'),
      ('Kolik stojí redesign webu?', 'Záleží na rozsahu a funkcích. Cenu znáte vždy předem, ještě než se rozhodnete pokračovat. Návrh nové podoby je zdarma.'),
    ],
  },
  {
    'slug': 'eshopy',
    'nav': 'Tvorba e-shopů',
    'title': 'Tvorba e-shopu na míru — prodej a rezervace | WebHunter',
    'desc': 'Tvorba e-shopů a webů s prodejem, rezervacemi, registracemi a online kurzy. Moderní design, rychlost a platby. Návrh zdarma do 48 hodin.',
    'label': 'E-shopy a prodej',
    'h1': 'E-shopy, které <span class="serif">opravdu prodávají.</span>',
    'lead': 'Katalog, košík, platby, rezervace, registrace na akce nebo prodej online kurzů. Postavíme vám web, přes který se dá rovnou nakoupit.',
    'obj': 'coin',
    'answer': 'WebHunter tvoří e-shopy a weby s online prodejem na míru: katalog produktů, košík a platby, rezervace termínů, registrace na akce s platbou startovného nebo prodej online kurzů. Návrh e-shopu je zdarma do 48 hodin.',
    'benefits': [
      ('bnv-lime', 'coin', 'Prodej a platby', 'Košík, platby kartou a přehledné objednávky. Nakupování bez zbytečných kroků.'),
      ('bnv-blue', 'stopwatch', 'Rezervace a registrace', 'Rezervace lekcí, termínů nebo registrace na závody s platbou startovného.'),
      ('bnv-sky', 'spark', 'Online kurzy', 'Prodej kurzů a digitálních produktů vedle vašich ostatních služeb.'),
      ('bnv-dark', 'shield', 'Obchodní podmínky a GDPR', 'Vše, co e-shop podle zákona potřebuje, nastavíme s odborníky.'),
    ],
    'sections': [
      ('Co vám postavíme', [
        'Od menšího e-shopu s pár produkty po katalog stovek položek. Vždy s důrazem na to, aby zákazník rychle našel, co hledá, a nákup dokončil.',
        ['E-shop s katalogem, filtry a košíkem', 'Platby kartou a převodem', 'Rezervační systém pro služby a lekce', 'Registrace na akce s online platbou', 'Prodej online kurzů a členství', 'Napojení na e-mailing a Meta Pixel'],
      ]),
      ('Weby, na kterých už se prodává', [
        'Beka Bazar prodává kancelářský nábytek v korunách i eurech, AQUAcoolers rozváží vodu po celé republice, Papa Pech prodává online kurzy a Hasoběh vybírá startovné online. Podívejte se na ně níže.',
      ]),
    ],
    'work': ['bekabazar-cz', 'papapech-cz', 'hasobeh-cz'],
    'faq': [
      ('Na jaké platformě e-shop stavíte?', 'Vybíráme podle rozsahu a vašich potřeb — od lehkého řešení pro pár produktů po plnohodnotný e-shop. Vždy tak, aby byl rychlý a snadno se spravoval.'),
      ('Umíte napojit platby?', 'Ano. Nastavíme platby kartou, převodem i další metody a napojíme potvrzovací e-maily.'),
      ('Pomůžete s obchodními podmínkami?', 'Ano. Obchodní podmínky, zásady ochrany osobních údajů i cookies řešíme s odborníky z Compliance Partner.'),
    ],
  },
  {
    'slug': 'seo',
    'nav': 'SEO optimalizace',
    'title': 'SEO optimalizace webu — buďte vidět na Googlu | WebHunter',
    'desc': 'SEO optimalizace webových stránek: technické SEO, struktura, texty, rychlost a strukturovaná data. Web, kterému Google rozumí a zákazníci ho najdou.',
    'label': 'SEO',
    'h1': 'SEO, aby vás zákazníci <span class="serif">našli první.</span>',
    'lead': 'Nejhezčí web je k ničemu, když ho nikdo nenajde. Stavíme weby tak, aby jim Google rozuměl od prvního dne — technicky čisté, rychlé a se správnou strukturou.',
    'obj': 'magnifier',
    'answer': 'SEO (optimalizace pro vyhledávače) je souhrn úprav, díky kterým web lépe rozumí Google a Seznam a zobrazí ho výš ve výsledcích hledání. WebHunter řeší SEO už při tvorbě webu: technickou čistotu, rychlost, strukturu stránek, texty a strukturovaná data.',
    'benefits': [
      ('bnv-sky', 'magnifier', 'Technické SEO', 'Čistý kód, správné nadpisy, sitemap, přesměrování a indexace bez chyb.'),
      ('bnv-lime', 'bolt', 'Rychlost webu', 'Rychlý web má lepší pozice i víc zákazníků. Optimalizujeme obrázky i kód.'),
      ('bnv-blue', 'cursor', 'Texty pro lidi i Google', 'Obsah, který odpovídá na otázky zákazníků a obsahuje slova, která hledají.'),
      ('bnv-dark', 'spark', 'Strukturovaná data', 'Informace o firmě, službách a FAQ pro bohatší výsledky ve vyhledávání.'),
    ],
    'sections': [
      ('Co SEO zahrnuje', [
        'Každý web, který postavíme, má SEO v základu. Pro firmy, které chtějí růst, nabízíme i dlouhodobou práci na obsahu a pozicích.',
        ['Analýza klíčových slov vašeho oboru', 'Struktura stránek podle toho, co lidé hledají', 'Technická optimalizace a rychlost', 'Meta titulky a popisky pro každou stránku', 'Strukturovaná data (Schema.org)', 'Registrace do Google Search Console a Seznam Webmaster', 'Lokální SEO a Google profil firmy'],
      ]),
      ('SEO a GEO jdou ruku v ruce', [
        'Stále víc lidí hledá přes umělou inteligenci. Proto každý web připravujeme i pro AI vyhledávání — podívejte se na <a href="sluzby/geo/" class="link-u">GEO optimalizaci</a>.',
      ]),
    ],
    'work': ['sport-active-cz', 'jt-auto-cz', 'rkvitkadlec-cz'],
    'faq': [
      ('Jak rychle se projeví výsledky SEO?', 'Technické SEO se projeví během několika týdnů po indexaci. Pozice u konkurenčních slov se budují měsíce. Přesné pozice nikdo zaručit nemůže — kdo to slibuje, nemluví pravdu.'),
      ('Je SEO součástí každého webu?', 'Ano. Technické SEO, rychlost, strukturu a strukturovaná data řešíme u každého webu v základu.'),
      ('Řešíte i Seznam?', 'Ano. V Česku hledá část lidí přes Seznam, proto web registrujeme i do Seznam Webmaster.'),
    ],
  },
  {
    'slug': 'geo',
    'nav': 'GEO — AI vyhledávání',
    'title': 'GEO optimalizace pro ChatGPT a AI vyhledávání | WebHunter',
    'desc': 'GEO (Generative Engine Optimization) je optimalizace webu pro AI vyhledávání. Připravíme web tak, aby mu rozuměl ChatGPT, Perplexity, Gemini i Google AI a doporučoval vaši firmu.',
    'label': 'GEO · AI vyhledávání',
    'h1': 'GEO. Aby vás doporučila <span class="serif">i umělá inteligence.</span>',
    'lead': 'Zákazníci se stále častěji ptají ChatGPT nebo Gemini, koho si mají vybrat. Připravíme váš web tak, aby mu AI rozuměla a mohla vás doporučit.',
    'obj': 'bubble',
    'answer': 'GEO (Generative Engine Optimization) je optimalizace webu pro vyhledávání pomocí umělé inteligence, jako je ChatGPT, Perplexity, Gemini nebo Google AI Overviews. Cílem je, aby AI správně pochopila, co firma dělá, pro koho a kde, a mohla ji citovat a doporučit.',
    'benefits': [
      ('bnv-dark', 'bubble', 'Jasné odpovědi', 'Obsah psaný tak, aby z něj AI snadno vytáhla přesnou odpověď a citovala vás.'),
      ('bnv-blue', 'spark', 'Strukturovaná data', 'Fakta o firmě, službách, cenách a oblasti působení ve strojově čitelné podobě.'),
      ('bnv-lime', 'magnifier', 'Přístup pro AI roboty', 'Soubory llms.txt a robots.txt, které AI vyhledávačům usnadní čtení webu.'),
      ('bnv-sky', 'shield', 'Důvěryhodnost', 'Reference, kontakty a konkrétní informace, podle kterých AI hodnotí zdroje.'),
    ],
    'sections': [
      ('Jak se GEO liší od SEO', [
        'SEO pomáhá, aby se web zobrazil ve výsledcích Googlu. GEO pomáhá, aby ho AI asistenti použili jako zdroj a vaši firmu přímo doporučili v odpovědi. Obojí stavíme na stejném základu: kvalitním, přehledném a pravdivém obsahu.',
        ['Stručné odpovědi na nejčastější otázky zákazníků', 'Sekce FAQ se strukturovanými daty', 'Jednoznačné informace o firmě, službách a lokalitě', 'Soubor llms.txt se shrnutím webu pro AI', 'Povolený přístup AI robotů (GPTBot, ClaudeBot, PerplexityBot…)', 'Konzistentní údaje na webu, v Google profilu i katalozích'],
      ]),
      ('Proč to řešit už teď', [
        'AI vyhledávání roste velmi rychle a firmy, které AI dobře zná, získávají doporučení dřív než konkurence. Kdo začne teď, má náskok.',
      ]),
    ],
    'work': ['credora-cz', 'axoncapital-eu', 'najemsradosti-cz'],
    'faq': [
      ('Co je GEO?', 'GEO (Generative Engine Optimization) je optimalizace webu pro AI vyhledávače jako ChatGPT, Perplexity, Gemini nebo Google AI Overviews, aby firmu správně pochopily a doporučily.'),
      ('Můžete zaručit, že mě ChatGPT doporučí?', 'Zaručit to nemůže nikdo — AI rozhoduje sama. Umíme ale výrazně zvýšit šanci tím, že web připravíme tak, aby mu AI rozuměla a důvěřovala.'),
      ('Je GEO součástí nového webu?', 'Ano. Základ GEO dostane každý web, který postavíme. Pro firmy v silně konkurenčních oborech nabízíme i dlouhodobou práci na obsahu.'),
    ],
  },
  {
    'slug': 'gdpr-cookies',
    'nav': 'GDPR a cookies',
    'title': 'GDPR a cookies na webu — cookie lišta a zásady | WebHunter',
    'desc': 'Nastavení webu podle GDPR: cookie lišta se souhlasy, zásady ochrany osobních údajů a správné zpracování údajů z formulářů. Ve spolupráci s Compliance Partner.',
    'label': 'GDPR a cookies',
    'h1': 'GDPR a cookies. <span class="serif">Bez rizika pokuty.</span>',
    'lead': 'Cookie lišta, souhlasy, zásady ochrany osobních údajů a formuláře nastavené správně. Na rozdíl od mnoha agentur to bereme vážně a spolupracujeme s odborníky z Compliance Partner.',
    'obj': 'shield',
    'answer': 'Každý web, který v Česku sbírá osobní údaje nebo používá analytické a marketingové cookies, musí splňovat GDPR a zákon o elektronických komunikacích. WebHunter nastavuje cookie lištu se skutečnými souhlasy, zásady ochrany osobních údajů a formuláře ve spolupráci s odborníky z Compliance Partner.',
    'benefits': [
      ('bnv-dark', 'shield', 'Cookie lišta se souhlasy', 'Analytika a reklamní pixely se spustí až po souhlasu návštěvníka. Tak, jak to zákon vyžaduje.'),
      ('bnv-sky', 'cursor', 'Zásady ochrany údajů', 'Srozumitelné zásady přesně podle toho, jaké údaje váš web opravdu zpracovává.'),
      ('bnv-lime', 'check', 'Formuláře v pořádku', 'Informace o zpracování u každého formuláře a údaje jen v nezbytném rozsahu.'),
      ('bnv-blue', 'spark', 'S odborníky', 'Spolupracujeme s Compliance Partner, kteří se GDPR pro weby věnují.'),
    ],
    'sections': [
      ('Co nastavíme', [
        'Web projdeme a nastavíme vše, co je potřeba, aby byl v souladu s GDPR a pravidly pro cookies.',
        ['Cookie lištu s volbou kategorií a odmítnutím jedním klikem', 'Blokování analytiky a pixelů do udělení souhlasu', 'Zásady ochrany osobních údajů a informace o cookies', 'Informace u kontaktních formulářů', 'Nastavení doby uchování údajů', 'Doporučení pro smlouvy se zpracovateli'],
      ]),
      ('Compliance Partner', [
        'Na oblast GDPR spolupracujeme s odborníky z <a href="https://www.compliancepartner.cz" target="_blank" rel="noopener" class="link-u">Compliance Partner</a>, kteří se specializují na soulad firemních webů s GDPR a pravidly pro cookies.',
      ]),
    ],
    'work': ['najemsradosti-cz', 'vacekterapie-cz', 'credora-cz'],
    'faq': [
      ('Potřebuje každý web cookie lištu?', 'Pokud web používá analytické nebo marketingové cookies (například Google Analytics nebo Meta Pixel), musí mít lištu, přes kterou návštěvník souhlas udělí nebo odmítne. Čistě nezbytné cookies souhlas nevyžadují.'),
      ('Stačí lišta s tlačítkem „Rozumím“?', 'Ne. Souhlas musí být svobodný a stejně snadné musí být i odmítnutí. Nástroje se smí spustit až po souhlasu.'),
      ('Umíte opravit i web, který jste nedělali?', 'Ano. Projdeme váš současný web a navrhneme, co je potřeba upravit — nebo vám rovnou připravíme návrh nového webu zdarma.'),
    ],
  },
  {
    'slug': 'weby-pro-reality',
    'nav': 'Weby pro nemovitosti',
    'title': 'Web pro každou nemovitost za 695 Kč — SEO a GEO | WebHunter',
    'desc': 'Prezentační web pro konkrétní nemovitost na subdoméně vaší realitní kanceláře. Galerie, parametry, mapa, WhatsApp, SEO pro Google a GEO pro AI. 695 Kč jednorázově.',
    'label': 'Weby pro reality',
    'h1': 'Vlastní web pro <span class="serif">každou nemovitost.</span>',
    'lead': 'Ke každému vašemu inzerátu připravíme hotový prezentační web, který nemovitosti přivede zájemce i mimo realitní portály. Za 695 Kč jednorázově, na subdoméně vaší kanceláře.',
    'obj': 'magnifier',
    'hstats': [('695 Kč', 'jednorázově'), ('0 Kč', 'za doménu'), ('SEO', '+ GEO')],
    'hchip': 'Web je hotový předem',
    'form': ('Odkaz na váš inzerát', 'sreality.cz/detail/…', 'Chci web k inzerátu', False),
    'answer': 'WebHunter připravuje pro realitní kanceláře a makléře samostatné prezentační weby ke konkrétním nemovitostem. Každý web má fotogalerii, parametry, mapu, kontakt přes WhatsApp a je optimalizovaný pro Google (SEO) i pro AI vyhledávače jako ChatGPT (GEO). Běží zdarma na subdoméně kanceláře a stojí 695 Kč jednorázově.',
    'benefits': [
      ('bnv-blue', 'magnifier', 'Dohledatelná na Googlu', 'Kdo hledá „dům na prodej Libín“, najde i web vaší nemovitosti, ne jen portály.'),
      ('bnv-dark', 'bubble', 'Připravená pro AI', 'ChatGPT i Gemini přesně pochopí, co prodáváte, kde, za kolik a s jakou dispozicí.'),
      ('bnv-lime', 'coin', 'Bez domény a poplatků', 'Web běží na subdoméně vaší kanceláře, třeba nemovitost.vasekancelar.cz.'),
      ('bnv-sky', 'check', 'Hotový předem', 'Web vám ukážeme dřív, než za něj cokoli zaplatíte. Stačí ho spustit.'),
    ],
    'sections': [
      ('Co každý web obsahuje', [
        'Nejde jen o další stránku s fotkami. Web je postavený přímo pro jednu nemovitost a vede zájemce k jedinému kroku: domluvit si prohlídku.',
        ['Velká fotogalerie a přehledné parametry', 'Mapa a popis lokality', 'Přímý kontakt na makléře přes WhatsApp i telefon', 'Možnost doplnit video nebo 3D prohlídku', 'Vzhled v barvách vaší realitní kanceláře', 'SEO pro Google a strukturovaná data', 'GEO — optimalizace pro ChatGPT, Gemini a další AI'],
      ]),
      ('SEO pro Google a GEO pro AI', [
        'Lidé nehledají jen na realitních portálech. Zadávají do Googlu přímo lokalitu a cenu, a čím dál častěji se ptají umělé inteligence: „Hledám dům na prodej v Libíně do 2 milionů. Co je v nabídce?“',
        'Web připravujeme tak, aby vyhledávače i AI přesně pochopily, co se prodává, kde se nemovitost nachází, za jakou cenu a s jakou dispozicí. Vaše nabídka tak může přivést zájemce, kteří by se k ní přes portály vůbec nedostali. Víc o tom píšeme u služby <a href="sluzby/geo/" class="link-u">GEO optimalizace</a>.',
      ]),
      ('Na subdoméně vaší kanceláře', [
        'Nemusíte kupovat žádnou další doménu ani zasahovat do svého současného webu. Web napojíme zdarma na subdoménu kanceláře, například nemovitost.vasekancelar.cz. Na stejné adrese pak mohou být všechny vaše nabídky.',
      ]),
      ('Kolik to stojí', [
        'Web pro jednu nemovitost stojí 695 Kč jednorázově, bez dalších plateb. Nejdřív vám pošleme hotový web k vašemu inzerátu, a teprve když se vám líbí, spustíme ho.',
      ]),
    ],
    'examples': [
      ('ukazka-1', '6ab677c88194facc3fbf7704', 'Byt 2+kk, 48 m²', 'Praha — Radlice'),
      ('ukazka-2', '6ab677c45a6f7e771eb2b2e0', 'Chalupa 140 m²', 'Bublava'),
      ('ukazka-3', '6ab677c5f1901fce6a5cb22b', 'Byt 3+kk, 89 m²', 'Brno — Komárov'),
      ('ukazka-4', '6ab677c47969e63475455725', 'Rodinný dům 120 m²', 'Lučany nad Nisou'),
      ('ukazka-5', '6ab677c13b5969af80e7bb23', 'Byt 1+kk, 47 m²', 'Praha — Holešovice'),
      ('ukazka-6', '6ab677c6aa4eccd60578bd27', 'Byt 3+kk, 77 m²', 'Praha — Troja'),
    ],
    'offer': ('Web pro jednu nemovitost', '695', 'Prezentační web pro konkrétní nemovitost na subdoméně realitní kanceláře, jednorázová platba.'),
    'work': [],
    'faq': [
      ('Kolik stojí web pro jednu nemovitost?', '695 Kč jednorázově, bez dalších plateb. Doménu kupovat nemusíte, web běží na subdoméně vaší kanceláře.'),
      ('Musím kupovat novou doménu?', 'Ne. Web napojíme zdarma na subdoménu vaší stávající kanceláře, například nemovitost.vasekancelar.cz. Na stejné adrese mohou být všechny vaše nabídky.'),
      ('Co když už mám vlastní web kanceláře?', 'Nevadí, do současného webu nijak nezasahujeme. Subdoména funguje samostatně vedle něj.'),
      ('Jak rychle může web běžet?', 'Web k vašemu inzerátu vám pošleme už hotový. Po schválení ho spustíme a napojíme na subdoménu.'),
      ('Můžu přidat video nebo 3D prohlídku?', 'Ano. Web obsahuje místo pro video i 3D prohlídku, stačí nám poslat odkaz.'),
    ],
  },
]
