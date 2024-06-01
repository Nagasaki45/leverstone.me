#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'Tom Leverstone'
SITENAME = 'Tom Leverstone'
ABOUT_TITLE = "Hi! I'm Tom 👋"
DESCRIPTION = 'A father, software engineer, and hobbies collector. You may know me as Tom Gurion. Now it\'s Tom Leverstone.'

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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Things we don't need
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Filepaths and URLs

CATEGORY_URL = '/{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '/{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

PAGINATED_TEMPLATES = {'category': 10}

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
    ('fa fa-envelope', 'mailto:tleverstone@gmail.com', 'Email'),
)

SUMMARY_MAX_LENGTH = 35
