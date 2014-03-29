# -*- coding: utf-8 -*-

# Get default settings
from .base import *
import dj_database_url

# Feedback
ADMINS = [
    ('Me', 'my@mail.com'),
]

# Set Django's database settings to Heroku's environment variable
# DATABASE_URL or default to Sqlite if unable to find.
DATABASES['default'] = dj_database_url.config(default=os.environ.get(
    'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, '{{ project_name }}.sqlite3'))
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
