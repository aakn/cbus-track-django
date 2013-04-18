from django.conf.urls import patterns, url

urlpatterns = patterns('track.ajax_views',
    url(r'^last_trip/(?P<bus>\d+)/$', 'last_trip'),
    url(r'^buses_status/$', 'buses_status'),    
    url(r'^last_trip/(?P<bus>\d+)/(?P<limit>\d+)/$', 'last_trip'),
    url(r'^trip/(?P<bus>\d+)/(?P<date>\S+)/$', 'trip'),
    url(r'^current_trip/(?P<bus>\d+)/$', 'current_trip'),
    url(r'^list_of_stops/(?P<bus_number>\d+)/$', 'list_of_stops'),
    url(r'^list_of_routes/$', 'list_of_routes'),
    # url(r'^add_bus_stop/(?P<bus_number>\d+)/(?P<stop_name>[\d\w\.\$\-%_ ]+)/(?P<lat>(\d*[.])?\d+([A-Za-z])?)/(?P<lon>(\d*[.])?\d+([A-Za-z])?)/$', 'add_bus_stop'),
    # url(r'^add_user/(?P<name>[\d\w\.\- ]+)/(?P<stop_id>\d+)/(?P<gcm_id>[\d\w\-_]+)/$', 'add_user'),
    # url(r'^update_user/(?P<user_id>\d+)/(?P<name>[\d\w\.\- ]+)/(?P<stop_id>\d+)/(?P<gcm_id>[\d\w\-_]+)/$', 'update_user'),
)
