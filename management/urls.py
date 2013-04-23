from django.conf.urls import patterns, url

urlpatterns = patterns('management.views',
	
 url(r'^daily_stats/$', 'daily_stats'),
 url(r'', 'show_stats'),
)
