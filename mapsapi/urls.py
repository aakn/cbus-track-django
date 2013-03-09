from django.conf.urls import patterns, url

urlpatterns = patterns('mapsapi.views',
	url(r'^count/$', 'get_counter'),
    url(r'^get_address/(?P<lat>(\d*[.])?\d+)/(?P<lng>(\d*[.])?\d+)/$', 'get_address'),
    url(r'^get_time_and_distance/(?P<lat1>(\d*[.])?\d+)/(?P<lng1>(\d*[.])?\d+)/(?P<lat2>(\d*[.])?\d+)/(?P<lng2>(\d*[.])?\d+)/$', 'get_time_and_distance'),
)