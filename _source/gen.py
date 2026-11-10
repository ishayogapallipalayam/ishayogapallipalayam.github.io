import json, os, shutil, sys

DOMAIN = os.environ.get("DOMAIN", "https://ishayogapallipalayam.in").rstrip("/")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/site"
NAME = "Isha Yoga Pallipalayam"
PH1, PH2 = "7010692011", "9842773480"
WA = "917010692011"
REG = "https://isha.co/pallipalayam"
WA_TEXT = "Namaskaram%2C%20I%20would%20like%20to%20know%20about%20Isha%20Yoga%20classes%20in%20Pallipalayam"
MAPQ = "https://www.google.com/maps/search/?api=1&query=Isha+Yoga+Pallipalayam"
EMBED = "https://www.google.com/maps?q=Isha+Yoga+Pallipalayam&output=embed"
POSTER = "images/isha-yoga-pallipalayam-program-poster.jpg"
POSTER_SM = "images/isha-yoga-pallipalayam-program-poster-600.jpg"

# ---- FREE CLASS: edit only this block when a new free class comes up ----
FREE = {
    "active": True,                      # False = shows "next class to be announced", no Event schema
    "date_en": "Sunday, 15 November 2026",
    "short_en": "15 Nov",
    "date_ta": "நவம்பர் 15 (ஞாயிற்றுக்கிழமை)",
    "time_en": "7:00 to 9:00 am",
    "time_ta": "காலை 7 முதல் 9 மணி வரை",
    "start": "2026-11-15T07:00:00+05:30",
    "end": "2026-11-15T09:00:00+05:30",
    "reg": "https://isha.co/ss-pallipalayam",
    "lastmod": "2026-11-10",
}
FREE_PAGE = "free-yoga-class-pallipalayam.html"

NAV = [
    ("index.html", "Home"),
    (FREE_PAGE, "Free Class"),
    ("isha-yoga-programs.html", "Programs"),
    ("yoga-classes-erode.html", "Yoga in Erode"),
    ("yoga-classes-kumarapalayam-veppadai-bhavani.html", "Nearby Areas"),
    ("isha-yoga-tamil.html", "தமிழ்"),
    ("contact.html", "Contact"),
]

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": DOMAIN + "/#business",
    "name": NAME,
    "description": "Isha yoga and meditation programs designed by Sadhguru, including Inner Engineering (Isha Yoga program) and free Surya Kriya classes, in Pallipalayam near Erode.",
    "url": DOMAIN + "/",
    "telephone": ["+91" + PH1, "+91" + PH2],
    "image": DOMAIN + "/" + POSTER,
    "address": {"@type": "PostalAddress", "addressLocality": "Pallipalayam", "addressRegion": "Tamil Nadu", "addressCountry": "IN"},
    "areaServed": ["Pallipalayam", "Erode", "Kumarapalayam", "Veppadai", "Bhavani", "Tiruchengode", "Sankagiri"],
    "hasMap": MAPQ,
    "sameAs": [REG],
}

EVENT = {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "Isha Yoga Program (Tamil) in Pallipalayam",
    "description": "7-day Isha Yoga program designed by Sadhguru, including initiation into Shambhavi Mahamudra Kriya. Morning or evening batch, 6:00 to 8:30.",
    "startDate": "2026-11-25T06:00:00+05:30",
    "endDate": "2026-12-01T20:30:00+05:30",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "inLanguage": "ta",
    "image": [DOMAIN + "/" + POSTER],
    "location": {"@type": "Place", "name": "Kongu Kalaiarangam",
                 "address": {"@type": "PostalAddress", "streetAddress": "Kongu Kalaiarangam, Vediyarasampalayam",
                             "addressLocality": "Pallipalayam", "addressRegion": "Tamil Nadu", "addressCountry": "IN"}},
    "organizer": {"@type": "Organization", "name": NAME, "url": DOMAIN + "/"},
    "offers": {"@type": "Offer", "url": REG, "availability": "https://schema.org/InStock", "validFrom": "2026-11-01T00:00:00+05:30"},
}


FREE_EVENT = {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "Free Yoga Class (Surya Shakti) in Pallipalayam",
    "description": "Free yoga class by Isha volunteers in Pallipalayam, near Erode. Open to beginners. Registration is free.",
    "startDate": FREE["start"],
    "endDate": FREE["end"],
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "inLanguage": "ta",
    "isAccessibleForFree": True,
    "image": [DOMAIN + "/" + POSTER],
    "location": {"@type": "Place", "name": "Isha Yoga Pallipalayam centre",
                 "address": {"@type": "PostalAddress", "addressLocality": "Pallipalayam", "addressRegion": "Tamil Nadu", "addressCountry": "IN"}},
    "organizer": {"@type": "Organization", "name": NAME, "url": DOMAIN + "/"},
    "offers": {"@type": "Offer", "url": FREE["reg"], "price": "0", "priceCurrency": "INR", "availability": "https://schema.org/InStock"},
}

VIDEO = {"@context": "https://schema.org", "@type": "VideoObject",
         "name": "Surya Shakti free yoga class in Pallipalayam: participants share their experience",
         "description": "Participants share their experience of the free Surya Shakti yoga class by Isha volunteers in Pallipalayam, near Erode.",
         "thumbnailUrl": DOMAIN + "/videos/surya-shakti-free-yoga-class-pallipalayam.jpg",
         "contentUrl": DOMAIN + "/videos/surya-shakti-free-yoga-class-pallipalayam.mp4",
         "uploadDate": "2026-11-10", "duration": "PT1M26S", "inLanguage": "ta"}

if FREE["active"]:
    FREE_BLOCK = f"""
<div class="event">
<span class="upnext">Free yoga class</span>
<h3>Free Yoga Class (Surya Shakti) in Pallipalayam</h3>
<dl>
<dt>Date</dt><dd>{FREE["date_en"]}</dd>
<dt>Time</dt><dd>{FREE["time_en"]}</dd>
<dt>Place</dt><dd>Isha Yoga Pallipalayam centre, Pallipalayam</dd>
<dt>Fee</dt><dd>Free</dd>
</dl>
<div class="btns"><a class="btn btn-primary" href="{FREE["reg"]}">Register free</a><a class="btn btn-ghost" href="tel:+91{PH1}">Call {PH1}</a></div>
</div>"""
    FREE_BLOCK_TA = f"""
<div class="event">
<dl>
<dt>தேதி</dt><dd>{FREE["date_ta"]}</dd>
<dt>நேரம்</dt><dd>{FREE["time_ta"]}</dd>
<dt>கட்டணம்</dt><dd>முற்றிலும் இலவசம்</dd>
</dl>
<div class="btns"><a class="btn btn-primary" href="{FREE["reg"]}">இலவசமாகப் பதிவு செய்ய</a><a class="btn btn-ghost" href="tel:+91{PH1}">அழைக்க</a></div>
</div>"""
    FREE_TITLE = f"Free Yoga Class in Pallipalayam | Surya Shakti, {FREE['short_en']}"
    FREE_BANNER = f"""<section><div class="wrap"><h2>Free yoga class in Pallipalayam: {FREE["short_en"]}</h2>
<p>A free Surya Shakti yoga class is on {FREE["date_en"]}, {FREE["time_en"]}. <a href="{FREE_PAGE}">See details and register free</a>.</p></div></section>"""
else:
    FREE_BLOCK = f"""
<div class="event"><span class="upnext">Free yoga class</span>
<h3>Next free yoga class: to be announced</h3>
<p>Free yoga classes are held from time to time in Pallipalayam. Call or WhatsApp us to be told when the next one is.</p>
<div class="btns"><a class="btn btn-wa" href="https://wa.me/{WA}?text={WA_TEXT}">WhatsApp us</a><a class="btn btn-ghost" href="tel:+91{PH1}">Call {PH1}</a></div></div>"""
    FREE_BLOCK_TA = """<div class="event"><p>அடுத்த இலவச யோகா வகுப்பு தேதி விரைவில் அறிவிக்கப்படும். அறிய அழைக்கவும்.</p></div>"""
    FREE_TITLE = "Free Yoga Class in Pallipalayam | Surya Shakti"
    FREE_BANNER = ""


def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}


def page(fname, title, desc, h1, body, schemas=(), lang="en"):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == fname else ""}{" lang=ta class=ta" if h.endswith("tamil.html") else ""}>{t}</a></li>'
        for h, t in NAV)
    canon = DOMAIN + "/" + ("" if fname == "index.html" else fname)
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/{POSTER}">
<meta property="og:locale" content="{'ta_IN' if lang == 'ta' else 'en_IN'}">
<meta name="theme-color" content="#d9661f">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='46' fill='%23d9661f'/%3E%3Ctext x='50' y='66' font-size='50' text-anchor='middle' fill='white' font-family='sans-serif'%3EI%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="index.html">{NAME}<small>Isha yoga Erode &middot; yoga &amp; meditation classes</small></a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
<details class="menu"><summary>Menu</summary><nav aria-label="Mobile"><ul>{nav}</ul></nav></details>
</div></header>
<main>
{body.replace("{{H1}}", h1)}
</main>
<footer><div class="wrap cols">
<div><h4>{NAME}</h4><p>Isha yoga and meditation programs designed by Sadhguru, for Pallipalayam, Erode, Kumarapalayam, Veppadai, Bhavani and Tiruchengode.</p></div>
<div><h4>Contact</h4><p>Pallipalayam, Namakkal district, Tamil Nadu</p><p>Phone: <a href="tel:+91{PH1}">{PH1}</a>, <a href="tel:+91{PH2}">{PH2}</a></p><p><a href="https://wa.me/{WA}?text={WA_TEXT}">WhatsApp us</a> &middot; <a href="{MAPQ}">Google Maps</a></p></div>
<div><h4>Programs</h4><p><a href="{REG}">Register: isha.co/pallipalayam</a></p><p>All programs: <a href="https://isha.sadhguru.org">isha.sadhguru.org</a></p><p class="note">Isha Foundation programs, run by Isha volunteers in Pallipalayam.</p></div>
</div></footer>
<div class="sticky"><a class="c" href="tel:+91{PH1}">Call</a><a class="w" href="https://wa.me/{WA}?text={WA_TEXT}">WhatsApp</a><a class="r" href="{REG}">Register</a></div>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)


EVENT_BLOCK = f"""
<div class="event">
<span class="upnext">Upcoming program</span>
<h3>7-day Isha Yoga Program in Pallipalayam (Tamil)</h3>
<dl>
<dt>Dates</dt><dd>25 November to 1 December 2026</dd>
<dt>Timings</dt><dd>Morning or evening batch, 6:00 to 8:30</dd>
<dt>Venue</dt><dd>Kongu Kalaiarangam, Vediyarasampalayam, Pallipalayam</dd>
<dt>Includes</dt><dd>Initiation into Shambhavi Mahamudra Kriya</dd>
</dl>
<div class="btns"><a class="btn btn-primary" href="{REG}">Register now</a><a class="btn btn-ghost" href="tel:+91{PH1}">Call {PH1}</a></div>
</div>"""

CTA = f"""<div class="btns"><a class="btn btn-primary" href="{REG}">Register for the next program</a><a class="btn btn-wa" href="https://wa.me/{WA}?text={WA_TEXT}">WhatsApp</a><a class="btn btn-ghost" href="tel:+91{PH1}">Call</a></div>"""

PROGRAM_CARDS = f"""
<div class="grid">
<div class="card"><span class="tag">7 days</span><h3>Isha Yoga Program (Inner Engineering)</h3>
<p>The Isha Yoga program, known as Inner Engineering in English, is designed by Sadhguru. It includes initiation into <b>Shambhavi Mahamudra Kriya</b>, a 21-minute practice you can continue at home every day. Held in Tamil and in English at Pallipalayam.</p></div>
<div class="card"><span class="tag">Free</span><h3>Surya Kriya Yoga Class</h3>
<p>Surya Kriya is a classical hatha yoga practice from Isha. Free Surya Kriya classes are held from time to time at Pallipalayam and are open to beginners. <a href="{FREE_PAGE}">Free class details</a>.</p></div>
<div class="card"><span class="tag">Events</span><h3>Devi Pooja and special events</h3>
<p>Devi Pooja, satsangs and special days such as Mahashivratri, Guru Purnima and International Yoga Day are held for the local community. Follow our Google Maps listing for announcements.</p></div>
</div>"""

TAMIL_SHORT = f"""
<div class="tamil ta" lang="ta">
<h3>ஈஷா யோகா பள்ளிபாளையம் மற்றும் ஈஷா யோகா ஈரோடு</h3>
<p>பள்ளிபாளையம், ஈரோடு, குமாரபாளையம், வெப்படை பகுதி மக்களுக்கான ஈஷா யோகா வகுப்புகள், இன்னர் இன்ஜினியரிங் மற்றும் இலவச சூரிய க்ரியா யோகா வகுப்புகள். ஷாம்பவி மஹாமுத்ரா க்ரியா தீட்சையுடன் கூடிய 7 நாள் ஈஷா யோகா வகுப்பு நவம்பர் 25 முதல் டிசம்பர் 1 வரை நடைபெறுகிறது.</p>
<p>வகுப்பு தேதி மற்றும் நேரம் அறிய அழைக்கவும்: <a href="tel:+91{PH1}">{PH1}</a>, <a href="tel:+91{PH2}">{PH2}</a></p>
</div>"""

COMMON_FAQ = [
    ("Where are Isha yoga classes held in Pallipalayam?",
     "The current 7-day Isha Yoga program is held at Kongu Kalaiarangam, Vediyarasampalayam, Pallipalayam, just across the Cauvery from Erode. Venues can change for each program, so please check the program details or call before you come."),
    ("Is there a free yoga class?",
     "Yes. Free Surya Kriya yoga classes are held from time to time. Call or WhatsApp us to know the next date."),
    ("Do I need any yoga experience?",
     "No. The programs are open to complete beginners, students, working professionals, women and senior citizens."),
    ("In which language are the classes held?",
     "The Isha Yoga program is held in Tamil, and Inner Engineering is held in English."),
    ("How do I register?",
     f"Register online at isha.co/pallipalayam, or call {PH1} or {PH2}."),
]


def faq_html(qas):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qas) + "</div>"


def build():
    os.makedirs(OUT, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.css"), os.path.join(OUT, "style.css"))

    # HOME
    page("index.html",
         "Isha Yoga Pallipalayam | Isha Yoga Classes near Erode",
         "Isha Yoga program (Inner Engineering) with Shambhavi Mahamudra Kriya and free Surya Kriya yoga classes in Pallipalayam, for Erode and Kumarapalayam.",
         "Isha Yoga Pallipalayam: Isha Yoga Classes near Erode",
         f"""
<div class="hero"><div class="wrap">
<div>
<h1>{{{{H1}}}}</h1>
<p class="lead">Yoga and meditation programs designed by Sadhguru, for people in Pallipalayam, Erode, Kumarapalayam, Veppadai and nearby areas. Open to beginners.</p>
{CTA}
</div>
<img class="poster" src="{POSTER_SM}" width="600" height="600" alt="Isha Yoga program poster, Pallipalayam, 25 November to 1 December" fetchpriority="high">
</div></div>

{FREE_BANNER}
<section><div class="wrap">
<h2>Next Isha Yoga program in Pallipalayam</h2>
{EVENT_BLOCK}
</div></section>

<section class="alt"><div class="wrap">
<h2>Isha yoga programs in Pallipalayam</h2>
<p>Isha Yoga Pallipalayam is run by local Isha volunteers. We conduct the Isha Yoga program (Inner Engineering), free Surya Kriya yoga classes and community events, so that people from Pallipalayam and Erode can learn Isha practices close to home.</p>
{PROGRAM_CARDS}
<p style="margin-top:16px"><a href="isha-yoga-programs.html">See all programs and details</a></p>
</div></section>

<section><div class="wrap">
<h2>Why people join Isha yoga classes</h2>
<div class="grid">
<div class="card"><h3>Simple daily practice</h3><p>Shambhavi Mahamudra Kriya takes about 21 minutes a day and can be done at home once you are initiated.</p></div>
<div class="card"><h3>Better sleep and calm</h3><p>Studies of Shambhavi practitioners, including research involving Harvard Medical School, report improvements in sleep quality and wellbeing.</p></div>
<div class="card"><h3>For everyone</h3><p>Students, working professionals, homemakers and senior citizens join the same program. No prior yoga experience is needed.</p></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Yoga classes for Erode, Kumarapalayam and nearby areas</h2>
<p>Pallipalayam is just across the Cauvery from Erode, about 5 km from Erode bus stand. People join our programs from Erode city areas such as Karungalpalayam, Surampatti and Veerappanchatram, and from Kumarapalayam, Veppadai, Bhavani, Tiruchengode and Sankagiri.</p>
<p><a href="yoga-classes-erode.html">Yoga and meditation classes in Erode</a> &middot; <a href="yoga-classes-kumarapalayam-veppadai-bhavani.html">Kumarapalayam, Veppadai and Bhavani</a></p>
{TAMIL_SHORT}
</div></section>

<section><div class="wrap">
<h2>Frequently asked questions</h2>
{faq_html(COMMON_FAQ)}
</div></section>
""",
         schemas=(BUSINESS, EVENT, faq_schema(COMMON_FAQ)))

    # PROGRAMS
    page("isha-yoga-programs.html",
         "Isha Yoga Programs, Pallipalayam & Erode | Inner Engineering",
         "Isha Yoga program (Inner Engineering) with Shambhavi Mahamudra Kriya, free Surya Kriya yoga classes and Devi Pooja in Pallipalayam, near Erode.",
         "Isha Yoga Programs in Pallipalayam and Erode",
         f"""
<section><div class="wrap">
<h1>{{{{H1}}}}</h1>
<p class="lead">All programs are designed by Sadhguru and conducted by Isha volunteers and teachers in Pallipalayam, close to Erode.</p>
{EVENT_BLOCK}
</div></section>

<section class="alt"><div class="wrap">
<h2>Isha Yoga program (Inner Engineering) with Shambhavi Mahamudra Kriya</h2>
<p>The Isha Yoga program is called <b>Inner Engineering</b> in English. Over 7 days it offers tools for wellbeing and initiation into <b>Shambhavi Mahamudra Kriya</b>, a powerful 21-minute meditation practice. Once initiated, you can practise Shambhavi at home every day.</p>
<p>The program is held in Tamil as the Isha Yoga program and in English as Inner Engineering. It is open to anyone who can sit for the session timings; no prior yoga experience is needed.</p>
<img src="{POSTER_SM}" width="600" height="600" loading="lazy" alt="Isha Yoga program in Pallipalayam with Shambhavi Mahamudra Kriya" style="width:100%;max-width:420px;border-radius:14px;margin:6px 0 18px">
<h3>Upcoming dates</h3>
<p>25 November to 1 December 2026, morning or evening batch, 6:00 to 8:30, at Kongu Kalaiarangam, Vediyarasampalayam, Pallipalayam. <a href="{REG}">Register here</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Free Surya Kriya yoga class</h2>
<p>Surya Kriya is a classical hatha yoga practice offered by Isha. Free Surya Kriya classes are held from time to time in Pallipalayam and are suitable for beginners. Call <a href="tel:+91{PH1}">{PH1}</a> or WhatsApp us to know the next class date.</p>
<h2>Devi Pooja, satsang and special days</h2>
<p>We also hold Devi Pooja, satsangs and special days such as Mahashivratri, Guru Purnima and International Yoga Day for the local community. Announcements are posted on our Google Maps listing.</p>
<h2>More Isha programs</h2>
<p>For other Isha programs, including online programs, visit <a href="https://isha.sadhguru.org">isha.sadhguru.org</a>.</p>
{CTA}
{TAMIL_SHORT}
</div></section>
""",
         schemas=(EVENT,))

    # ERODE
    erode_faq = [
        ("Is there an Isha yoga centre in Erode?",
         "Isha Yoga Pallipalayam conducts Isha yoga programs for people in Erode. Pallipalayam is across the Cauvery from Erode, about 5 km from Erode bus stand."),
        ("Are there free yoga classes near Erode?",
         "Yes. Free Surya Kriya yoga classes are held from time to time in Pallipalayam. Call or WhatsApp us for the next date."),
        ("Where can I learn Shambhavi Mahamudra in Erode?",
         "Shambhavi Mahamudra Kriya is taught in the 7-day Isha Yoga program (Inner Engineering) held in Pallipalayam, near Erode."),
    ]
    page("yoga-classes-erode.html",
         "Yoga & Meditation Classes in Erode | Isha Yoga Pallipalayam",
         "Yoga and meditation classes for Erode: Isha Yoga programs and free Surya Kriya classes in Pallipalayam, 5 km from Erode bus stand. Call or register.",
         "Yoga and Meditation Classes in Erode",
         f"""
<section><div class="wrap">
<h1>{{{{H1}}}}</h1>
<p class="lead">Looking for Isha yoga in Erode, or yoga classes in Erode for beginners? Our Isha yoga and meditation centre in Pallipalayam is a short ride away, just across the Cauvery and about 5 km from Erode bus stand.</p>
{CTA}
</div></section>

<section class="alt"><div class="wrap">
<h2>Isha yoga Erode: classes for people in Erode city</h2>
<p>Many participants in our programs come from Erode city, including Karungalpalayam, Surampatti, Veerappanchatram, Rangampalayam, Thindal, Solar, Chithode and the Erode bazaar area. The programs are designed by Sadhguru and are open to beginners.</p>
{PROGRAM_CARDS}
</div></section>

<section><div class="wrap">
<h2>Inner Engineering and Shambhavi Mahamudra near Erode</h2>
<p>The 7-day Isha Yoga program, called Inner Engineering in English, includes initiation into Shambhavi Mahamudra Kriya. The next program in Pallipalayam runs from 25 November to 1 December 2026, morning or evening, 6:00 to 8:30.</p>
{EVENT_BLOCK}
</div></section>

<section class="alt"><div class="wrap">
<h2>Meditation classes for stress, sleep and focus</h2>
<p>People from Erode join Isha yoga and meditation classes for many reasons: to sleep better, to feel calmer at work, to improve focus during studies, or simply to have a daily practice. These programs are not a medical treatment; if you have a health condition, please speak to your doctor and mention it when you register.</p>
<div class="tamil ta" lang="ta">
<h3>ஈஷா யோகா ஈரோடு: ஈரோடு யோகா வகுப்புகள்</h3>
<p>ஈரோட்டில் யோகா அல்லது தியான வகுப்பு தேடுகிறீர்களா? ஈரோடு பேருந்து நிலையத்திலிருந்து சுமார் 5 கி.மீ தொலைவில் உள்ள பள்ளிபாளையத்தில் ஈஷா யோகா வகுப்புகள், இன்னர் இன்ஜினியரிங் மற்றும் இலவச சூரிய க்ரியா யோகா வகுப்புகள் நடைபெறுகின்றன. தொடர்புக்கு: <a href="tel:+91{PH1}">{PH1}</a></p>
</div>
</div></section>

<section><div class="wrap">
<h2>Questions from Erode</h2>
{faq_html(erode_faq)}
</div></section>
""",
         schemas=(BUSINESS, faq_schema(erode_faq)))

    # NEARBY
    page("yoga-classes-kumarapalayam-veppadai-bhavani.html",
         "Yoga Classes near Kumarapalayam, Veppadai, Bhavani",
         "Isha yoga and meditation classes in Pallipalayam for Kumarapalayam (Komarapalayam), Veppadai, Bhavani, Tiruchengode and Sankagiri. Free Surya Kriya.",
         "Yoga Classes near Kumarapalayam, Veppadai, Bhavani and Tiruchengode",
         f"""
<section><div class="wrap">
<h1>{{{{H1}}}}</h1>
<p class="lead">Isha Yoga Pallipalayam welcomes people from the towns and villages around Pallipalayam. Here is how far our programs are from where you live.</p>
{CTA}
</div></section>

<section class="alt"><div class="wrap">
<h2>Distance from nearby towns to Pallipalayam</h2>
<div class="grid">
<div class="card"><h3>Kumarapalayam (Komarapalayam)</h3><p>About 10 km from Pallipalayam. Both towns are in Komarapalayam taluk, Namakkal district.</p></div>
<div class="card"><h3>Veppadai</h3><p>On the Pallipalayam to Sankari road, at the junction with the Tiruchengode to Komarapalayam road.</p></div>
<div class="card"><h3>Bhavani</h3><p>About 12 km from Pallipalayam.</p></div>
<div class="card"><h3>Tiruchengode</h3><p>About 15 km from Pallipalayam.</p></div>
<div class="card"><h3>Sankagiri</h3><p>About 19 km from Pallipalayam.</p></div>
<div class="card"><h3>Erode</h3><p>About 5 km from Erode bus stand, across the Cauvery. <a href="yoga-classes-erode.html">Yoga classes in Erode</a></p></div>
</div>
<p class="note">Distances are approximate, measured from Pallipalayam town. Check the program venue before you travel.</p>
</div></section>

<section><div class="wrap">
<h2>Areas we welcome participants from</h2>
<ul class="areas">
<li>Pallipalayam and Pallipalayam Agraharam</li><li>Alampalayam and Pudupalayam</li>
<li>Kumarapalayam (Komarapalayam)</li><li>Veppadai</li>
<li>Bhavani</li><li>Tiruchengode</li>
<li>Sankagiri</li><li>Pappampalayam</li>
<li>Erode city</li><li>Moolapalayam and Moolapatrai</li>
</ul>
<h2>Programs you can join</h2>
{PROGRAM_CARDS}
</div></section>

<section class="alt"><div class="wrap">
{EVENT_BLOCK}
<div class="tamil ta" lang="ta" style="margin-top:20px">
<h3>குமாரபாளையம், வெப்படை, பவானி பகுதி யோகா வகுப்புகள்</h3>
<p>குமாரபாளையம், வெப்படை, பவானி, திருச்செங்கோடு, சங்ககிரி பகுதி மக்கள் பள்ளிபாளையத்தில் நடைபெறும் ஈஷா யோகா மற்றும் இலவச சூரிய க்ரியா யோகா வகுப்புகளில் கலந்துகொள்ளலாம். தொடர்புக்கு: <a href="tel:+91{PH1}">{PH1}</a>, <a href="tel:+91{PH2}">{PH2}</a></p>
</div>
</div></section>
""",
         schemas=(BUSINESS,))

    # FREE CLASS
    free_faq = [
        ("Is there a free yoga class in Pallipalayam?",
         (f"Yes. A free yoga class (Surya Shakti) is on {FREE['date_en']}, {FREE['time_en']}, at the Isha Yoga Pallipalayam centre. Registration is free at isha.co/ss-pallipalayam." if FREE["active"]
          else "Free yoga classes are held from time to time in Pallipalayam. Call or WhatsApp us to know the next date.")),
        ("Is the class really free?", "Yes. The class is offered free of cost by Isha volunteers. There is no fee to register or attend."),
        ("Can beginners join?", "Yes. No yoga experience is needed. Students, working professionals, homemakers and senior citizens can join."),
        ("Is there a free yoga class near Erode?", "Pallipalayam is just across the Cauvery from Erode, about 5 km from Erode bus stand, so people from Erode, Kumarapalayam, Veppadai and Bhavani attend."),
        ("How do I register?", f"Register online at isha.co/ss-pallipalayam, or call {PH1}." if FREE["active"] else f"Call {PH1} or {PH2}, or WhatsApp us."),
    ]
    page(FREE_PAGE,
         FREE_TITLE,
         f"Free yoga class (Surya Shakti) in Pallipalayam, near Erode: {FREE['date_en']}, {FREE['time_en']}. Open to beginners. Register free." if FREE["active"]
         else "Free yoga classes in Pallipalayam, near Erode, by Isha volunteers. Open to beginners. Call or WhatsApp for the next free class date.",
         "Free Yoga Class in Pallipalayam (Surya Shakti)",
         f"""
<section><div class="wrap">
<h1>{{{{H1}}}}</h1>
<p class="lead">Looking for a free yoga class in Pallipalayam or free yoga classes near Erode? Isha volunteers hold free Surya Shakti yoga classes in Pallipalayam, open to beginners.</p>
{FREE_BLOCK}
</div></section>

<section class="alt"><div class="wrap">
<h2>Watch: Surya Shakti free yoga class, participants' experiences</h2>
<video controls preload="none" playsinline poster="videos/surya-shakti-free-yoga-class-pallipalayam.jpg" width="360" height="640" style="width:100%;max-width:360px;border-radius:14px;display:block;margin:0 0 12px;background:#fde3c8" aria-label="Surya Shakti free yoga class in Pallipalayam, participants share their experience">
<source src="videos/surya-shakti-free-yoga-class-pallipalayam.mp4" type="video/mp4"></video>
<p class="note">Free Surya Shakti yoga class by Isha volunteers, Pallipalayam.</p>
</div></section>

<section><div class="wrap">
<h2>What people feel after the class</h2>
<p>Participants of Surya Shakti say:</p>
<div class="grid">
<div class="card"><p>&ldquo;I feel the flexibility of my body.&rdquo;</p></div>
<div class="card"><p>&ldquo;I feel very active.&rdquo;</p></div>
</div>
<p class="note" style="margin-top:12px">Experiences shared by participants. Results differ from person to person. This class is not a medical treatment; if you have a health condition, please speak to your doctor and tell the volunteers when you register.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Free yoga class near Erode, Kumarapalayam and Veppadai</h2>
<p>The class is held at the Isha Yoga Pallipalayam centre, just across the Cauvery from Erode and about 5 km from Erode bus stand. People come from Erode city, Kumarapalayam (Komarapalayam), Veppadai, Bhavani, Tiruchengode and Sankagiri. See <a href="yoga-classes-erode.html">yoga classes in Erode</a> and <a href="yoga-classes-kumarapalayam-veppadai-bhavani.html">nearby areas</a>.</p>
<h2>After the free class</h2>
<p>If you like the class, you can join the 7-day <a href="isha-yoga-programs.html">Isha Yoga program (Inner Engineering)</a>, which includes initiation into Shambhavi Mahamudra Kriya.</p>
<div class="tamil ta" lang="ta">
<h3>பள்ளிபாளையத்தில் இலவச யோகா வகுப்பு: சூரிய சக்தி</h3>
<p>பள்ளிபாளையம், ஈரோடு, குமாரபாளையம், வெப்படை பகுதி மக்களுக்காக ஈஷா தன்னார்வத் தொண்டர்கள் நடத்தும் முற்றிலும் இலவச யோகா வகுப்பு (சூரிய சக்தி). ஆரம்பநிலையில் உள்ளவர்களும் கலந்துகொள்ளலாம்.</p>
{FREE_BLOCK_TA}
<p>தொடர்புக்கு: <a href="tel:+91{PH1}">{PH1}</a>, <a href="tel:+91{PH2}">{PH2}</a></p>
</div>
</div></section>

<section><div class="wrap">
<h2>Free yoga class: questions</h2>
{faq_html(free_faq)}
</div></section>
""",
         schemas=((BUSINESS, FREE_EVENT, VIDEO, faq_schema(free_faq)) if FREE["active"] else (BUSINESS, VIDEO, faq_schema(free_faq))))

    # TAMIL
    ta_faq = [
        ("பள்ளிபாளையத்தில் ஈஷா யோகா வகுப்பு எங்கு நடைபெறுகிறது?",
         "நவம்பர் 25 முதல் டிசம்பர் 1 வரையிலான ஈஷா யோகா வகுப்பு கொங்கு கலையரங்கம், வெடியரசம்பாளையம், பள்ளிபாளையத்தில் நடைபெறுகிறது."),
        ("இலவச யோகா வகுப்பு உள்ளதா?",
         "ஆம். இலவச சூரிய க்ரியா யோகா வகுப்புகள் அவ்வப்போது நடைபெறுகின்றன. அடுத்த வகுப்பு தேதி அறிய அழைக்கவும்."),
        ("யோகா அனுபவம் தேவையா?",
         "இல்லை. மாணவர்கள், பணிபுரிபவர்கள், பெண்கள், மூத்த குடிமக்கள் என அனைவரும் கலந்துகொள்ளலாம்."),
    ]
    page("isha-yoga-tamil.html",
         "ஈஷா யோகா பள்ளிபாளையம் | ஈரோடு யோகா வகுப்புகள்",
         "ஈஷா யோகா பள்ளிபாளையம்: ஈரோடு, குமாரபாளையம், வெப்படை பகுதி மக்களுக்கான ஈஷா யோகா, இன்னர் இன்ஜினியரிங், ஷாம்பவி மற்றும் இலவச சூரிய க்ரியா யோகா வகுப்புகள்.",
         "ஈஷா யோகா பள்ளிபாளையம்: ஈரோடு யோகா மற்றும் தியான வகுப்புகள்",
         f"""
<section><div class="wrap ta">
<h1>{{{{H1}}}}</h1>
<p class="lead">சத்குரு வடிவமைத்த ஈஷா யோகா வகுப்புகள் பள்ளிபாளையத்தில் நடைபெறுகின்றன. பள்ளிபாளையம், ஈரோடு, குமாரபாளையம், வெப்படை, பவானி, திருச்செங்கோடு பகுதி மக்கள் அனைவரும் கலந்துகொள்ளலாம்.</p>
<div class="btns"><a class="btn btn-primary" href="{REG}">பதிவு செய்ய</a><a class="btn btn-wa" href="https://wa.me/{WA}?text={WA_TEXT}">WhatsApp</a><a class="btn btn-ghost" href="tel:+91{PH1}">அழைக்க</a></div>
</div></section>

<section class="alt"><div class="wrap ta">
<h2>7 நாள் ஈஷா யோகா வகுப்பு: பள்ளிபாளையம் யோகா வகுப்புகள்</h2>
<div class="event">
<dl>
<dt>தேதி</dt><dd>நவம்பர் 25 முதல் டிசம்பர் 1, 2026 வரை</dd>
<dt>நேரம்</dt><dd>காலை அல்லது மாலை: 6:00 - 8:30</dd>
<dt>இடம்</dt><dd>கொங்கு கலையரங்கம், வெடியரசம்பாளையம், பள்ளிபாளையம்</dd>
</dl>
<p>ஷாம்பவி மஹாமுத்ரா க்ரியாவைத் தொடர்ந்து பயிற்சி செய்வதால் தூக்கத்தின் தரம் மேம்படுவதாக ஹார்வர்ட் மருத்துவப் பள்ளி ஆய்வு முடிவுகள் கூறுகின்றன.</p>
<div class="btns"><a class="btn btn-primary" href="{REG}">இப்போதே பதிவு செய்யுங்கள்</a></div>
</div>
</div></section>

<section><div class="wrap ta">
<h2>எங்கள் வகுப்புகள்</h2>
<div class="grid">
<div class="card"><h3>ஈஷா யோகா (இன்னர் இன்ஜினியரிங்)</h3><p>7 நாள் வகுப்பு. ஷாம்பவி மஹாமுத்ரா க்ரியா தீட்சை வழங்கப்படும். தமிழில் ஈஷா யோகா, ஆங்கிலத்தில் இன்னர் இன்ஜினியரிங்.</p></div>
<div class="card"><h3>இலவச சூரிய க்ரியா யோகா</h3><p>அவ்வப்போது நடைபெறும் இலவச ஹட யோகா வகுப்பு. ஆரம்பநிலையில் உள்ளவர்களும் கலந்துகொள்ளலாம்.</p></div>
<div class="card"><h3>தேவி பூஜை மற்றும் சிறப்பு நிகழ்ச்சிகள்</h3><p>தேவி பூஜை, சத்சங்கம், மகாசிவராத்திரி, குரு பௌர்ணமி, சர்வதேச யோகா தினம்.</p></div>
</div>
<h2 style="margin-top:28px">அடிக்கடி கேட்கப்படும் கேள்விகள்</h2>
{faq_html(ta_faq)}
<p>தொடர்புக்கு: <a href="tel:+91{PH1}">{PH1}</a>, <a href="tel:+91{PH2}">{PH2}</a></p>
</div></section>
""",
         schemas=(EVENT, faq_schema(ta_faq)), lang="ta")

    # CONTACT
    page("contact.html",
         "Contact Isha Yoga Pallipalayam | Call, WhatsApp, Location",
         "Contact Isha Yoga Pallipalayam near Erode. Call 7010692011 or 9842773480, WhatsApp us, or register online at isha.co/pallipalayam. Location map and FAQ.",
         "Contact Isha Yoga Pallipalayam",
         f"""
<section><div class="wrap">
<h1>{{{{H1}}}}</h1>
<p class="lead">Call or WhatsApp us for program dates, timings and registration. The centre opens during programs, so please call before visiting.</p>
<div class="grid">
<div class="card"><h3>Call</h3><p><a href="tel:+91{PH1}">{PH1}</a><br><a href="tel:+91{PH2}">{PH2}</a></p></div>
<div class="card"><h3>WhatsApp</h3><p><a class="btn btn-wa" href="https://wa.me/{WA}?text={WA_TEXT}">Message us</a></p></div>
<div class="card"><h3>Register online</h3><p><a class="btn btn-primary" href="{REG}">isha.co/pallipalayam</a></p></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Location</h2>
<p>Pallipalayam, Namakkal district, just across the Cauvery from Erode. Current program venue: Kongu Kalaiarangam, Vediyarasampalayam, Pallipalayam.</p>
<iframe class="map" src="{EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Isha Yoga Pallipalayam on Google Maps"></iframe>
<p style="margin-top:10px"><a href="{MAPQ}">Open in Google Maps</a></p>
</div></section>

<section><div class="wrap">
<h2>Frequently asked questions</h2>
{faq_html(COMMON_FAQ)}
{TAMIL_SHORT}
</div></section>
""",
         schemas=(BUSINESS, faq_schema(COMMON_FAQ)))

    # 404
    with open(os.path.join(OUT, "404.html"), "w") as f:
        f.write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | {NAME}</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/style.css"></head><body><section><div class="wrap"><h1>Page not found</h1><p><a href="/">Go to the {NAME} home page</a></p></div></section></body></html>')

    pages = [h for h, _ in NAV]
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for h in pages:
            loc = DOMAIN + "/" + ("" if h == "index.html" else h)
            f.write(f"  <url><loc>{loc}</loc><lastmod>{FREE['lastmod'] if h in (FREE_PAGE, 'index.html') else '2026-11-02'}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    host = DOMAIN.split("//")[1]
    if not host.endswith("github.io"):
        with open(os.path.join(OUT, "CNAME"), "w") as f:
            f.write(host + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()


build()
print("built", OUT, DOMAIN)
