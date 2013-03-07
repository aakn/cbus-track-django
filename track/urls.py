from django.conf.urls import patterns, url

urlpatterns = patterns('track.views',
	# for legacy code
	url(r'^php/log.php/$', 'php_add'),
	# for updating via git
	url(r'^deploy/$', 'deploy'),
	url(r'^$', 'index', {}, name='home_url_name'),
	url(r'^stats/$', 'stats', {}, name='stats_url_name'),
	url(r'^about/$', 'about', {}, name='about_url_name'),
    url(r'^add/(?P<bus>\d+)/(?P<lat>(\d*[.])?\d+([A-Za-z])?)/(?P<lon>(\d*[.])?\d+([A-Za-z])?)/(?P<speed>(\d*[.])?\d+)/(?P<balance>[\d\w\.\$]+)/(?P<valid>([A-Z]/)?)$', 'add'),
)