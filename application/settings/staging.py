# -*- coding: utf-8 -*-

# Get default settings
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'My {{ project_name }}, secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
