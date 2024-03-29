AUTHOR = 'Brian Lee'
SITENAME = 'brian lee'
NAME_KOR = '이지상 李知相'
SITESUBTITLE=u'brianjsl [at] mit [dot] edu'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_URL = 'https://github.com/brianjsl/brianjsl.com'

# Article settings
ARTICLE_PATHS= ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
#DEFAULT_METADATA = {'status': 'draft'}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGINS = ['pelican.plugins.render_math', ]
IGNORE_FILES = []

DISPLAY_PAGES_ON_MENU = True

#paths
PAGE_PATHS=['pages']

#THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.md'
TWITTER_USERNAME = 'brianjsl'
GITHUB_USERNAME = 'brianjsl'

ENABLE_MATHJAX = True

# Footer info
LICENSE_URL = 'https://github.com/brianjsl/brianjsl.com/blob/main/LICENSE'
LICENSE = "MIT"

# templates

DIRECT_TEMPLATES= ['index']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False