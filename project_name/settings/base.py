# -*- coding: utf-8 -*-

"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from .utils import rel
import os, site

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = rel('..')
BASE_DIR = rel('')

# site.addpackage is actually responsible for *.pth file processing
site.addpackage(os.path.join(ROOT_DIR), 'modules.pth', known_paths=set())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2(71@@pf!j$a#u$_y$6vmf-=@z$x2z#q-=(+ono)dt!uu!niol'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Application definition
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# Extra
	'django.contrib.syndication',
	'django.contrib.flatpages',
	'django.contrib.comments',
	'django.contrib.humanize',
	'django.contrib.sitemaps',
	'django.contrib.sites',

	# This is South, intelligent schema and data
	# migrations for ​Django projects.
	'south',

	# This is {{ project_name }} root module, place where
	# I set my applications.
	'{{ project_name }}',

	# This is {{ project_name }} tags application, place where
	# I track content links.
	'tags',

	# This is {{ project_name }} news application, place where
	# I will post my news.
	'news',

	# This is {{ project_name }} blog application, place where
	# I will post my articles.
	'stream',

	# This is {{ project_name }} labs application, place where
	# I will post my experiments.
	'labs',

	# This is {{ project_name }} contact application, place where
	# I will receive my mails.
	'contact',
)
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	# Cookie-based, for anonymous users
	'django.middleware.locale.LocaleMiddleware',
)
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
	}
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Templates
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TEMPLATE_CONTEXT_PROCESSORS = [
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
]

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = [
	os.path.join(ROOT_DIR, 'templates'),
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
GULPFILE = os.path.join(ROOT_DIR, 'static/gulpfile.js')
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(ROOT_DIR, 'static')
]
