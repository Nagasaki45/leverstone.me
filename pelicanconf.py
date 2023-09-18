#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'Tom Gurion Leverstone'
SITENAME = 'Tom Gurion Leverstone'
DESCRIPTION = 'Father, musician, and coder. I collect hobbies in my spare time.'

SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

ARTICLE_ORDER_BY = 'order'

DEFAULT_DATE = 'fs'  # Get date from file creation time if missing

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Don't generate anything but index and articles
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'pdfs',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGINS = ['pelican_youtube']

SOCIAL = (
    ('fas fa-blog', 'https://blog.tomgurion.me'),
    ('fab fa-github', 'https://github.com/Nagasaki45'),
    ('fab fa-mastodon', 'https://mastodon.online/@nagasaki45'),
    ('fa fa-envelope', 'mailto:nagasaki45@gmail.com'),
)

HOBBIES = [
    {
        'title': 'Music',
        'content': '''
        I play an instrument since... forever!
        Started with sax and piano as a kid. Picked up bass guitar at 14 and played in a few rock bands since then.
        Got into electronic music in 2017 and shortly after started performing improvised modular jams under the alias <a href="https://nagasaki45.com"><i>nagasaki45</i></a>.
        Recently teamed up with <a href="https://lwlsn.github.io/digitalselves-web/"><i>digital selves</i></a> to perform together as <i>IDMT?</i>
        '''.strip(),
    },
    {
        'title': 'Code',
        'content': '''
        My main language is python. I use it regularly for web development, data analysis, and other bits and pieces.
        Like elixir for highly concurrent webapps.
        Can do some js and frontend with vue.js, gatsby.js, and bulma.
        Familiar with way too many creative coding languages: max/MSP and Pd, arduino and processing, some unity3d, blender and a bit more.
        '''.strip(),
    },
    {
        'title': 'Board games',
        'content': '''
        Enjoy playing board games for many years, and got deeper into the hobby ~2018.
        Favourite game at the moment is <a href="https://boardgamegeek.com/boardgame/155821/inis">Inis</a>.
        If you're from Queen Mary University of London, we play regularly. Drop me a line!
        '''.strip(),
    },
    {
        'title': 'Sports',
        'content': '''
        Bouldering regularly at <a href="https://www.mileendwall.org.uk/">Mile End Climbing Wall</a>.
        On a good day I might even manage a V5.
        Recently got into cycling, and especially bikepacking.
        Always try to escape the city on the weekends for a night in the tent and some scenic rides.
        There's no such thing as too many hobbies, right?
        '''.strip(),
    },
    {
        'title': 'Crafts',
        'content': '''
        Started sewing to make bags for my bike.
        Now developing some ambition for larger projects.
        Get my saw and chisels out and do some carpentry when I need new furniture.
        Also, design and build some simple modules for my synth.
        You see, my hobbies feed themselves.
        '''.strip(),
    },
]
