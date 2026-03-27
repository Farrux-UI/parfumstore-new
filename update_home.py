import re

paths = [
    r"c:\Users\User\Desktop\parfumstore-n\src\pages\index.astro",
    r"c:\Users\User\Desktop\parfumstore-n\src\pages\[lang]\index.astro"
]

for file_path in paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: Add i18n import
    if "useTranslations" not in content:
        if file_path.endswith("[lang]\\index.astro"):
            content = content.replace("import Layout from '../../layouts/Layout.astro';", 
                                      "import { useTranslations } from '../../utils/i18n';\nimport Layout from '../../layouts/Layout.astro';")
        else:
            content = content.replace("import Layout from '../layouts/Layout.astro';", 
                                      "import { useTranslations } from '../utils/i18n';\nimport Layout from '../layouts/Layout.astro';")
            
        content = content.replace("---", "---\nconst lang = Astro.currentLocale || 'az';\nconst t = useTranslations(lang);", 2)

    # Note: `---` replacement above using count=2 will drop it right after the second ---. 
    # Let's fix that safely:
    parts = content.split("---")
    if len(parts) >= 3 and "const t = useTranslations(lang);" not in parts[1]:
        parts[1] = parts[1] + "const lang = Astro.currentLocale || 'az';\nconst t = useTranslations(lang);\n"
        content = "---".join(parts)


    # Replacements
    replacements = {
        r"About\s*<\/h2>": "{t('home.about')}</h2>",
        r"Since the beginning, Parfumstore has represented the intersection of art, heritage, and editorial excellence. We do not simply vend fragrances—we present olfactory narratives.": "{t('home.about_p1')}",
        r"Each bottle in our collection is selected through meticulous curation, representing decades of craftsmanship from master perfumers across the world. From Grasse to Baku, every fragrance embodies the philosophy that true luxury whispers rather than shouts.": "{t('home.about_p2')}",
        r"We present perfumes as fine art. The packaging, the story, the presentation—every element reflects our commitment to editorial excellence and visual harmony.": "{t('home.about_p3')}",
        r"Editorial Image": "{t('home.editorialImage')}",
        r"Find Your Perfect Scent": "{t('home.findScent')}",
        r"Mysterious Oud": "{t('home.mysteriousOud')}",
        r"Deep, resinous wood notes with smoky richness. The ancient heart of Arabian perfumery, veiled in dark velvet.": "{t('home.oudDesc')}",
        r"Warm Amber": "{t('home.warmAmber')}",
        r"Sun-kissed fossils of ancient resin. A liquid embrace of honeyed warmth and luminous depth that lingers.": "{t('home.amberDesc')}",
        r"Fresh Spices": "{t('home.freshSpices')}",
        r"Cardamom, pink pepper, and star anise. A vibrant overture of hand-ground botanicals from distant markets.": "{t('home.spiceDesc')}",
        r">Explore<": ">{t('home.explore')}<",
        r"Bestsellers\s*<\/h2>": "{t('home.bestsellers')}</h2>",
        r">More Products<": ">{t('home.moreProducts')}<",
        r"Philosophy\s*<\/h2>": "{t('home.philosophy')}</h2>",
        r"Why Us\s*<\/h3>": "{t('home.whyUs')}</h3>",
        r"Our selective approach means every fragrance in our repository has been chosen with the same rigor a museum curator applies to fine art. We reject trends. We seek timelessness. Each bottle represents decades of master craftsmanship.": "{t('home.whyUsDesc')}",
        r"Why Niche\?\s*<\/h3>": "{t('home.whyNiche')}</h3>",
        r"Art versus mass market — niche perfumery is the couture of fragrance. While commercial scents aim for broad appeal, niche compositions are authored works of olfactory art, designed to provoke, captivate, and endure.": "{t('home.whyNicheDesc')}",
        r"Notes & Evolution\s*<\/h3>": "{t('home.notesEvolution')}</h3>",
        r"A fragrance lives and breathes. Top notes greet you. Heart notes reveal character. Base notes leave a lasting signature. Understanding this evolution transforms wearing perfume into a deeply personal ritual.": "{t('home.notesDesc')}",
        r"Contacts\s*<\/h4>": "{t('home.contacts')}</h4>",
        r"Location\s*<\/h4>": "{t('home.location')}</h4>",
        r"Baku, Azerbaijan": "{t('home.locationDesc1')}",
        r"By Appointment": "{t('home.locationDesc2')}",
        r"Tuesday – Sunday": "{t('home.locationDesc3')}",
        r"Legal\s*<\/h4>": "{t('home.legal')}</h4>",
        r"Privacy Policy": "{t('home.privacyPolicy')}",
        r"Terms of Service": "{t('home.termsService')}",
        r"Return Policy": "{t('home.returnPolicy')}",
        r"Stay Updated\s*<\/h4>": "{t('home.stayUpdated')}</h4>",
        r">Subscribe<": ">{t('home.subscribe')}<",
        r"We respect your privacy. Unsubscribe at any time.": "{t('home.weRespect')}",
        r'placeholder="YOUR EMAIL"': 'placeholder={t("home.placeholderEmail")}'
    }

    for pattern, repl in replacements.items():
        content = re.sub(pattern, repl, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done")
