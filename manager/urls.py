from django.conf.urls import patterns, url

urlpatterns = patterns('manager.views',
	url(r'^$', 'show_stats'),
)
