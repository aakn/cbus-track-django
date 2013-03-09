from track.models import BusTravelLog
from django.http import HttpResponse
from django.shortcuts import render_to_response

def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse(last, content_type="application/text")

def current_trip(request, bus = '1'):
	return render_to_response('current_trip.html', {'bus': bus})
