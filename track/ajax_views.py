from track.models import BusTravelLog, BusStop, RouteDetail, User
from mapsapi.models import MapsAddressCache
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
import datetime
def list_of_stops(request, bus_number):
	route = RouteDetail.objects.get(pk=bus_number)
	stops = BusStop.objects.filter(bus=route)
	stops_list = []
	for stop in stops:

		users = User.objects.filter(stop=stop)

		current_stop = {
			'id': str(stop.id),
			'name': str(stop.name),
			'lat': str(stop.lat),
			'lon': str(stop.lon),
			'no_of_users' : len(users),
		}
		stops_list.append(current_stop)
	json = simplejson.dumps(stops_list, check_circular=False)
	return HttpResponse(json)


def list_of_routes(request):
	routes = RouteDetail.objects.all()
	route_list = []
	for route in routes:

		stops = BusStop.objects.filter(bus=route)
		no_of_users = 0

		for stop in stops:
			users = User.objects.filter(stop=stop)
			no_of_users = no_of_users + len(users)

		current_route = {
			'id': route.id,
			'route_number': str(route.number),
			'no_of_stops' : len(stops),
			'no_of_users' : no_of_users
		}
		route_list.append(current_route)
	json = simplejson.dumps(route_list, check_circular=False)
	return HttpResponse(json)


def buses_status(request):
	routes = RouteDetail.objects.all()
	bus_status = []
	for route in routes:
		last = BusTravelLog.objects.get_last_trip(route, int(1), True)
		last = last[0]
		lat = last['lat']
		lon = last['lon']	
		address = MapsAddressCache.objects.get_address(lat, lon)

		#last2=simplejson.loads(last[0])
		current_route = {
			'id' : route.id,
			'lat' : lat,
			'lon' : lon,
			'speed' : last['speed'],
			'time' : last['time'],
			'number' : route.number,
			'address' : address,
		}
		bus_status.append(current_route)
	json = simplejson.dumps(bus_status, check_circular=False)
	return HttpResponse(json)


def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse(last)
	

def trip(request, bus = '1', date='2013-04-18',morn_even='0'):
	#last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	#return HttpResponse(last)
	return HttpResponse("date is  "+date)
	dateobj=datetime.datetime.strptime(date, "%Y-%m-%d").date()
	dateobj = datetime.datetime.now()

	if(morn_even == '0'):
		lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
		upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
	else:
		lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,15,00)
		upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,20,00)
	result = BusTravelLog.objects.filter(time__gt=lower_threshold).filter(time__lt=upper_threshold).filter(bus_id=bus).filter(valid="YES").order_by('-time')
	log_list=[]
	for o in result:
		curr = {
			'lat': o.lat, 
			'speed': o.speed, 
			'lon': o.lon, 
			'time': str(o.time)[:19],
		}
		log_list.append(curr)
	json = simplejson.dumps(log_list, check_circular=False)	
	return HttpResponse(json)

def current_trip(request, bus = '1'):
	return render_to_response('track/current_trip.html', {'bus': bus})
	
