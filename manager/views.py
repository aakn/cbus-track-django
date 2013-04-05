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
	count = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id')).order_by('-id')[:5]

	#return render_to_response('manager/count.html', {'counter': count,})
	log = []
	log_maps =[]
	delta = datetime.timedelta(days=-1)
	dateobj = datetime.datetime.now()

	for i in range(5):
		morning_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
		morning_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
		evening_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,15,00)
		evening_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,20,00)	

		morning_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=morning_lower_threshold).filter(time__lt=morning_upper_threshold).annotate(counter=Count('id'))
		evening_query = BusTravelLog.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=evening_lower_threshold).filter(time__lt=evening_upper_threshold).annotate(counter=Count('id'))
		morning_maps_query = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=morning_lower_threshold).filter(time__lt=morning_upper_threshold).annotate(counter=Count('id')).order_by('-id')[:5]
		evening_maps_query = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').filter(time__gt=evening_lower_threshold).filter(time__lt=evening_upper_threshold).annotate(counter=Count('id')).order_by('-id')[:5]

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
			'date' : str(evening_upper_threshold.strftime("%B %d, %Y")),
			'morning' : morning_count,
			'evening' : evening_count,
			'total' : total_count,
		}
		log.append(data)
		dateobj = dateobj + delta

		if(len(morning_maps_query) > 0):
			morning_maps_count = morning_maps_query[0]['counter']
		else:
			morning_maps_count = 0

		if(len(evening_maps_query) > 0):
			evening_maps_count = evening_maps_query[0]["counter"]
		else:
			evening_maps_count = 0

		total_maps_count = morning_maps_count+ evening_maps_count
		data_maps = {
			'date' : str(evening_upper_threshold.strftime("%B %d, %Y")),
			'morning' : morning_maps_count,
			'evening' : evening_maps_count,
			'total' : total_maps_count,
		}
		log_maps.append(data_maps)
		dateobj = dateobj + delta
	
	#return render_to_response('track/daily_count.html', {'counter': log, 'request':request,})
	return render_to_response('manager/count.html', {'counter': log, 'request':request,'counter2' : log_maps})