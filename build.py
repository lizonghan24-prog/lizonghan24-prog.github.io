"""Build the static homepage and project notes with Python's standard library."""
from pathlib import Path
from html import escape
from hashlib import sha256
import json

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
PROJECTS = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))
BASE = 'https://lizonghan24-prog.github.io/'
STYLE_VERSION = sha256((DIST / 'styles.css').read_bytes()).hexdigest()[:10]

def text(value):
    return escape(str(value), quote=True)

def head(title, description, prefix='./', canonical=''):
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{text(title)}</title>
  <meta name="description" content="{text(description)}">
  <meta name="theme-color" content="#faf9f6">
  <link rel="canonical" href="{BASE}{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{text(title)}">
  <meta property="og:description" content="{text(description)}">
  <meta property="og:url" content="{BASE}{canonical}">
  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}styles.css?v={STYLE_VERSION}">
</head>
<body>
<a class="skip" href="#main">跳转到正文</a>
'''

def header(home='./index.html'):
    return f'''<header class="site-header page-width">
  <a class="site-name" href="{home}">李宗翰<span>Zonghan Li</span></a>
  <nav aria-label="主导航">
    <a href="{home}#projects">项目</a>
    <a href="{home}#about">关于</a>
    <a href="https://github.com/lizonghan24-prog">GitHub<span aria-hidden="true"> ↗</span></a>
  </nav>
</header>
'''

def footer(home='./index.html'):
    return f'''<footer class="page-width site-footer">
  <span>© 2026 李宗翰</span>
  <a href="{home}">首页</a>
</footer>
</body>
</html>
'''

def project_item(project):
    return f'''<article class="project-entry">
  <h3><a href="./projects/{project['id']}.html">{text(project['title'])}</a></h3>
  <p class="project-description">{text(project['summary'])}</p>
  <p class="project-tools">{text(project['tools'])}</p>
</article>
'''

intro = '''<main id="main" class="page-width" tabindex="-1">
  <section class="introduction" id="about" aria-labelledby="name">
    <div class="intro-label"><p>个人主页</p><p class="intro-subtitle">嵌入式 / 控制 / 软件</p></div>
    <div class="intro-body">
      <h1 id="name">李宗翰</h1>
      <p>我做嵌入式开发，也写和设备配套的桌面软件。</p>
      <p>最近的项目主要是电机控制、低功耗设备和上位机。日常用得比较多的是 STM32、C 和 Python，结构设计会用到 SolidWorks。</p>
      <p>这里整理了一些做过和还在做的项目。</p>
      <a class="profile-link" href="https://github.com/lizonghan24-prog">github.com/lizonghan24-prog <span aria-hidden="true">↗</span></a>
    </div>
  </section>
  <section class="projects" id="projects" aria-labelledby="projects-title">
    <div class="section-label"><h2 id="projects-title">项目</h2><p>2026</p></div>
    <div class="project-groups">
'''
home = head('李宗翰 — 个人主页', '李宗翰的个人主页。嵌入式开发、电机控制、低功耗设备与上位机项目。') + header() + intro
for group in ['设备与软件', '控制与采集']:
    home += f'<section class="project-group" aria-label="{group}">\n<h2 class="group-title">{group}</h2>\n'
    home += ''.join(project_item(p) for p in PROJECTS if p['group'] == group)
    home += '</section>\n'
home += '    </div>\n  </section>\n</main>\n' + footer()
(DIST / 'index.html').write_text(home, encoding='utf-8', newline='\n')

(DIST / 'projects').mkdir(exist_ok=True)
for index, project in enumerate(PROJECTS):
    p = project
    title = p['title']
    page = head(title + ' — 李宗翰', p['summary'], '../', f"projects/{p['id']}.html") + header('../index.html')
    page += f'''<main id="main" class="article-width" tabindex="-1">
  <a class="back-link" href="../index.html#projects">← 所有项目</a>
  <article class="project-article">
    <header class="article-header">
      <p class="article-category">{text(p['group'])}</p>
      <h1>{text(title)}</h1>
      <p class="article-tools">{text(p['tools'])}</p>
    </header>
    <p class="article-intro">{text(p['intro'])}</p>
'''
    for section in p['sections']:
        page += f'    <section>\n      <h2>{text(section["title"])}</h2>\n'
        page += ''.join(f'      <p>{text(paragraph)}</p>\n' for paragraph in section['paragraphs'])
        page += '    </section>\n'
    page += f'    <p class="project-note">{text(p["note"])}</p>\n  </article>\n'
    next_p = PROJECTS[(index + 1) % len(PROJECTS)]
    page += f'''<nav class="article-navigation" aria-label="其他项目">
  <a href="../index.html#projects">项目列表</a>
  <a href="./{next_p['id']}.html">{text(next_p['title'])} →</a>
</nav>
</main>
'''
    (DIST / 'projects' / f"{p['id']}.html").write_text(page + footer('../index.html'), encoding='utf-8', newline='\n')

urls = [''] + [f"projects/{p['id']}.html" for p in PROJECTS]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += ''.join(f'  <url><loc>{BASE}{url}</loc></url>\n' for url in urls) + '</urlset>\n'
(DIST / 'sitemap.xml').write_text(sitemap, encoding='utf-8', newline='\n')
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + BASE + 'sitemap.xml\n', encoding='utf-8', newline='\n')
print(f'Built homepage and {len(PROJECTS)} project notes.')
