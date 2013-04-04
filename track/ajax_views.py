from track.models import BusTravelLog
from django.http import HttpResponse
from django.shortcuts import render_to_response

def list_of_stops(request):
	return HttpResponse("hi")
	
def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse(last)

def current_trip(request, bus = '1'):
	return render_to_response('current_trip.html', {'bus': bus})
	
