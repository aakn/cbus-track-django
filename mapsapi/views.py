import json, urllib2
from django.http import HttpResponse
from mapsapi.models import MapsAPIUsageCounter

def get_address(request, lat, lng):
	jsondata = json.load(urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true' % (lat, lng)))
	counter = MapsAPIUsageCounter()
	counter.save()
	from django.utils import simplejson
	jsonreturn = simplejson.dumps({'address': jsondata['results'][0]['formatted_address']})
	return HttpResponse(jsonreturn)

def get_time_and_distance(request, lat1, lng1, lat2, lng2):
	jsondata = json.load(urllib2.urlopen('http://maps.googleapis.com/maps/api/directions/json?origin=%s,%s&destination=%s,%s&sensor=true' % (lat1, lng1, lat2, lng2)))
	counter = MapsAPIUsageCounter()
	counter.save()
	from django.utils import simplejson
	jsonreturn = simplejson.dumps({
		'distance': jsondata['routes'][0]['legs']['distance']['text'],
		'duration': jsondata['routes'][0]['legs']['duration']['text'],
		})
	return HttpResponse(jsonreturn)	