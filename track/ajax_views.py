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
	log = []
	delta = datetime.timedelta(days=-1)
	dateobj = datetime.datetime.now()

	for i in range(5):
		morning_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
		morning_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
		evening_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,15,00)
		evening_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,20,00)	

		morning_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=morning_lower_threshold).filter(time__lt=morning_upper_threshold).annotate(counter=Count('id'))
		evening_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=evening_lower_threshold).filter(time__lt=evening_upper_threshold).annotate(counter=Count('id'))

		if(len(morning_query) > 0):
			morning_count = morning_query[0]['counter']
		else:
			morning_count = 0

		if(len(evening_query) > 0):
			evening_count = evening_query[0]["counter"]
		else:
			evening_count = 0

		total_count = morning_count+ evening_count
		data = {
			'date' : str(evening_upper_threshold.date()),
			'morning' : morning_count,
			'evening' : evening_count,
			'total' : total_count,
		}
		log.append(data)
		dateobj = dateobj + delta
	
	return render_to_response('dailyrequests/count.html', {'counter': log,})
