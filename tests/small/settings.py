import os
PROJECT_DIR = os.path.dirname(__file__)
project_dir = lambda p: os.path.join(PROJECT_DIR, p)

# Django settings for small project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = project_dir('test.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''


TIME_ZONE = 'Australia/Melbourne'
LANGUAGE_CODE = 'en-au'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = project_dir('media')
FIXTURE_DIRS = (project_dir('fixtures'),)

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'small.urls'

TEMPLATE_DIRS = (
    project_dir('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_dms',
    'django_dms.apps.small_dms',
    #'django_extensions', # install and enable to use the scripts
)


# Import sorl.thumbnail if it is available
try:
    import sorl.thumbnail
    INSTALLED_APPS += ('sorl.thumbnail',)
except ImportError:
    pass


# Import local settings if provided
try:
    from local_settings import *
except ImportError:
    pass
