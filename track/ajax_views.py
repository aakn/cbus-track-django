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
	dateobj=datetime.datetime.now()
	currdate=dateobj.date()
	t=datetime.time(07,00)
	log_list = []
	mornlowerdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day-2,05,00)
	mornupperdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day-2,9,00)
	evenlowerdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day-2,05,00)
	evenupperdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day-2,9,00)	
	count = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=lowerdate).filter(time__lt=upperdate).annotate(counter=Count('id'))
	#return render_to_response("The Date now is "+ str(currdate))
	log_list.append(count)

	mornlowerdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
	mornupperdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
	evenlowerdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
	evenupperdate=datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)	
	count = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=lowerdate).filter(time__lt=upperdate).annotate(counter=Count('id'))
	#return render_to_response("The Date now is "+ str(currdate))
	log_list.append(count)
	return render_to_response('dailyrequests/count.html', {'counter': count,})
