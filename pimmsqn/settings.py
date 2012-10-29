# -*- coding: utf-8 -*-
# Django settings for cmip5q project.
import os
thisDir = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# If we need to deploy the ap using a script path, we have to tell it here ... 
# This is a cmip5 addition to the normal django settings, used by urls.py
DEPLOYED_SCRIPT_PATH=''

ADMINS = (
    ('Gerard Devine', 'g.m.devine@reading.ac.uk'),
)
SERVER_EMAIL = 'meta4q@neptune.badc.rl.ac.uk'

MANAGERS = ADMINS

#settings for local sqlite
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(thisDir, 'pimmsqn.sqlite') # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = thisDir

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z$aa%+2gds&=+gk*m)2dvt%#t28o(kbq38nao#&45k&)651_(g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'pimmsqn.urls'

# Switch for PJK's sandbox.  
# TODO: Does Django have a better way of doing this e.g. env variable?
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(thisDir, "templates")
            )

TEMPLATE_STRING_IF_INVALID = 'what happened here?'

#STATIC_DOC_ROOT = os.path.join(thisDir, "templates", "css", )
STATIC_DOC_ROOT = os.path.join(thisDir, "static", )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'south',
    'apps.qn',
    'apps.initialiser',
    'apps.explorer'
)

# ----------------------------------------------------
# Local customisations follow
#
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(name)s %(module)s %(levelname)s [%(asctime)s] %(message)s',
)
LOG=logging.getLogger('CMIP5')

# Location of test files to expose through feed

TESTDIR = os.path.join (thisDir,'test')

try:
    from local_settings import *
except ImportError:
    pass

