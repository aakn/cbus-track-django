from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/', include('track.ajax_urls')),
    url(r'^maps/', include('mapsapi.urls')),
    url(r'^manager/', include('manager.urls')),
    url(r'', include('track.urls')),
)

