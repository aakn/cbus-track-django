from mapsapi.models import MapsAddressCache, MapsAPIUsageCounter
import json, urllib2
from django.utils import simplejson

def check_cache(lat, lng):

	lat = float(lat)
	lat = "%.3f" % lat

	lng = float(lng)
	lng = "%.3f" % lng

	address_arr = MapsAddressCache.objects.filter(lat=lat).filter(lng=lng)

	if len(address_arr) == 0:
		# Getting address from the maps api
		address = get_address_from_maps_api(lat, lng)
		if address == 'null':
			return simplejson.dumps({'address': 'null'})
		entry = MapsAddressCache(lat=lat, lng=lng, address=address)
		entry.save()
	else:
		address = address_arr[0].address
	 
	address_json = simplejson.dumps({'address': address})
	return address_json


def get_address_from_maps_api(lat, lng):
	jsondata = json.load(urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true' % (lat, lng)))
	counter = MapsAPIUsageCounter()
	counter.save()
	try:
		address = jsondata['results'][0]['formatted_address']
	except IndexError:
		address = 'null'

	return address