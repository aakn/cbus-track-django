import json, urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapsapi.models import MapsAPIUsageCounter, MapsAddressCache

def get_address(request, lat, lng):
	address = MapsAddressCache.objects.get_address(lat, lng)
	return HttpResponse(address)

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

def get_counter(request):
	burp
	from django.db.models import Count
	count = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id'))

	return render_to_response('mapsapi/count.html', {'counter': count,})
