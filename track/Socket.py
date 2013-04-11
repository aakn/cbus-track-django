import urllib
import urllib2

def send_data(channel, event, data):
	socket_data = {
		'event' : event,
		'channel' : channel,
		'data' : data
	}

	result = urllib2.urlopen('http://http://50.62.76.127:4000/post/', urllib.urlencode(socket_data))
	content = result.read()

	return content