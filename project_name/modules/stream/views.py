# -*- coding: utf-8 -*-

from django import http
from django.conf import settings
from django.shortcuts import render
from django.template import Context, loader

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# root
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stream(request, template_name='scaffold/stream.html'):
	"""
	Main page
	"""
	return render(request, template_name, {
		'ROOT_DIR': settings.ROOT_DIR,
		'BASE_DIR': settings.BASE_DIR,
	})
