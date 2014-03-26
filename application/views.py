# -*- coding: utf-8 -*-

from django import http
from django.conf import settings
from django.shortcuts import render
from django.template import Context, loader

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bad_request(request, template_name='http/400.html'):
	"""
	400 error handler.
	"""
	template = loader.get_template(template_name)
	return http.HttpResponseServerError(template.render(Context({
		'BASE_DIR': settings.BASE_DIR,
		'request': request
	})))

def permission_denied(request, template_name='http/403.html'):
	"""
	403 error handler.
	"""
	template = loader.get_template(template_name)
	return http.HttpResponseServerError(template.render(Context({
		'BASE_DIR': settings.BASE_DIR,
		'request': request
	})))

def page_error(request, template_name='http/404.html'):
	"""
	404 error handler
	"""
	template = loader.get_template(template_name)
	return http.HttpResponseNotFound(template.render(Context({
		'BASE_DIR': settings.BASE_DIR,
		'request': request
	})))

def server_error(request, template_name='http/500.html'):
	"""
	500 error handler.
	"""
	template = loader.get_template(template_name)
	return http.HttpResponseServerError(template.render(Context({
		'BASE_DIR': settings.BASE_DIR,
		'request': request
	})))
