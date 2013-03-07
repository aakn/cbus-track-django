from django.conf.urls import patterns, url

urlpatterns = patterns('track.ajax_view',
    url(r'^last_trip/(?P<bus>\d+)/$', 'last_trip'),
    url(r'^last_trip/(?P<bus>\d+)/(?P<limit>\d+)/$', 'last_trip'),
    url(r'^current_trip/(?P<bus>\d+)/$', 'current_trip'),
    url(r'^get_address/(?P<lat>(\d*[.])?\d+)/(?P<lng>(\d*[.])?\d+)/$', 'get_address'),
    url(r'^get_time_and_distance/(?P<lat1>(\d*[.])?\d+)/(?P<lng1>(\d*[.])?\d+)/(?P<lat2>(\d*[.])?\d+)/(?P<lng2>(\d*[.])?\d+)/$', 'get_time_and_distance'),
)