"""Regenerate the four static HTML pages. Personal copy lives in dist/assets/content.js."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
NAME = 'Nguyễn Hồng Thái'
PAGES = [('home', 'Home', 'index.html'), ('work', 'Work', 'work.html'), ('about', 'About', 'about.html'), ('contact', 'Contact', 'contact.html')]

def header(active):
    def links(mobile=False):
        return ''.join(f'<a class="{"mobile-link" if mobile else "nav-link"}" href="{file}" {"aria-current=\"page\"" if key == active else ""}>{label}</a>' for key, label, file in PAGES)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header shell">
  <nav class="desktop-nav" aria-label="Main navigation">{links()}</nav>
  <button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-navigation" hidden><span class="menu-label">Menu</span><span class="menu-icon" aria-hidden="true"><i></i><i></i><i></i></span></button>
  <nav class="mobile-nav" id="mobile-navigation" aria-label="Mobile navigation" hidden>{links(True)}</nav>
</header>'''

def portrait(compact=False):
    return f'''<div class="portrait {'compact' if compact else 'home-portrait'}" role="img" aria-label="Initials avatar for {NAME}; portrait photo to be added">
  <div class="monogram" aria-hidden="true"><span>N</span><span>H</span><span>T</span></div>
  <span class="portrait-caption">Portrait to be added</span>
</div>'''

def footer(active):
    lead = f'<span data-name>{NAME}</span>' if active == 'home' else '<a class="footer-link" href="index.html"><span class="arrow" aria-hidden="true">←</span>Home</a>'
    return f'''<footer class="site-footer shell">{lead}<span class="footer-note">Draft · details to be added</span></footer>'''

HOME_BACKGROUND = '''<div class="home-backdrop" aria-hidden="true">
  <div class="landscape-layer landscape-open"><img src="assets/backgrounds/open-meadow.png" width="720" height="404" alt="" decoding="async"></div>
  <div class="landscape-layer landscape-breeze"><img src="assets/backgrounds/breeze-field.png" width="641" height="360" alt="" decoding="async"></div>
  <div class="landscape-layer landscape-grass"><img src="assets/backgrounds/grass-sky.png" width="1200" height="1200" alt="" decoding="async"></div>
  <div class="landscape-wash"></div>
</div>'''

ART_GALLERY = f'''<div class="home-visual">
  <section class="art-wall" aria-label="Three artworks in wooden frames">
    <figure class="framed-art art-starry" style="--tilt:-4deg;--delay:180ms">
      <div class="wooden-frame"><img src="assets/art/starry-night.webp" width="1100" height="878" fetchpriority="high" decoding="async" alt="The Starry Night by Vincent van Gogh: swirling blue skies, bright stars, a cypress tree, and a village"></div>
      <figcaption><strong>The Starry Night</strong><span>Vincent van Gogh · 1889</span></figcaption>
    </figure>
    <figure class="framed-art art-leonardo" style="--tilt:3deg;--delay:380ms">
      <div class="wooden-frame"><img src="assets/art/leonardo.webp" width="750" height="1078" loading="lazy" decoding="async" alt="A red chalk profile portrait of Leonardo da Vinci, attributed to Francesco Melzi"></div>
      <figcaption><strong>Leonardo da Vinci</strong><span>Portrait attributed to Francesco Melzi</span></figcaption>
    </figure>
    <figure class="framed-art art-wanderer" style="--tilt:-2deg;--delay:560ms">
      <div class="wooden-frame"><img src="assets/art/wanderer.webp" width="850" height="1089" loading="lazy" decoding="async" alt="Der Wanderer über dem Nebelmeer by Caspar David Friedrich: a man on a rocky summit looking across mist-covered mountains"></div>
      <figcaption><strong lang="de">Der Wanderer über dem Nebelmeer</strong><span>Caspar David Friedrich · c. 1818</span></figcaption>
    </figure>
  </section>
  <div class="home-visual-footer">
    <div class="home-identity"><div class="portrait avatar" role="img" aria-label="Initials avatar for {NAME}; portrait photo to be added"><span class="avatar-initials" aria-hidden="true">NHT</span></div><p><span data-name>{NAME}</span><span>Portrait to be added</span></p></div>
    <details class="art-credits"><summary>Artwork credits</summary><div class="art-credit-list">
      <p>The artworks are reproduced from Wikimedia Commons. The wooden frames are created for this website.</p>
      <a href="https://commons.wikimedia.org/wiki/File:Vincent_van_Gogh_Starry_Night.jpg" target="_blank" rel="noopener noreferrer">The Starry Night · Vincent van Gogh <span aria-hidden="true">↗</span></a>
      <a href="https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg" target="_blank" rel="noopener noreferrer">Der Wanderer über dem Nebelmeer · Caspar David Friedrich <span aria-hidden="true">↗</span></a>
      <a href="https://commons.wikimedia.org/wiki/File:A_portrait_of_Leonardo,_by_Francesco_Melzi.jpg" target="_blank" rel="noopener noreferrer">Portrait of Leonardo da Vinci · attributed to Francesco Melzi <span aria-hidden="true">↗</span></a>
    </div></details>
  </div>
</div>'''

HOME = f'''<main id="main" class="home-main shell">
  <div class="home-grid">
    <div class="hero-copy">
      <div class="hero-eyebrow page-enter"><span class="eyebrow">01 / Home</span></div>
      <h1 class="name-stack" aria-label="{NAME}"><span class="name-word" style="--i:0" aria-hidden="true">Nguyễn</span><span class="name-word" style="--i:1" aria-hidden="true">Hồng</span><span class="name-word" style="--i:2" aria-hidden="true">Thái</span></h1>
      <div class="hero-bio"><p data-introduction>Add your introduction and career direction.</p><div class="expertise-tags" data-expertise aria-label="Areas of expertise"><span>Expertise to be added</span><span>Expertise to be added</span></div></div>
      <div class="hero-actions"><a class="pill primary" href="work.html">Explore my work<span class="arrow" aria-hidden="true">→</span></a><a class="pill" href="about.html">About me</a></div>
    </div>
    {ART_GALLERY}
  </div>
  <nav class="home-page-links page-enter" aria-label="Explore the website"><a href="work.html">Work<span class="arrow" aria-hidden="true">→</span></a><a href="about.html">About<span class="arrow" aria-hidden="true">→</span></a><a href="contact.html">Contact<span class="arrow" aria-hidden="true">→</span></a></nav>
</main>'''

def project_panel(i):
    number = f'{i + 1:02}'
    tone = ['mint', 'blue', 'teal'][i]
    return f'''<article class="project-panel" data-tone="{tone}" role="group" aria-roledescription="slide" aria-label="Project {i + 1} of 3" {'hidden' if i else ''}>
  <div class="project-copy">
    <span class="eyebrow">Project {number} / 03</span>
    <h2 data-project-title>Your featured project</h2>
    <p class="project-intro" data-project-intro>Project introduction to be added.</p>
    <dl class="project-facts"><div><dt>Role</dt><dd data-project-role>To be added</dd></div><div><dt>Achievements</dt><dd data-project-achievements>To be added</dd></div></dl>
  </div>
  <div class="project-attachment">
    <div class="attachment-matte"><div class="attachment-screen"><img src="assets/blank-project.png" width="1600" height="1100" alt="Blank image placeholder for project {number}"><span class="attachment-empty" aria-hidden="true">Image placeholder</span></div></div>
    <div class="attachment-actions"><span class="attachment-meta">Image attachment</span><button class="text-button" data-open-preview aria-label="Open project {number} attachment preview" hidden>Open preview<span class="arrow" aria-hidden="true">↗</span></button></div>
  </div>
</article>'''

WORK = f'''<main id="main" class="shell page-enter">
  <div class="page-heading"><div class="overline"><span class="eyebrow">02 / Work</span><span class="rule" aria-hidden="true"></span></div><h1>Selected work.</h1></div>
  <section class="carousel" data-carousel aria-label="Featured projects" aria-roledescription="carousel">
    <div class="carousel-stage">{''.join(project_panel(i) for i in range(3))}</div>
    <div class="carousel-controls js-only" hidden>
      <button class="carousel-control" data-action="prev" aria-label="Previous project"><span class="arrow" aria-hidden="true">←</span><span>Previous</span></button>
      <div class="project-selectors" aria-label="Select a project" style="--active:0">{''.join(f'<button class="project-selector" aria-label="Show project {i + 1} of 3" aria-pressed="{"true" if i == 0 else "false"}">{i + 1:02}</button>' for i in range(3))}</div>
      <button class="carousel-control" data-action="pause" aria-label="Pause automatic project rotation"><span data-rotation-icon aria-hidden="true">Ⅱ</span><span data-rotation-label>Pause</span></button>
      <button class="carousel-control" data-action="next" aria-label="Next project"><span>Next</span><span class="arrow" aria-hidden="true">→</span></button>
    </div>
    <div class="rotation-track js-only" aria-hidden="true" hidden><span></span></div><p class="rotation-note js-only" hidden>Rotates every 8 seconds · pause anytime</p>
    <noscript><p class="rotation-note">Enable JavaScript to browse all three project introductions.</p></noscript>
  </section>
  <p class="sr-only" data-project-status aria-live="polite" aria-atomic="true"></p>
</main>
<dialog class="preview-dialog" aria-labelledby="preview-title" aria-describedby="preview-description">
  <div class="preview-top"><h2 id="preview-title" data-preview-title>Project attachment</h2><button class="preview-close" data-close-preview aria-label="Close attachment preview">Close ×</button></div>
  <div class="preview-content" data-preview-content></div>
  <div class="preview-caption"><p id="preview-description" data-preview-description></p><a data-preview-file href="assets/blank-project.png" target="_blank" rel="noopener">Open original ↗</a></div>
</dialog>'''

ABOUT = f'''<main id="main" class="shell page-enter">
  <div class="page-heading"><div class="overline"><span class="eyebrow">03 / About</span><span class="rule" aria-hidden="true"></span></div><h1>A little<br>about me.</h1></div>
  <section class="about-intro" aria-label="Introduction">{portrait(True)}<div class="about-story"><p data-story>Add your story, areas of expertise, and the direction you want to take your career.</p><div class="expertise-tags" data-expertise aria-label="Areas of expertise"><span>Expertise to be added</span><span>Expertise to be added</span></div></div></section>
  <section class="reveal" aria-labelledby="skills-title"><div class="section-heading"><h2 id="skills-title">Skills</h2><span class="eyebrow">What I bring</span></div>
    <div class="skill-rows">
      <div class="skill-row"><h3>Professional skills</h3><ul data-skill-list="professional"><li>Core skill to be added</li><li>Core skill to be added</li><li>Core skill to be added</li></ul></div>
      <div class="skill-row"><h3>Tools &amp; technologies</h3><ul data-skill-list="tools"><li>Tool or technology to be added</li><li>Tool or technology to be added</li><li>Tool or technology to be added</li></ul></div>
      <div class="skill-row"><h3>Ways of working</h3><ul data-skill-list="working"><li>Working approach to be added</li><li>Working approach to be added</li><li>Working approach to be added</li></ul></div>
    </div>
  </section>
  <section class="reveal" aria-labelledby="education-title"><div class="section-heading"><h2 id="education-title">Education</h2><span class="eyebrow">The foundation</span></div>
    <dl class="education-list"><div><dt>University</dt><dd data-education="university">To be added</dd></div><div><dt>Degree</dt><dd data-education="degree">To be added</dd></div><div><dt>Degree classification</dt><dd data-education="classification">To be added</dd></div></dl>
  </section>
</main>'''

CONTACT = '''<main id="main" class="shell contact-main page-enter">
  <span class="eyebrow">04 / Contact</span>
  <h1 class="contact-title"><span>Let’s</span><span>connect.</span></h1>
  <div class="contact-composition">
    <div class="contact-message"><p>Start a conversation.<br>Share an idea.<br>Make something happen.</p></div>
    <section class="contact-panel" aria-label="Contact details">
      <div class="contact-row" data-contact="phone"><h2>Phone</h2><span class="contact-value">To be added</span><span class="arrow" aria-hidden="true" hidden>↗</span></div>
      <div class="contact-row" data-contact="email"><h2>Email</h2><span class="contact-value">To be added</span><span class="arrow" aria-hidden="true" hidden>↗</span></div>
      <div class="contact-row" data-contact="linkedin"><h2>LinkedIn</h2><span class="contact-value">To be added</span><span class="arrow" aria-hidden="true" hidden>↗</span></div>
      <div class="contact-row" data-contact="github"><h2>GitHub</h2><span class="contact-value">To be added</span><span class="arrow" aria-hidden="true" hidden>↗</span></div>
    </section>
  </div>
</main>'''

for key, label, file in PAGES:
    title = NAME if key == 'home' else f'{label} — {NAME}'
    content = dict(home=HOME, work=WORK, about=ABOUT, contact=CONTACT)[key]
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="{'#388087' if key == 'contact' else '#F6F6F2'}">
  <meta name="description" content="The personal website of {NAME}. Explore projects, professional skills, education, and contact details.">
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="stylesheet" href="assets/styles.css">
  <script src="assets/content.js" defer></script>
  <script src="assets/site.js" defer></script>
</head>
<body class="{key}-page">
{HOME_BACKGROUND + chr(10) if key == 'home' else ''}{header(key)}
{content}
{footer(key)}
</body>
</html>
'''
    (DIST / file).write_text(html, encoding='utf-8')
print('Rendered Home, Work, About, and Contact.')
