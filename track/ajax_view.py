from track.models import BusTravelLog
from django.http import HttpResponse
from django.shortcuts import render_to_response

def last_trip(request, bus = '1'):
	last = BusTravelLog.objects.get_last_trip(bus)
	return HttpResponse("%s" % last)

def current_trip(request, bus = '1'):
	return render_to_response('current_coord.html', {'bus': bus})