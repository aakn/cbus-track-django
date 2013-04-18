from django.conf.urls import patterns, url

urlpatterns = patterns('management.views',
	url(r'', 'show_stats'),
)
