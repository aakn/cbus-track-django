from track.models import BusTravelLog
from django.http import HttpResponse

def last_trip(request, bus = '1'):
	last = BusTravelLog.objects.get_last_trip(bus)
	return HttpResponse("%s" % last)