# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pages
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	url(r'^$', include('news.urls')),
    url(r'^work/', include('work.urls')),
    url(r'^labs/', include('labs.urls')),
    url(r'^stream/', include('stream.urls')),
    url(r'^contact/', include('contact.urls')),

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# admin
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://docs.djangoproject.com/en/dev/howto/static-files/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http status
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
handler400 = '{{ project_name }}.views.bad_request'
handler403 = '{{ project_name }}.views.permission_denied'
handler404 = '{{ project_name }}.views.page_error'
handler500 = '{{ project_name }}.views.server_error'

if getattr(settings, 'DEBUG', False):
	from django.core.urlresolvers import get_resolver
	errorresolve = get_resolver(None)
	urlpatterns += patterns('',
		url(r'400/$', *errorresolve.resolve400()),
		url(r'403/$', *errorresolve.resolve403()),
		url(r'404/$', *errorresolve.resolve404()),
		url(r'500/$', *errorresolve.resolve500()),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True
		}),
		url(r'', include('django.contrib.staticfiles.urls')),
	)
