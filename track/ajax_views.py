from track.models import BusTravelLog
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
def last_trip(request, bus = '1', limit = '0'):
	last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	return HttpResponse(last)

def current_trip(request, bus = '1'):
	return render_to_response('current_trip.html', {'bus': bus})
	
#prash added
def daily_req(request):
	#last = BusTravelLog.objects.get_last_trip(bus, int(limit))
	#return HttpResponse("%s" % last)
	from django.db.models import Count
	#count = DailyRequestCounter.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id'))
	#return render_to_response('dailyrequests/count.html', {'counter': count,})
	#timeset = BusTravelLog.objects.filter(bus=1).filter(.order_by('-time')[:1]
	#for item in timeset: 
	#	time = item.time
	#time = time.date()
	#count =BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id'))
	count =BusTravelLog.objects.extra({'date' : "time(time)"}).values('date').annotate(distinct=True)
	#return render_to_response("The Date now is "+ str(currdate))
	return render_to_response('dailyrequests/count.html', {'counter': count,})
