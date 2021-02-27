# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from server.apps.core import views as core_views

admin.autodiscover()

urlpatterns = [
    # django-admin:
    url(r'^admin/', admin.site.urls),
    url('^test_view/', core_views.TestView.as_view()),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: Z435
    from django.views.static import serve  # noqa: Z435

    urlpatterns = [
                      # URLs specific only to django-debug-toolbar:
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                      # noqa: DJ05

                      # Serving media files in development only:
                      url(r'^media/(?P<path>.*)$', serve, {
                          'document_root': settings.MEDIA_ROOT,
                      }),
                  ] + urlpatterns + staticfiles_urlpatterns()
