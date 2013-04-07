from track.models import BusTravelLog, BusStop, RouteDetail, User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
import json

def list_of_stops(request, bus_number):
	route = RouteDetail.objects.get(pk=bus_number)
	stops = BusStop.objects.filter(bus=route)
	stops_list = []
	for stop in stops:
		current_stop = {
			'id': str(stop.id),
			'name': str(stop.name),
			'lat': str(stop.lat),
			'lon': str(stop.lon),
		}
		stops_list.append(current_stop)
	json = simplejson.dumps(stops_list, check_circular=False)
	return HttpResponse(json)

def list_of_routes(request):
	routes = RouteDetail.objects.all()
	route_list = []
	for route in routes:
		current_route = {
			'id': route.id,
			'route_number': str(route.number),
		}
		route_list.append(current_route)
	json = simplejson.dumps(route_list, check_circular=False)
	return HttpResponse(json)

def buses_status(request):
	routes = RouteDetail.objects.all()
	bus_status = []
	for route in routes:
		last = BusTravelLog.objects.get_last_trip(route, int(1))	
		#last2=simplejson.loads(last[0])
		current_route = {
			'id': route.id,
			'status' : last
		}
		bus_status.append(current_route)
	json = simplejson.dumps(bus_status, check_circular=False)
	return HttpResponse(json)


def add_bus_stop(request, bus_number, stop_name, lat, lon):
	route = RouteDetail.objects.get(pk=bus_number)
	stop = BusStop(route, lat, lon, stop_name)
	stop.save()
	return HttpResponse("Done")

def add_user(request, name, stop_id, gcm_id):
	stop = BusStop.objects.get(pk=stop_id)
	user = User(stop, name, gcm_id)
	user.save()
	return HttpResponse("Done")

def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse(last)

def current_trip(request, bus = '1'):
	return render_to_response('track/current_trip.html', {'bus': bus})
	
