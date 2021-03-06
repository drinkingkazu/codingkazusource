#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazuhiro Terao'
SITENAME = 'Coding Kazu'
SITETITLE = "Hunting Neutrinos with Big Detectors and Super-Fast Computers"
SITESUBTITLE = "Coding Particle Physicist"


THEME = 'kaleko_theme'
THEME_STATIC_DIR = 'kaleko_theme/static'
PATH = 'content'
STATIC_PATHS = [ 'images', 'CNAME', "docs" ]

TIMEZONE = 'America/Chicago'

DEFAULT_PAGINATION = 5

DEFAULT_LANG = 'en'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DIRECT_TEMPLATES = ['index']

GOOGLE_ANALYTICS = 'UA-71585052-2'

# Top Menu Links
NAVLINKS = (
	('#page-top', 'Home'),
	('#about', 'About'),
        ('#research', 'Research'),
	('#contact', 'Contact')
)


#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],

	['Message', 'textarea', 'message', 'Please enter a message.']
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#MARKUP = ('md', 'ipynb')
#PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['ipynb']
