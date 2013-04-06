import json, urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapsapi.models import MapsAPIUsageCounter, MapsAddressCache# Create your views here.
from track.models import Balance, BusTravelLog, RouteDetail
from mapsapi.models import MapsAddressCache
from track.convert_coordinates import convert
import pusher, datetime

def show_stats(request):
	from django.db.models import Count
	#count = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id')).order_by('-id')[:5]

	#return render_to_response('manager/count.html', {'counter': count,})
	log= []
	log_per_bus=[]
	log_maps =[]
	delta = datetime.timedelta(days=-1)
	

	num_of_buses=RouteDetail.objects.count()

	for ctr in range(1,num_of_buses+1):

		dateobj = datetime.datetime.now()
		for i in range(5):
			morning_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
			morning_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
			evening_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,15,00)
			evening_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,20,00)	

			bus_name=RouteDetail.objects.get(pk=ctr)
			morning_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=morning_lower_threshold).filter(time__lt=morning_upper_threshold).annotate(counter=Count('id')).filter(bus_id=ctr)
			evening_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=evening_lower_threshold).filter(time__lt=evening_upper_threshold).annotate(counter=Count('id')).filter(bus_id=ctr)
	
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
				'name' : str(bus_name.number),
				'date' : str(evening_upper_threshold.strftime("%B %d, %Y")),
				'morning' : morning_count,
				'evening' : evening_count,
				'total' : total_count,
			}
			dateobj = dateobj + delta
			log_per_day.append(data)
		log.append(log_per_bus)

	
	#return render_to_response('track/daily_count.html', {'counter': log, 'request':request,})
	return render_to_response('manager/count.html', {'buslog': log, 'request':request,})