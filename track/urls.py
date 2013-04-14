from django.conf.urls import patterns, url

urlpatterns = patterns('track.views',
	# for legacy code
	url(r'^php/log.php$', 'php_add'),
	# for updating via git
	url(r'^deploy/$', 'deploy'),
	
	# for basic views
	url(r'^$', 'index', {}, name='home_url_name'),
	url(r'^stats/$', 'stats', {}, name='stats_url_name'),
	url(r'^about/$', 'about', {}, name='about_url_name'),

	# for adding location data into the database
	url(r'^add/(?P<bus>\d+)/(?P<lat>(\d*[.])?\d+([A-Za-z])?)/(?P<lon>(\d*[.])?\d+([A-Za-z])?)/(?P<speed>(\d*[.])?\d+)/(?P<valid>[A-Z]?)/(?P<balance>[\d\w\.\$\-_% ]*)/$', 'add'),

	# for checking the number of daily requests made to the server
    url(r'^dailyreq/$', 'daily_req'),

    # for testing custom sockets
    # remove this during production
    url(r'^test/$', 'socket_test'),
)

urlpatterns += patterns('track.app_views',
	url(r'^bus_stop/add/$', 'add_bus_stop'),
    url(r'^user/add/$', 'add_user'),
    url(r'^user/(?P<user_id>\d+)/update/stop/$', 'update_user_stop'),
)