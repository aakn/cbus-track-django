from django.conf.urls import patterns, url

urlpatterns = patterns('track.ajax_view',
    url(r'^last_trip/(?P<bus>\d+)/$', 'last_trip'),
    url(r'^last_trip/(?P<bus>\d+)/(?P<limit>\d+)/$', 'last_trip'),
    url(r'^current_trip/(?P<bus>\d+)/$', 'current_trip'),
)