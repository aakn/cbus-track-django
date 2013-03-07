from track.models import BusTravelLog
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json, urllib2

def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse("%s" % last)

def current_trip(request, bus = '1'):
	return render_to_response('current_trip.html', {'bus': bus})

def get_address(request, lat, lng):
	jsondata = json.load(urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true' % (lat, lng)))
	from django.utils import simplejson
	jsonreturn = simplejson.dumps({'address': jsondata['results'][0]['formatted_address']})
	return HttpResponse(jsonreturn)

def get_time_and_distance(request, lat1, lng1, lat2, lng2):
	jsondata = json.load(urllib2.urlopen('http://maps.googleapis.com/maps/api/directions/json?origin=%s,%s&destination=%s,%s&sensor=true' % (lat1, lng1, lat2, lng2)))
	from django.utils import simplejson
	jsonreturn = simplejson.dumps({
		'distance': jsondata['routes'][0]['legs']['distance']['text'],
		'duration': jsondata['routes'][0]['legs']['duration']['text'],
		})
	return HttpResponse(jsonreturn)	