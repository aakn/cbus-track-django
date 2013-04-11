import urllib, urllib2
from django.utils import simplejson

def trigger(channel, event, data):
	socket_data = {
		'event' : event,
		'channel' : channel,
		'data' : simplejson.dumps(data),
	}

	host = 'http://50.62.76.127';
	result = urllib2.urlopen(host+'/post/', urllib.urlencode(socket_data))
	content = result.read()

	return content