import urllib
import urllib2
from django.utils import simplejson

def send_gcm_message(api_key, reg_id, data, collapse_key=None):

	values = {
		"registration_id": reg_id,
		"collapse_key": collapse_key,
	}

	for k, v in data.items():
		values["data.%s" % k] = v.encode('utf-8')

	data = urllib.urlencode(values)

	headers = {
		'UserAgent': "GCM-Server",
		'Content-Type': 'application/json',
		'Authorization': 'key=' + api_key,
		'Content-Length': str(len(data))
	}

	request = urllib2.Request("https://android.googleapis.com/gcm/send", data, headers)
	response = urllib2.urlopen(request)
	result = response.read()

	return result


def make_request(api_key, reg_id, data, collapse_key=None):
	json_data = {"collapse_key" : "msg", 
			"data" : data, 
		"registration_ids": reg_id,
	}
	url = 'https://android.googleapis.com/gcm/send'
	myKey = api_key
	data = simplejson.dumps(json_data)
	headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	
	result = response.read()
	return result