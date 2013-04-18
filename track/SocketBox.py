import urllib, urllib2
from django.utils import simplejson

def trigger(channel, event, data):
	socket_data = {
		'event' : event,
		'channel' : channel,
		'data' : simplejson.dumps(data),
	}

	host = 'http://socket.insigniadevs.com:4000';
	try:
		result = urllib2.urlopen(host + '/post/', urllib.urlencode(socket_data))
		content = result.read()
	except Exception:
		content = "FAIL"
	return content