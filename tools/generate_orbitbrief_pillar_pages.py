#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://ihtishamhussain.com"
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6571112990031093" crossorigin="anonymous"></script>'


@dataclass(frozen=True)
class Pillar:
    slug: str
    title: str
    meta: str
    kicker: str
    h1: str
    intro: str
    quick: str
    why: str
    sections: tuple[tuple[str, str], tuple[str, str], tuple[str, str]]
    workflow: tuple[str, str, str, str]
    faq: tuple[tuple[str, str], tuple[str, str], tuple[str, str]]
    related: tuple[tuple[str, str], ...]
    visual: str


VISUALS = {
    "orbit": '<circle cx="380" cy="260" r="118" fill="#16347a"/><ellipse cx="380" cy="260" rx="300" ry="110" fill="none" stroke="#64d2ff" stroke-width="4" stroke-dasharray="14 12"/><g transform="translate(545 190)"><rect x="-34" y="-14" width="68" height="28" rx="7" fill="#edf4ff"/><rect x="-86" y="-8" width="44" height="16" fill="#8b5cf6"/><rect x="42" y="-8" width="44" height="16" fill="#8b5cf6"/></g><circle cx="545" cy="190" r="10" fill="#3ee58f"/>',
    "rocket": '<path d="M170 430 C260 300 410 205 620 105" fill="none" stroke="#64d2ff" stroke-width="5" stroke-dasharray="16 12"/><g transform="translate(510 160) rotate(-35)"><path d="M0 -90 C50 -42 50 45 0 90 C-50 45 -50 -42 0 -90Z" fill="#edf4ff"/><path d="M0 -90 C20 -42 20 45 0 90" fill="#64d2ff" opacity=".55"/><rect x="-42" y="40" width="28" height="60" fill="#8b5cf6"/><rect x="14" y="40" width="28" height="60" fill="#8b5cf6"/><path d="M-22 96 L0 145 L22 96Z" fill="#ffce5c"/></g><circle cx="165" cy="430" r="70" fill="#16347a"/>',
    "asteroid": '<circle cx="220" cy="300" r="96" fill="#16347a"/><circle cx="200" cy="275" r="42" fill="#64d2ff"/><path d="M120 300 C260 170 430 135 650 130" fill="none" stroke="#64d2ff" stroke-width="3" stroke-dasharray="10 12"/><g fill="#8b5cf6"><path d="M585 116 l24 12 12 24 -18 22 -30 -6 -12 -30z"/><path d="M470 320 l34 15 8 32 -32 18 -30 -14 -4 -34z"/></g>',
    "solar": '<circle cx="175" cy="260" r="88" fill="#ffce5c"/><circle cx="175" cy="260" r="130" fill="none" stroke="#ffce5c" stroke-width="3" opacity=".55"/><path d="M320 160 C440 105 500 205 650 135" fill="none" stroke="#64d2ff" stroke-width="7" stroke-linecap="round"/><path d="M320 250 C450 190 520 290 655 220" fill="none" stroke="#8b5cf6" stroke-width="7" stroke-linecap="round"/><circle cx="610" cy="280" r="64" fill="#16347a"/>',
    "dashboard": '<rect x="70" y="80" width="620" height="360" rx="24" fill="#0d1632" stroke="#64d2ff"/><rect x="105" y="120" width="180" height="90" rx="16" fill="#121d3f"/><rect x="315" y="120" width="180" height="90" rx="16" fill="#121d3f"/><rect x="525" y="120" width="125" height="90" rx="16" fill="#121d3f"/><path d="M120 320 C230 235 330 370 450 285 S610 300 650 245" fill="none" stroke="#3ee58f" stroke-width="5"/>',
    "cubesat": '<g transform="translate(380 260)"><rect x="-80" y="-80" width="160" height="160" rx="16" fill="#edf4ff"/><path d="M-80 -30 H80 M-80 25 H80 M-25 -80 V80 M30 -80 V80" stroke="#64d2ff" stroke-width="5"/><rect x="-220" y="-40" width="110" height="80" fill="#8b5cf6"/><rect x="110" y="-40" width="110" height="80" fill="#8b5cf6"/><path d="M-110 0 H-80 M80 0 H110" stroke="#edf4ff" stroke-width="8"/></g><ellipse cx="380" cy="260" rx="300" ry="120" fill="none" stroke="#64d2ff" stroke-width="3" stroke-dasharray="12 12"/>',
    "traffic": '<circle cx="380" cy="260" r="96" fill="#16347a"/><ellipse cx="380" cy="260" rx="310" ry="110" fill="none" stroke="#64d2ff" stroke-width="3"/><ellipse cx="380" cy="260" rx="230" ry="170" fill="none" stroke="#8b5cf6" stroke-width="3" stroke-dasharray="10 12"/><g fill="#edf4ff"><rect x="540" y="205" width="58" height="26" rx="6"/><rect x="200" y="315" width="58" height="26" rx="6"/><rect x="455" y="370" width="58" height="26" rx="6"/></g>',
    "briefing": '<rect x="90" y="80" width="580" height="360" rx="24" fill="#0d1632" stroke="#64d2ff"/><line x1="140" y1="150" x2="520" y2="150" stroke="#64d2ff" stroke-width="8" stroke-linecap="round"/><line x1="140" y1="215" x2="620" y2="215" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round"/><line x1="140" y1="280" x2="470" y2="280" stroke="#3ee58f" stroke-width="8" stroke-linecap="round"/><line x1="140" y1="345" x2="560" y2="345" stroke="#ffce5c" stroke-width="8" stroke-linecap="round"/>',
}


PILLARS = [
    Pillar(
        "iss-tracker",
        "Live ISS Tracker — Where Is the International Space Station Now?",
        "Track the ISS, understand live latitude and longitude, and learn how public ISS telemetry fits into OrbitBrief's mission intelligence console.",
        "Live ISS Tracker",
        "Where is the ISS right now?",
        "The International Space Station is one of the best ways to make orbital motion visible. It crosses continents, oceans, and time zones many times each day, turning latitude and longitude into something anyone can follow.",
        "A live ISS tracker shows the station's current latitude, longitude, speed, and ground track. OrbitBrief uses this type of public telemetry as a friendly entry point into space mission awareness.",
        "ISS tracking is high-interest evergreen content. Students search for it, space enthusiasts revisit it, and educators can use it to explain orbital mechanics without starting from equations.",
        (("Current Position", "Latitude and longitude tell you where the ISS is above Earth right now. The values change quickly because the station is travelling at orbital speed."), ("Ground Track", "The ground track is the path the ISS appears to trace across Earth's surface. It helps users understand why the station can be visible from different locations on the same day."), ("Mission Context", "A stronger tracker connects ISS movement with launches, space weather, and daily briefings so users understand more than a moving dot.")),
        ("Read public ISS telemetry", "Map position to a visual orbit panel", "Explain what latitude and longitude mean", "Link the signal into the daily OrbitBrief console"),
        (("Is OrbitBrief an official ISS tracker?", "No. OrbitBrief is an independent public-data product by DataSourceCode Labs."), ("Can I track the ISS for free?", "Yes. Public APIs such as WhereTheISS can provide browser-friendly ISS location data."), ("Why is the ISS position always changing?", "The ISS orbits Earth roughly every 90 minutes, so its ground position moves continuously.")),
        (("/space/topics/live-iss-location-map/", "Live ISS location map"), ("/space/topics/iss-pass-prediction-for-beginners/", "ISS pass prediction"), ("/space/topics/satellite-ground-track-explained/", "Satellite ground tracks")),
        "orbit",
    ),
    Pillar("upcoming-rocket-launches", "Upcoming Rocket Launches — Next Space Launch Dashboard", "Explore upcoming rocket launches, launch windows, mission status, providers, and how OrbitBrief turns launch data into readable briefings.", "Rocket Launch Intelligence", "Upcoming rocket launches in one mission briefing.", "Rocket launches are exciting, but schedules shift often. A good launch page needs more than a countdown: it needs provider context, mission status, launch window confidence, and a way to explain delays.", "An upcoming rocket launches dashboard summarizes the next missions, launch windows, providers, status, and useful links in one readable view.", "Launch queries are frequent and time-sensitive. They can bring recurring search traffic when the page is useful, fast, and connected to a live feed.", (("Launch Window", "A launch window is a period when the mission can lift off. Showing a window is more honest than showing only a single time."), ("Provider and Mission", "Provider, rocket, payload, and location help users understand the mission behind the countdown."), ("Status Language", "Go, hold, TBD, success, and failure states should be visually clear and beginner-friendly.")), ("Fetch upcoming launch feed", "Normalize provider and window data", "Rank launches by time and status", "Show them in the OrbitBrief mission feed"), (("Where does launch data come from?", "OrbitBrief is designed to use public launch data sources such as Launch Library 2."), ("Why do launch dates change?", "Weather, technical checks, range availability, and mission constraints can all shift a launch."), ("Can students use launch data?", "Yes. Launch feeds are useful for learning mission timelines and public space data workflows.")), (("/space/topics/next-rocket-launch-today/", "Next rocket launch today"), ("/space/topics/rocket-launch-calendar-api/", "Rocket launch calendar API"), ("/space/topics/space-launch-window-explained/", "Launch windows explained")), "rocket"),
    Pillar("near-earth-objects", "Near-Earth Objects Today — Asteroid Close Approach Awareness", "Understand near-Earth objects, asteroid close approaches, hazard flags, size estimates, and OrbitBrief's NEO awareness layer.", "NEO Awareness", "Near-Earth objects explained for daily space briefings.", "Asteroid and near-Earth object data can sound dramatic, but most objects are awareness items rather than immediate threats. The product challenge is to explain the signal without exaggeration.", "A near-Earth object is an asteroid or comet whose orbit brings it near Earth's neighborhood. A useful dashboard shows name, size estimate, close approach context, and hazard flag carefully.", "NEO topics attract curiosity and news-driven searches. They also need responsible wording so the content feels educational rather than sensational.", (("Size Estimates", "Most public feeds show an estimated range rather than an exact size. Dashboards should communicate uncertainty clearly."), ("Hazard Flags", "Potentially hazardous does not mean an impact is expected. It means the object meets monitoring criteria."), ("Awareness Briefing", "OrbitBrief can summarize NEOs as awareness signals alongside launches, ISS tracking, and space weather.")), ("Read public NEO data", "Extract name, size, and hazard flag", "Avoid alarmist wording", "Add the signal to the daily briefing"), (("Are near-Earth objects dangerous?", "Most are not immediate dangers. They are tracked for awareness and science."), ("What does potentially hazardous mean?", "It is a monitoring classification based on size and orbit criteria, not a prediction of impact."), ("Does OrbitBrief predict impacts?", "No. OrbitBrief explains public awareness data and links users to broader context.")), (("/space/topics/asteroid-close-approach-today/", "Asteroid close approach today"), ("/space/topics/nasa-neows-api-explained/", "NASA NeoWs API"), ("/space/topics/potentially-hazardous-asteroid-meaning/", "Potentially hazardous asteroid meaning")), "asteroid"),
    Pillar("space-weather-dashboard", "Space Weather Dashboard — Solar Activity for Satellite Awareness", "Learn what a space weather dashboard should show: solar activity, geomagnetic storms, NASA notifications, satellite impact, and readable briefing language.", "Space Weather", "A dashboard for solar activity and mission awareness.", "Space weather connects solar activity to practical effects near Earth. It can influence satellites, radio communication, GPS accuracy, and operational awareness.", "A space weather dashboard summarizes solar flares, geomagnetic storm notices, radiation storm alerts, and possible impact in plain language.", "Space weather is an evergreen educational topic with real-world relevance. It can support traffic from students, radio users, aurora watchers, and space enthusiasts.", (("Solar Signals", "Solar flares, coronal mass ejections, and energetic particles are different phenomena and should not be mixed together carelessly."), ("Operational Impact", "Strong events can matter for satellite drag, radio conditions, GPS accuracy, and mission planning."), ("Readable Alerts", "Raw alert feeds need translation into concise summaries and severity language.")), ("Read public notification feeds", "Classify alert type", "Explain likely impact", "Show source health and fallback state"), (("Is space weather normal weather?", "No. It describes solar and near-Earth space conditions rather than clouds or rain."), ("Can space weather affect satellites?", "Yes. Strong events can affect drag, electronics, communication, and operational planning."), ("Does OrbitBrief issue official alerts?", "No. OrbitBrief summarizes public feeds for awareness and education.")), (("/space/topics/space-weather-today/", "Space weather today"), ("/space/topics/nasa-donki-notifications/", "NASA DONKI notifications"), ("/space/topics/space-weather-impact-on-satellites/", "Space weather impact on satellites")), "solar"),
    Pillar("solar-storm-alerts", "Solar Storm Alerts — Geomagnetic Storm Monitoring Explained", "Solar storm alerts explained for beginners: geomagnetic storms, satellite impact, GPS effects, aurora context, and OrbitBrief briefing design.", "Solar Storm Alerts", "Solar storm alerts made readable.", "Solar storm alerts are often written for technical users. OrbitBrief's approach is to make them readable: what happened, what systems may be affected, and whether the signal needs attention.", "A solar storm alert warns that solar activity may disturb near-Earth space. The best public pages explain severity and impact without causing unnecessary alarm.", "Solar storm search traffic spikes during active solar events. Strong evergreen explanations can also rank between news cycles.", (("Geomagnetic Storms", "Geomagnetic storms are disturbances in Earth's magnetic environment caused by solar activity."), ("Possible Effects", "Impacts can include aurora visibility, radio disruption, GPS degradation, and satellite operations awareness."), ("Briefing Format", "A useful briefing separates the event, severity, source, and plain-language takeaway.")), ("Monitor public alert feeds", "Summarize event type", "Explain likely user impact", "Connect to OrbitBrief's daily feed"), (("Are solar storms always dangerous?", "No. Many alerts are awareness-level events."), ("Can solar storms create auroras?", "Yes. Geomagnetic activity can increase aurora visibility in some regions."), ("Should beginners monitor solar storm alerts?", "Yes, if the dashboard explains what the alert means in plain language.")), (("/space/topics/geomagnetic-storm-dashboard/", "Geomagnetic storm dashboard"), ("/space/topics/solar-flare-alert-dashboard/", "Solar flare alert dashboard"), ("/space/topics/aurora-forecast-space-weather/", "Aurora and space weather")), "solar"),
    Pillar("satellite-operations-dashboard", "Satellite Operations Dashboard — What Space Teams Need", "A practical guide to satellite operations dashboards: status cards, event timelines, source health, operator notes, and public-data awareness.", "Satellite Operations Dashboard", "One screen for mission awareness.", "A satellite operations dashboard should not simply collect widgets. It should help a team notice what changed, what matters now, and what action should happen next.", "A satellite operations dashboard summarizes spacecraft status, alerts, timelines, source health, and operator notes in a way that supports monitoring and decisions.", "This topic connects OrbitBrief to a real SaaS category: dashboards that turn complex technical data into workflows.", (("Status Cards", "Metrics should be short, prioritized, and visually consistent."), ("Event Timelines", "Passes, launches, alerts, and review items are easier to understand when organized by time."), ("Operator Notes", "Notes and decisions turn passive monitoring into a workflow.")), ("Collect signals", "Group by mission relevance", "Highlight priority and uncertainty", "Record the briefing outcome"), (("Is OrbitBrief operational software?", "No. It is a public-data mission awareness product concept."), ("Who needs this kind of dashboard?", "Students, enthusiasts, educators, and early-stage space teams can all benefit from readable dashboards."), ("Could this become SaaS?", "Yes. Future features could include saved dashboards, teams, alerts, and briefing exports.")), (("/space/topics/operator-briefing-dashboard/", "Operator briefing dashboard"), ("/space/topics/source-health-dashboard/", "Source health dashboard"), ("/space/topics/satellite-risk-monitoring-dashboard/", "Satellite risk monitoring dashboard")), "dashboard"),
    Pillar("mission-control-dashboard", "Mission Control Dashboard — Modern Space Console Design", "Mission control dashboard design for space products: signal hierarchy, source health, timelines, dark UI, and readiness scoring.", "Mission Control UX", "Mission control dashboards should feel calm, not chaotic.", "Mission-control aesthetics can attract users, but clarity keeps them. A good space console uses strong visual hierarchy, restrained animation, and direct explanations.", "A mission control dashboard is a focused interface for monitoring status, timelines, alerts, and source health during mission-like workflows.", "This page supports product and UX searches around space dashboards while connecting back to the OrbitBrief console.", (("Signal Hierarchy", "Important items should be visible before decorative elements."), ("Source Health", "Dashboards that depend on public feeds should show whether a source is live, delayed, or using fallback data."), ("Readiness Score", "A score can summarize overall state, but it should be explainable and not pretend to be official.")), ("Normalize data sources", "Compute a simple readiness signal", "Show feed health", "Produce an operator-style briefing"), (("Why dark UI?", "Dark UI fits space dashboards and helps status colors stand out."), ("Should dashboards animate everything?", "No. Motion should clarify context, not distract."), ("Is a readiness score official?", "In OrbitBrief it is a product metric for awareness, not an operational certification.")), (("/space/topics/mission-readiness-score/", "Mission readiness score"), ("/space/topics/space-dashboard-ux-design/", "Space dashboard UX design"), ("/space/topics/dark-mode-mission-console/", "Dark mode mission console")), "dashboard"),
    Pillar("cubesat-mission-planning", "CubeSat Mission Planning — Student Satellite Dashboard Ideas", "CubeSat mission planning for students: launch readiness, timelines, ground station planning, risk registers, and OrbitBrief dashboard concepts.", "CubeSat Mission Planning", "A student-friendly mission dashboard for CubeSat teams.", "CubeSat teams often balance engineering, documentation, deadlines, and learning. A lightweight dashboard can help turn mission planning into shared awareness.", "CubeSat mission planning organizes mission goals, payload readiness, launch timeline, operations planning, communication windows, and team risks.", "CubeSat content can attract students, university teams, educators, and space clubs. It also fits OrbitBrief's learning-focused product direction.", (("Mission Timeline", "Design, integration, testing, launch, commissioning, and operations need visible milestones."), ("Ground Station Planning", "Teams need to understand when and how they may communicate with a spacecraft."), ("Risk Register", "Simple risk tracking makes student projects more professional.")), ("Define mission milestones", "Track public launch and space signals", "Summarize readiness and risks", "Share a briefing with the team"), (("Is OrbitBrief only for professionals?", "No. It is useful for students and enthusiasts too."), ("Can public APIs help CubeSat teams?", "Yes, for education and awareness. Operational systems need validated workflows."), ("Could OrbitBrief support teams later?", "Yes. Team workspaces and saved briefings are natural SaaS features.")), (("/space/topics/cubesat-dashboard-for-students/", "CubeSat dashboard for students"), ("/space/topics/cubesat-launch-readiness-checklist/", "CubeSat launch readiness checklist"), ("/space/topics/student-mission-control-console/", "Student mission control console")), "cubesat"),
    Pillar("space-traffic-management", "Space Traffic Management Explained — STM Basics", "Space Traffic Management explained: satellites, debris, coordination, sustainability, and how dashboards support public understanding.", "Space Traffic Management", "Space traffic management explained simply.", "As orbital activity grows, space becomes a coordination problem as well as an engineering problem. Space Traffic Management is the broad idea of making space operations safer and more sustainable.", "Space Traffic Management is the coordination of space activities to improve safety, sustainability, and responsible use of orbital environments.", "STM is a strategic keyword because it connects space sustainability, operators, policy, and software dashboards.", (("Coordination", "Operators need shared awareness when satellites and debris occupy busy orbital regions."), ("Sustainability", "Responsible orbit use depends on monitoring, planning, and reducing avoidable risk."), ("Public Understanding", "Dashboards and explainers make STM easier to understand for non-specialists.")), ("Collect public space signals", "Explain what they mean", "Connect them to sustainability context", "Guide readers into OrbitBrief's awareness console"), (("Is STM the same as air traffic control?", "No. Space traffic has different physics, ownership, and coordination constraints."), ("Does OrbitBrief provide STM services?", "No. OrbitBrief is a public-data awareness and education product."), ("Why does STM matter now?", "More satellites and debris increase the need for monitoring and coordination.")), (("/space/topics/space-traffic-management-dashboard/", "Space Traffic Management dashboard"), ("/space/topics/space-sustainability-dashboard/", "Space sustainability dashboard"), ("/space/topics/active-satellite-coordination/", "Active satellite coordination")), "traffic"),
    Pillar("space-situational-awareness", "Space Situational Awareness Explained — SSA Basics", "Space Situational Awareness explained: tracking satellites, debris, objects, space weather, and mission context in readable dashboards.", "Space Situational Awareness", "SSA is about knowing what is happening in orbit.", "Space Situational Awareness combines object tracking, environmental context, and operational interpretation. For beginners, the challenge is understanding the vocabulary before the math.", "Space Situational Awareness is the ability to observe and understand space objects and conditions, including satellites, debris, orbits, and environmental factors.", "SSA is a strong educational topic and highly relevant to modern space software. OrbitBrief can explain SSA concepts without claiming to be a certified SSA platform.", (("Object Awareness", "Satellites, debris, and natural objects all contribute to the space picture."), ("Environmental Context", "Space weather can change operational conditions around Earth."), ("Briefing Layer", "A dashboard turns complex space data into a sequence of understandable signals.")), ("Track public signals", "Group objects and events", "Explain risk and context carefully", "Link readers to deeper topics"), (("Is SSA only for governments?", "No. Operators, researchers, students, and enthusiasts can all learn from SSA concepts."), ("Is OrbitBrief an SSA platform?", "No. It is an awareness and education product concept using public data."), ("How is SSA different from STM?", "SSA is about knowing the space environment; STM is about coordination and management.")), (("/space/topics/space-situational-awareness-dashboard/", "SSA dashboard"), ("/space/topics/space-domain-awareness-vs-ssa/", "SDA vs SSA"), ("/space/topics/orbital-debris-monitoring/", "Orbital debris monitoring")), "traffic"),
    Pillar("satellite-collision-avoidance", "Satellite Collision Avoidance Explained — Risk Monitoring Basics", "Satellite collision avoidance explained carefully: conjunctions, miss distance, probability of collision, maneuver review, and safe dashboard language.", "Collision Avoidance Basics", "Satellite collision avoidance, explained carefully.", "Collision avoidance is a specialist operational domain. OrbitBrief can explain the vocabulary and dashboard ideas, but real avoidance decisions belong to validated systems and trained teams.", "Satellite collision avoidance is the process of monitoring predicted close approaches and deciding whether action is needed to reduce risk.", "This topic attracts high-value search interest, but it must be handled carefully to avoid overstating product capability.", (("Conjunction", "A conjunction is a predicted close approach between two space objects."), ("Miss Distance", "Miss distance is the estimated closest separation during the event."), ("Decision Support", "Dashboards can help explain context, but operational decisions require validated data and procedures.")), ("Explain the vocabulary", "Show how risk might be visualized", "Avoid operational claims", "Point readers to awareness and education use cases"), (("Does OrbitBrief calculate collision risk?", "No. OrbitBrief is not a certified collision-avoidance system."), ("Who performs real avoidance decisions?", "Satellite operators and flight dynamics specialists use validated tools and procedures."), ("Why explain this topic?", "Because understanding the vocabulary helps students and enthusiasts follow space sustainability discussions.")), (("/space/topics/conjunction-event-explained/", "Conjunction event explained"), ("/space/topics/miss-distance-explained/", "Miss distance explained"), ("/space/topics/probability-of-collision-explained/", "Probability of collision explained")), "traffic"),
    Pillar("daily-space-briefing", "Daily Space Briefing — Launches, ISS, Space Weather, and Asteroids", "A daily space briefing combines launches, ISS telemetry, NASA alerts, asteroid awareness, source health, and readable mission notes.", "Daily Space Briefing", "A daily briefing for what is happening in space.", "Space activity is scattered across many public sources. A daily space briefing helps users start with one readable summary instead of checking many feeds separately.", "A daily space briefing is a short operational-style summary of current space activity: launches, ISS location, space weather, NEO awareness, and source health.", "Daily briefing pages can support repeat visits, newsletter ideas, and future SaaS features such as saved dashboards or email alerts.", (("Launches", "Upcoming missions provide time-sensitive signals for the day."), ("Space Conditions", "Space weather and NEO awareness give broader context."), ("Source Health", "A briefing should tell users whether the data is live, delayed, or using fallback information.")), ("Read public feeds", "Summarize the important signals", "Group them by priority", "Present a human-readable daily note"), (("Can OrbitBrief become a daily email?", "Yes. A daily email or Slack digest is a natural future feature."), ("Is this only for experts?", "No. The briefing is designed for students, enthusiasts, educators, and early-stage teams."), ("What makes a good briefing?", "Short explanations, clear source status, and links to deeper context.")), (("/space/topics/daily-orbit-briefing/", "Daily orbit briefing"), ("/space/topics/mission-briefing-generator/", "Mission briefing generator"), ("/space/topics/space-alert-digest/", "Space alert digest")), "briefing"),
]


def visual(name: str) -> str:
    return f'<svg viewBox="0 0 760 520" role="img" aria-label="Space illustration"><rect width="760" height="520" rx="28" fill="#07112a"/>{VISUALS[name]}<g fill="#fff" opacity=".85"><circle cx="115" cy="105" r="3"/><circle cx="655" cy="95" r="3"/><circle cx="630" cy="405" r="4"/><circle cx="285" cy="430" r="3"/></g></svg>'


def schema(p: Pillar) -> str:
    questions = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (escape(q), escape(a))
        for q, a in p.faq
    )
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % questions


def page(p: Pillar) -> str:
    related = "\n".join(
        f'<a class="space-link-card" href="{escape(href)}"><h3>{escape(label)}</h3><p>Continue exploring this OrbitBrief topic.</p></a>'
        for href, label in p.related
    )
    cards = "\n".join(
        f'<article class="space-card"><h3>{escape(title)}</h3><p>{escape(body)}</p></article>'
        for title, body in p.sections
    )
    workflow = "\n".join(f"<li>{escape(step)}</li>" for step in p.workflow)
    faq = "\n".join(f"<h3>{escape(q)}</h3><p>{escape(a)}</p>" for q, a in p.faq)
    return dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{escape(p.title)}</title>
      <meta name="description" content="{escape(p.meta)}">
      <link rel="canonical" href="{SITE}/space/{p.slug}/">
      <link rel="stylesheet" href="/assets/style.css">
      <link rel="stylesheet" href="/assets/space-seo.css">
      {ADSENSE_SCRIPT}
      <script type="application/ld+json">{schema(p)}</script>
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
            <p class="space-kicker">{escape(p.kicker)}</p>
            <h1 class="space-title">{escape(p.h1)}</h1>
            <p>{escape(p.intro)}</p>
            <a class="space-btn" href="/apps/orbitbrief/">Launch OrbitBrief Console</a>
            <a class="space-btn" href="/space/topics/" style="margin-left:.5rem;">Browse Topics</a>
          </div>
          <div class="space-visual">{visual(p.visual)}</div>
        </section>

        <nav class="space-toc" aria-label="Page sections">
          <a href="#quick-answer">Quick answer</a>
          <a href="#why-it-matters">Why it matters</a>
          <a href="#dashboard-pattern">Dashboard pattern</a>
          <a href="#workflow">OrbitBrief workflow</a>
          <a href="#faq">FAQ</a>
        </nav>

        <section id="quick-answer" class="space-answer">
          <h2>Quick Answer</h2>
          <p>{escape(p.quick)}</p>
        </section>

        <section id="why-it-matters" class="space-answer">
          <h2>Why This Topic Matters</h2>
          <p>{escape(p.why)}</p>
          <p>For OrbitBrief, the product opportunity is to combine clear education with a live dashboard experience. Search visitors get a useful explanation first, then they can open the console to explore current public space signals.</p>
        </section>

        <section id="dashboard-pattern">
          <h2 class="section-title">What a Useful Dashboard Should Show</h2>
          <div class="space-card-grid">{cards}</div>
        </section>

        <div class="orbitbrief-ad-slot" aria-label="Future advertising slot">Future AdSense placement: responsive in-content unit.</div>

        <section id="workflow" class="space-answer">
          <h2>How OrbitBrief Handles This</h2>
          <p>OrbitBrief is designed as a public-data space intelligence console. The workflow for this topic is intentionally simple and transparent:</p>
          <ol>{workflow}</ol>
        </section>

        <section class="space-cta">
          <h2>Explore This in OrbitBrief</h2>
          <p>Open the live console for ISS telemetry, launch windows, NASA space-weather signals, near-Earth object awareness, source health, and daily mission-style briefings.</p>
          <a class="space-btn" href="/apps/orbitbrief/">Launch OrbitBrief</a>
        </section>

        <section>
          <h2 class="section-title">Related OrbitBrief Topics</h2>
          <div class="space-link-grid">{related}</div>
        </section>

        <section id="faq" class="space-faq">
          <h2>FAQ</h2>
          {faq}
        </section>
      </main>

      <footer class="site-footer"><p class="copyright container">© 2026 Ihtisham Hussain · OrbitBrief by DataSourceCode Labs</p></footer>
      <script src="/assets/site.js"></script>
    </body>
    </html>
    """)


def main() -> None:
    for pillar in PILLARS:
        path = ROOT / "space" / pillar.slug / "index.html"
        path.write_text(page(pillar), encoding="utf-8")
    print(f"Generated {len(PILLARS)} stronger OrbitBrief pillar pages.")


if __name__ == "__main__":
    main()
