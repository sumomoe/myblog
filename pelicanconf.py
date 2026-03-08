AUTHOR = 'moi'
SITENAME = "moi'sroom"
SITEURL = ''
RELATIVE_URLS = True

PATH = 'content'
ARTICLE_PATHS = ['.']

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'

THEME = 'mytheme'

# Markdownを使う
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# 記事URL
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# トップページ
INDEX_SAVE_AS = 'index.html'

# 記事一覧ページ
DIRECT_TEMPLATES = ['index', 'articles']

#ページURL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

#themeがoutputに現れなかったときに追加したやつ
THEME = "mytheme"
THEME_STATIC_DIR = "static"
STATIC_PATHS = ['static']