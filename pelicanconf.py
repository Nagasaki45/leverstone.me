#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'Tom Leverstone'
SITENAME = 'Tom Leverstone'
ABOUT_TITLE = "Hi! I'm Tom 👋"
DESCRIPTION = 'A father, software engineer, and hobbies collector.'

SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'


def ARTICLE_ORDER_BY(article):
    if article.category in ["Projects", "Hobbies"]:
        return float(article.order)
    return -article.date.timestamp()


DEFAULT_DATE = 'fs'  # Get date from file creation time if missing

# Things we don't need

ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Filepaths and URLs

CATEGORY_URL = '/{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '/{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '/{slug}'
PAGE_SAVE_AS = '{slug}.html'

PAGINATED_TEMPLATES = {'category': 10}

# Feeds

FEED_DOMAIN = os.environ.get('FEED_DOMAIN', '')
CATEGORY_FEED_ATOM = '{slug}/atom.xml'

# Static files

STATIC_PATHS = [
    'images',
    'pdfs',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGINS = [
    'pelican_youtube',
    'yaml_metadata',
]

# Content

SOCIAL = (
    ('fab fa-github', 'https://github.com/Nagasaki45', 'GitHub'),
    ('fab fa-linkedin', 'https://www.linkedin.com/in/tleverstone/', 'LinkedIn'),
    ('fab fa-goodreads', ' https://www.goodreads.com/nagasaki45', 'Goodreads'),
    ('fa fa-envelope', 'mailto:tleverstone@gmail.com', 'Email'),
)

SUMMARY_MAX_LENGTH = 35

# Markdown config

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}
