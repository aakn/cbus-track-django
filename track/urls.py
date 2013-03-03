from django.conf.urls import patterns, url

urlpatterns = patterns('track.ajax_view',
    url(r'^last_trip/(?P<bus>\d+)/$', 'last_trip'),
)