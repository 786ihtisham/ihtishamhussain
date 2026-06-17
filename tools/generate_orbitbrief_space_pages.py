#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
TOPIC_ROOT = ROOT / "space" / "topics"
SITE = "https://ihtishamhussain.com"
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6571112990031093" crossorigin="anonymous"></script>'


@dataclass(frozen=True)
class Topic:
    slug: str
    title: str
    keyword: str
    question: str
    category: str
    pillar: str
    angle: str


GROUPS = [
    {
        "category": "ISS and satellite tracking",
        "pillar": "/space/iss-tracker/",
        "angle": "live orbital tracking, ground tracks, passes, and beginner-friendly satellite visibility.",
        "items": [
            ("where-is-the-iss-now", "Where Is the ISS Now?", "where is the ISS now", "Where is the ISS right now?"),
            ("live-iss-location-map", "Live ISS Location Map", "live ISS location map", "How can I see the ISS location on a map?"),
            ("iss-pass-prediction-for-beginners", "ISS Pass Prediction for Beginners", "ISS pass prediction", "How do ISS pass predictions work?"),
            ("satellite-tracker-dashboard", "Satellite Tracker Dashboard", "satellite tracker dashboard", "What should a satellite tracker dashboard show?"),
            ("real-time-satellite-position-api", "Real-Time Satellite Position API", "real time satellite position API", "Which APIs can show live satellite positions?"),
            ("iss-altitude-and-speed-explained", "ISS Altitude and Speed Explained", "ISS altitude and speed", "How fast and high is the ISS?"),
            ("space-station-orbit-path", "Space Station Orbit Path", "space station orbit path", "What is the orbit path of the space station?"),
            ("satellite-ground-track-explained", "Satellite Ground Track Explained", "satellite ground track", "What is a satellite ground track?"),
            ("best-free-satellite-tracking-data", "Best Free Satellite Tracking Data", "free satellite tracking data", "Where can developers find free satellite tracking data?"),
            ("iss-tracker-for-students", "ISS Tracker for Students", "ISS tracker for students", "How can students learn from ISS tracking?"),
            ("orbital-position-dashboard", "Orbital Position Dashboard", "orbital position dashboard", "How do dashboards show orbital position?"),
            ("satellite-visibility-dashboard", "Satellite Visibility Dashboard", "satellite visibility dashboard", "How can a dashboard explain satellite visibility?"),
        ],
    },
    {
        "category": "Rocket launches",
        "pillar": "/space/upcoming-rocket-launches/",
        "angle": "upcoming launch windows, launch providers, mission status, and public launch intelligence.",
        "items": [
            ("next-rocket-launch-today", "Next Rocket Launch Today", "next rocket launch today", "What is the next rocket launch?"),
            ("rocket-launch-calendar-api", "Rocket Launch Calendar API", "rocket launch calendar API", "How can developers get rocket launch calendar data?"),
            ("upcoming-spacex-launches-dashboard", "Upcoming SpaceX Launches Dashboard", "upcoming SpaceX launches dashboard", "How can a dashboard track upcoming SpaceX launches?"),
            ("esa-launch-schedule-dashboard", "ESA Launch Schedule Dashboard", "ESA launch schedule", "How can users follow ESA launch schedules?"),
            ("space-launch-window-explained", "Space Launch Window Explained", "space launch window explained", "What is a launch window?"),
            ("launch-service-provider-tracker", "Launch Service Provider Tracker", "launch service provider tracker", "How do you track launch providers?"),
            ("rocket-launch-status-meaning", "Rocket Launch Status Meaning", "rocket launch status meaning", "What do launch statuses mean?"),
            ("launch-countdown-dashboard", "Launch Countdown Dashboard", "launch countdown dashboard", "What should a launch countdown dashboard include?"),
            ("free-space-launch-api", "Free Space Launch API", "free space launch API", "Which free APIs provide launch data?"),
            ("rocket-launch-briefing-page", "Rocket Launch Briefing Page", "rocket launch briefing", "What should a launch briefing include?"),
            ("mission-patch-and-launch-data", "Mission Patch and Launch Data", "mission patch launch data", "How can launch dashboards use mission patches?"),
            ("launch-location-map-dashboard", "Launch Location Map Dashboard", "launch location map dashboard", "How can a launch map improve mission awareness?"),
        ],
    },
    {
        "category": "Space weather",
        "pillar": "/space/space-weather-dashboard/",
        "angle": "solar activity, geomagnetic storms, satellite impact, GPS awareness, and public alert feeds.",
        "items": [
            ("space-weather-today", "Space Weather Today", "space weather today", "What is today's space weather?"),
            ("geomagnetic-storm-dashboard", "Geomagnetic Storm Dashboard", "geomagnetic storm dashboard", "How can a dashboard explain geomagnetic storms?"),
            ("solar-flare-alert-dashboard", "Solar Flare Alert Dashboard", "solar flare alert dashboard", "How should solar flare alerts be presented?"),
            ("cme-alerts-explained", "CME Alerts Explained", "CME alerts explained", "What is a coronal mass ejection alert?"),
            ("space-weather-impact-on-gps", "Space Weather Impact on GPS", "space weather impact on GPS", "Can space weather affect GPS?"),
            ("space-weather-impact-on-satellites", "Space Weather Impact on Satellites", "space weather impact on satellites", "How does space weather affect satellites?"),
            ("noaa-space-weather-dashboard", "NOAA Space Weather Dashboard", "NOAA space weather dashboard", "What can a NOAA space weather dashboard show?"),
            ("nasa-donki-notifications", "NASA DONKI Notifications", "NASA DONKI notifications", "What are NASA DONKI notifications?"),
            ("solar-radiation-storm-alerts", "Solar Radiation Storm Alerts", "solar radiation storm alerts", "What is a solar radiation storm alert?"),
            ("aurora-forecast-space-weather", "Aurora Forecast and Space Weather", "aurora forecast space weather", "How are auroras connected to space weather?"),
            ("satellite-drag-space-weather", "Satellite Drag and Space Weather", "satellite drag space weather", "How can solar activity affect satellite drag?"),
            ("space-weather-api-for-developers", "Space Weather API for Developers", "space weather API", "Which public APIs help developers track space weather?"),
        ],
    },
    {
        "category": "Asteroids and NEOs",
        "pillar": "/space/near-earth-objects/",
        "angle": "near-Earth object awareness, asteroid close approaches, size estimates, and hazard flags.",
        "items": [
            ("asteroid-close-approach-today", "Asteroid Close Approach Today", "asteroid close approach today", "Are any asteroids passing Earth today?"),
            ("near-earth-object-dashboard", "Near-Earth Object Dashboard", "near earth object dashboard", "What should a NEO dashboard show?"),
            ("potentially-hazardous-asteroid-meaning", "Potentially Hazardous Asteroid Meaning", "potentially hazardous asteroid meaning", "What does potentially hazardous asteroid mean?"),
            ("nasa-neows-api-explained", "NASA NeoWs API Explained", "NASA NeoWs API", "What is the NASA NeoWs API?"),
            ("asteroid-size-estimate-explained", "Asteroid Size Estimate Explained", "asteroid size estimate", "How are asteroid sizes estimated?"),
            ("asteroid-risk-dashboard", "Asteroid Risk Dashboard", "asteroid risk dashboard", "How should asteroid risk be shown?"),
            ("neo-awareness-for-students", "NEO Awareness for Students", "NEO awareness for students", "How can students learn about near-Earth objects?"),
            ("asteroid-feed-for-developers", "Asteroid Feed for Developers", "asteroid API for developers", "Which public asteroid APIs can developers use?"),
            ("near-earth-object-tracker-free", "Near-Earth Object Tracker Free", "free near earth object tracker", "Can I track near-Earth objects for free?"),
            ("asteroid-watch-dashboard", "Asteroid Watch Dashboard", "asteroid watch dashboard", "What is an asteroid watch dashboard?"),
            ("asteroids-and-space-situational-awareness", "Asteroids and Space Situational Awareness", "asteroids space situational awareness", "How do asteroids fit into space awareness?"),
            ("daily-asteroid-briefing", "Daily Asteroid Briefing", "daily asteroid briefing", "What should a daily asteroid briefing include?"),
        ],
    },
    {
        "category": "Space traffic and SSA",
        "pillar": "/space/space-situational-awareness/",
        "angle": "space situational awareness, traffic management, debris monitoring, conjunctions, and sustainable orbit use.",
        "items": [
            ("space-situational-awareness-dashboard", "Space Situational Awareness Dashboard", "space situational awareness dashboard", "What should an SSA dashboard show?"),
            ("space-traffic-management-dashboard", "Space Traffic Management Dashboard", "space traffic management dashboard", "What should an STM dashboard show?"),
            ("orbital-debris-monitoring", "Orbital Debris Monitoring", "orbital debris monitoring", "How is orbital debris monitored?"),
            ("conjunction-event-explained", "Conjunction Event Explained", "conjunction event explained", "What is a conjunction event in space?"),
            ("miss-distance-explained", "Miss Distance Explained", "miss distance satellite", "What does miss distance mean?"),
            ("probability-of-collision-explained", "Probability of Collision Explained", "probability of collision satellite", "What is probability of collision?"),
            ("space-sustainability-dashboard", "Space Sustainability Dashboard", "space sustainability dashboard", "How can dashboards support space sustainability?"),
            ("satellite-risk-monitoring-dashboard", "Satellite Risk Monitoring Dashboard", "satellite risk monitoring dashboard", "What is satellite risk monitoring?"),
            ("active-satellite-coordination", "Active Satellite Coordination", "active satellite coordination", "Why do active satellites need coordination?"),
            ("space-domain-awareness-vs-ssa", "Space Domain Awareness vs SSA", "space domain awareness vs SSA", "How is SDA different from SSA?"),
            ("space-debris-dashboard-for-students", "Space Debris Dashboard for Students", "space debris dashboard for students", "How can students learn about space debris?"),
            ("satellite-conjunction-briefing", "Satellite Conjunction Briefing", "satellite conjunction briefing", "What should a conjunction briefing include?"),
        ],
    },
    {
        "category": "CubeSat and education",
        "pillar": "/space/cubesat-mission-planning/",
        "angle": "student missions, CubeSat planning, ground stations, payload planning, and educational dashboards.",
        "items": [
            ("cubesat-dashboard-for-students", "CubeSat Dashboard for Students", "CubeSat dashboard for students", "What should a student CubeSat dashboard include?"),
            ("student-satellite-mission-dashboard", "Student Satellite Mission Dashboard", "student satellite mission dashboard", "How can students organize satellite missions?"),
            ("cubesat-launch-readiness-checklist", "CubeSat Launch Readiness Checklist", "CubeSat launch readiness checklist", "What goes into CubeSat launch readiness?"),
            ("cubesat-ground-station-planning", "CubeSat Ground Station Planning", "CubeSat ground station planning", "How do CubeSat teams plan ground station operations?"),
            ("cubesat-risk-register", "CubeSat Risk Register", "CubeSat risk register", "Why does a CubeSat team need a risk register?"),
            ("cubesat-payload-planning", "CubeSat Payload Planning", "CubeSat payload planning", "How do teams plan a CubeSat payload?"),
            ("university-space-mission-dashboard", "University Space Mission Dashboard", "university space mission dashboard", "What dashboard helps university space missions?"),
            ("space-stem-dashboard", "Space STEM Dashboard", "space STEM dashboard", "How can space dashboards support STEM education?"),
            ("cubesat-operations-timeline", "CubeSat Operations Timeline", "CubeSat operations timeline", "What is a CubeSat operations timeline?"),
            ("cubesat-public-data-tools", "CubeSat Public Data Tools", "CubeSat public data tools", "Which public data tools help CubeSat students?"),
            ("student-mission-control-console", "Student Mission Control Console", "student mission control console", "How can students build a mission control console?"),
            ("cubesat-briefing-template", "CubeSat Briefing Template", "CubeSat briefing template", "What should a CubeSat briefing template include?"),
        ],
    },
    {
        "category": "Mission control product design",
        "pillar": "/space/mission-control-dashboard/",
        "angle": "mission console design, dashboard UX, readiness scoring, source health, and operational notes.",
        "items": [
            ("mission-readiness-score", "Mission Readiness Score", "mission readiness score", "What is a mission readiness score?"),
            ("operator-briefing-dashboard", "Operator Briefing Dashboard", "operator briefing dashboard", "What should an operator briefing dashboard show?"),
            ("source-health-dashboard", "Source Health Dashboard", "source health dashboard", "Why does source health matter in dashboards?"),
            ("mission-timeline-dashboard", "Mission Timeline Dashboard", "mission timeline dashboard", "How should a mission timeline dashboard work?"),
            ("space-dashboard-ux-design", "Space Dashboard UX Design", "space dashboard UX design", "What makes space dashboard UX effective?"),
            ("dark-mode-mission-console", "Dark Mode Mission Console", "dark mode mission console", "Why do mission consoles often use dark UI?"),
            ("space-alert-priority-design", "Space Alert Priority Design", "space alert priority design", "How should space alerts be prioritized?"),
            ("public-data-mission-console", "Public Data Mission Console", "public data mission console", "Can public APIs power a mission-style console?"),
            ("mission-control-for-educators", "Mission Control for Educators", "mission control for educators", "How can educators use mission dashboards?"),
            ("space-briefing-user-interface", "Space Briefing User Interface", "space briefing user interface", "What should a space briefing UI include?"),
            ("operational-dashboard-micro-saas", "Operational Dashboard Micro-SaaS", "operational dashboard micro SaaS", "Can an operational dashboard become a micro-SaaS?"),
            ("space-intelligence-console", "Space Intelligence Console", "space intelligence console", "What is a space intelligence console?"),
        ],
    },
    {
        "category": "Public space APIs",
        "pillar": "/apps/orbitbrief/",
        "angle": "free APIs, browser-friendly data, fallback design, API source health, and developer education.",
        "items": [
            ("free-space-apis-for-developers", "Free Space APIs for Developers", "free space APIs for developers", "Which free space APIs can developers use?"),
            ("nasa-api-dashboard", "NASA API Dashboard", "NASA API dashboard", "How can NASA APIs power a dashboard?"),
            ("launch-library-api-dashboard", "Launch Library API Dashboard", "Launch Library API dashboard", "How can Launch Library data be used?"),
            ("wheretheiss-api-dashboard", "WhereTheISS API Dashboard", "WhereTheISS API dashboard", "How can WhereTheISS power live tracking?"),
            ("browser-friendly-space-apis", "Browser-Friendly Space APIs", "browser friendly space APIs", "Which space APIs work in browser dashboards?"),
            ("space-api-fallback-design", "Space API Fallback Design", "space API fallback design", "How should dashboards handle API failures?"),
            ("public-space-data-product", "Public Space Data Product", "public space data product", "How can public space data become a product?"),
            ("space-data-normalization", "Space Data Normalization", "space data normalization", "How do you normalize space API data?"),
            ("space-api-source-health", "Space API Source Health", "space API source health", "Why show source health in public API apps?"),
            ("static-space-dashboard-cloudflare-pages", "Static Space Dashboard on Cloudflare Pages", "static space dashboard Cloudflare Pages", "Can a space dashboard run on Cloudflare Pages?"),
            ("space-dashboard-without-backend", "Space Dashboard Without Backend", "space dashboard without backend", "Can a dashboard use public APIs without a backend?"),
            ("space-data-for-javascript-apps", "Space Data for JavaScript Apps", "space data for JavaScript apps", "How can JavaScript apps use space data?"),
        ],
    },
    {
        "category": "Daily space intelligence",
        "pillar": "/space/daily-space-briefing/",
        "angle": "daily briefings, newsletters, summaries, saved dashboards, and future SaaS workflows.",
        "items": [
            ("daily-space-news-dashboard", "Daily Space News Dashboard", "daily space news dashboard", "What should a daily space news dashboard include?"),
            ("daily-orbit-briefing", "Daily Orbit Briefing", "daily orbit briefing", "What is a daily orbit briefing?"),
            ("space-briefing-email", "Space Briefing Email", "space briefing email", "Could space data become a daily email briefing?"),
            ("space-awareness-newsletter", "Space Awareness Newsletter", "space awareness newsletter", "What should a space awareness newsletter include?"),
            ("mission-briefing-generator", "Mission Briefing Generator", "mission briefing generator", "How can public feeds generate mission briefings?"),
            ("space-events-today-dashboard", "Space Events Today Dashboard", "space events today dashboard", "What space events are worth tracking today?"),
            ("orbital-events-briefing", "Orbital Events Briefing", "orbital events briefing", "What is an orbital events briefing?"),
            ("space-alert-digest", "Space Alert Digest", "space alert digest", "How should space alerts be summarized?"),
            ("space-enthusiast-dashboard", "Space Enthusiast Dashboard", "space enthusiast dashboard", "What dashboard helps space enthusiasts?"),
            ("space-dashboard-for-researchers", "Space Dashboard for Researchers", "space dashboard for researchers", "How can researchers use public space dashboards?"),
            ("mission-intelligence-micro-saas", "Mission Intelligence Micro-SaaS", "mission intelligence micro SaaS", "What is a mission intelligence micro-SaaS?"),
            ("orbitbrief-product-roadmap", "OrbitBrief Product Roadmap", "OrbitBrief product roadmap", "What could OrbitBrief become as a SaaS product?"),
        ],
    },
]


BASE_URLS = [
    ("/", "1.0"),
    ("/about/", "0.8"),
    ("/services/", "0.8"),
    ("/portfolio/", "0.8"),
    ("/apps/orbitbrief/", "0.8"),
    ("/space/", "0.8"),
    ("/space/iss-tracker/", "0.7"),
    ("/space/upcoming-rocket-launches/", "0.7"),
    ("/space/near-earth-objects/", "0.7"),
    ("/space/space-weather-dashboard/", "0.7"),
    ("/space/solar-storm-alerts/", "0.7"),
    ("/space/satellite-operations-dashboard/", "0.7"),
    ("/space/mission-control-dashboard/", "0.7"),
    ("/space/cubesat-mission-planning/", "0.7"),
    ("/space/space-traffic-management/", "0.7"),
    ("/space/space-situational-awareness/", "0.7"),
    ("/space/satellite-collision-avoidance/", "0.7"),
    ("/space/daily-space-briefing/", "0.7"),
    ("/contact/", "0.8"),
]


def topics() -> list[Topic]:
    result: list[Topic] = []
    for group in GROUPS:
        for slug, title, keyword, question in group["items"]:
            result.append(
                Topic(
                    slug=slug,
                    title=title,
                    keyword=keyword,
                    question=question,
                    category=group["category"],
                    pillar=group["pillar"],
                    angle=group["angle"],
                )
            )
    return result


def svg(topic: Topic, index: int) -> str:
    hue = ["#64d2ff", "#8b5cf6", "#3ee58f", "#ffce5c", "#ff5c7a"][index % 5]
    return f"""
    <svg viewBox="0 0 760 520" role="img" aria-label="{escape(topic.title)} SVG illustration">
      <rect width="760" height="520" rx="28" fill="#07112a"/>
      <circle cx="380" cy="260" r="{92 + (index % 4) * 12}" fill="#16347a"/>
      <ellipse cx="380" cy="260" rx="{235 + (index % 5) * 16}" ry="{92 + (index % 3) * 18}" fill="none" stroke="{hue}" stroke-width="4" stroke-dasharray="14 12"/>
      <path d="M110 {360 - (index % 5) * 18} C240 {210 + (index % 4) * 16} 430 {180 + (index % 5) * 11} 650 {130 + (index % 4) * 28}" fill="none" stroke="#64d2ff" stroke-width="3" opacity=".85"/>
      <g fill="#edf4ff">
        <rect x="{170 + (index % 6) * 48}" y="{130 + (index % 4) * 36}" width="62" height="26" rx="7"/>
        <rect x="{470 - (index % 5) * 26}" y="{300 - (index % 4) * 24}" width="62" height="26" rx="7"/>
      </g>
      <g fill="{hue}">
        <circle cx="{145 + (index % 7) * 62}" cy="{105 + (index % 5) * 56}" r="7"/>
        <circle cx="{610 - (index % 6) * 44}" cy="{390 - (index % 5) * 48}" r="6"/>
      </g>
    </svg>
    """


def page(topic: Topic, index: int) -> str:
    url = f"{SITE}/space/topics/{topic.slug}/"
    description = (
        f"{topic.title}: a clear OrbitBrief guide to {topic.keyword}, "
        f"with space dashboard context, public data ideas, and mission briefing examples."
    )
    answer = (
        f"{topic.title} is part of OrbitBrief's focus on {topic.angle} "
        f"The goal is to make {topic.keyword} understandable for students, "
        f"space enthusiasts, educators, and early-stage space teams."
    )
    return dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{escape(topic.title)} — OrbitBrief Space Intelligence</title>
      <meta name="description" content="{escape(description)}">
      <link rel="canonical" href="{url}">
      <link rel="stylesheet" href="/assets/style.css">
      <link rel="stylesheet" href="/assets/space-seo.css">
      {ADSENSE_SCRIPT}
      <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{escape(topic.question)}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape(answer)}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "How does OrbitBrief use this topic?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "OrbitBrief turns public space data and educational context into a readable mission intelligence console. It is designed for awareness, education, and product discovery rather than operational safety decisions."
            }}
          }}
        ]
      }}
      </script>
    </head>
    <body class="space-page">
      <header class="site-header">
        <div class="container nav">
          <a class="brand" href="/">Ihtisham Hussain</a>
          <button class="nav-toggle" aria-label="Menu">☰</button>
          <ul class="nav-links">
            <li><a href="/space/">Space Hub</a></li>
            <li><a href="/space/topics/">Topics</a></li>
            <li><a href="/apps/orbitbrief/">OrbitBrief</a></li>
            <li><a href="/portfolio/">Portfolio</a></li>
          </ul>
        </div>
      </header>

      <main class="container">
        <section class="space-hero">
          <div>
            <p class="space-kicker">{escape(topic.category)}</p>
            <h1 class="space-title">{escape(topic.title)}</h1>
            <p>{escape(description)}</p>
            <div>
              <span class="space-pill">{escape(topic.keyword)}</span>
              <span class="space-pill">OrbitBrief</span>
              <span class="space-pill">Space intelligence</span>
            </div>
            <a class="space-btn" href="/apps/orbitbrief/">Launch OrbitBrief Console</a>
          </div>
          <div class="space-visual">{svg(topic, index)}</div>
        </section>

        <nav class="space-toc" aria-label="Page sections">
          <a href="#answer">Quick answer</a>
          <a href="#dashboard">Dashboard use case</a>
          <a href="#seo">Why it matters</a>
          <a href="#faq">FAQ</a>
        </nav>

        <section id="answer" class="space-answer">
          <h2>Quick Answer</h2>
          <p><strong>{escape(topic.question)}</strong> {escape(answer)}</p>
        </section>

        <section id="dashboard">
          <h2 class="section-title">How This Fits OrbitBrief</h2>
          <div class="space-card-grid">
            <article class="space-card">
              <h3>Mission Context</h3>
              <p>{escape(topic.title)} becomes more useful when it is shown with timing, source health, and related space events.</p>
            </article>
            <article class="space-card">
              <h3>Public Data Layer</h3>
              <p>OrbitBrief is designed around public feeds, fallback handling, and readable summaries instead of raw API output.</p>
            </article>
            <article class="space-card">
              <h3>Readable Briefings</h3>
              <p>The product goal is to turn technical space signals into short briefings that non-specialists can understand.</p>
            </article>
          </div>
        </section>

        <section id="seo" class="space-answer">
          <h2>Why {escape(topic.keyword)} Matters</h2>
          <p>People search for <strong>{escape(topic.keyword)}</strong> because space data is exciting but fragmented. A useful page should explain the concept, show how it appears in a dashboard, and guide users to a live product experience.</p>
          <p>OrbitBrief connects this topic to broader mission intelligence: ISS tracking, launches, near-Earth object awareness, space weather, satellite operations, CubeSat planning, and space traffic concepts.</p>
        </section>

        <section class="space-cta">
          <h2>Explore More in OrbitBrief</h2>
          <p>Open the live console or continue through the OrbitBrief topic library for more space dashboards and explainers.</p>
          <a class="space-btn" href="/apps/orbitbrief/">Launch Console</a>
          <a class="space-btn" href="{topic.pillar}" style="margin-left:.5rem;">Read Pillar Guide</a>
        </section>

        <section id="faq" class="space-faq">
          <h2>FAQ</h2>
          <h3>{escape(topic.question)}</h3>
          <p>{escape(answer)}</p>
          <h3>Is OrbitBrief official operational software?</h3>
          <p>No. OrbitBrief is an independent DataSourceCode Labs product for public space awareness, education, and product exploration. It is not intended for operational safety decisions.</p>
        </section>

        <div class="orbitbrief-ad-slot" aria-label="Future advertising slot">
          Future AdSense placement: responsive in-content unit.
        </div>
      </main>
      <footer class="site-footer"><p class="copyright container">© 2026 Ihtisham Hussain · OrbitBrief by DataSourceCode Labs</p></footer>
      <script src="/assets/site.js"></script>
    </body>
    </html>
    """)


def index_page(all_topics: list[Topic]) -> str:
    cards = "\n".join(
        f'<a class="space-link-card" href="/space/topics/{escape(t.slug)}/"><h3>{escape(t.title)}</h3><p>{escape(t.question)}</p><span class="space-pill">{escape(t.category)}</span></a>'
        for t in all_topics
    )
    return dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>OrbitBrief Space Topic Library — 100+ Space Guides</title>
      <meta name="description" content="Browse 100+ OrbitBrief guides for ISS tracking, rocket launches, space weather, asteroids, CubeSat planning, SSA, STM, and mission dashboard design.">
      <link rel="canonical" href="{SITE}/space/topics/">
      <link rel="stylesheet" href="/assets/style.css">
      <link rel="stylesheet" href="/assets/space-seo.css">
      {ADSENSE_SCRIPT}
    </head>
    <body class="space-page">
      <header class="site-header"><div class="container nav"><a class="brand" href="/">Ihtisham Hussain</a><button class="nav-toggle" aria-label="Menu">☰</button><ul class="nav-links"><li><a href="/space/">Space Hub</a></li><li><a href="/apps/orbitbrief/">OrbitBrief</a></li><li><a href="/portfolio/">Portfolio</a></li></ul></div></header>
      <main class="container">
        <section class="space-hero">
          <div>
            <p class="space-kicker">OrbitBrief Topic Library</p>
            <h1 class="space-title">100+ space guides for mission intelligence search.</h1>
            <p>Explore long-tail space explainers built around OrbitBrief: live satellite tracking, launch dashboards, NASA APIs, space weather, NEO awareness, CubeSat planning, SSA, STM, and mission control UX.</p>
            <a class="space-btn" href="/apps/orbitbrief/">Launch OrbitBrief Console</a>
          </div>
          <div class="space-visual">{svg(Topic("topics", "OrbitBrief Topic Library", "space topic library", "What is the OrbitBrief topic library?", "OrbitBrief", "/space/", "space education and dashboards."), 7)}</div>
        </section>
        <section>
          <h2 class="section-title">All OrbitBrief Topics</h2>
          <p class="section-lead">These pages are designed for SEO and GEO: direct answers, FAQ structure, internal links, and fast static delivery.</p>
          <div class="space-link-grid">{cards}</div>
        </section>
      </main>
      <footer class="site-footer"><p class="copyright container">© 2026 Ihtisham Hussain · OrbitBrief by DataSourceCode Labs</p></footer>
      <script src="/assets/site.js"></script>
    </body>
    </html>
    """)


def write_sitemap(all_topics: list[Topic]) -> None:
    urls = BASE_URLS + [("/space/topics/", "0.7")] + [
        (f"/space/topics/{topic.slug}/", "0.6") for topic in all_topics
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority in urls:
        lines.append(f"  <url><loc>{SITE}{path}</loc><priority>{priority}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    all_topics = topics()
    TOPIC_ROOT.mkdir(parents=True, exist_ok=True)
    for index, topic in enumerate(all_topics):
        directory = TOPIC_ROOT / topic.slug
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(page(topic, index), encoding="utf-8")
    (TOPIC_ROOT / "index.html").write_text(index_page(all_topics), encoding="utf-8")
    write_sitemap(all_topics)
    print(f"Generated {len(all_topics)} OrbitBrief topic pages.")


if __name__ == "__main__":
    main()
