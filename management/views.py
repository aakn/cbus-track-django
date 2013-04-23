import json, urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapsapi.models import MapsAPIUsageCounter, MapsAddressCache# Create your views here.
from track.models import Balance, BusTravelLog, RouteDetail
from mapsapi.models import MapsAddressCache
from track.convert_coordinates import convert
import pusher, datetime
import math

def show_stats(request):# Create your views here.
	routes = RouteDetail.objects.all()
	return render_to_response('management/trip_map.html',{ 'page': 'stats', 'request': request, 'routes': routes, })

def deg2rad(deg):
		return (float(deg) * float(math.pi)/ float(180.0));

def rad2deg(rad):
		return (rad * 180.0 / math.pi);


def computedisplacement(lat1,lon1,lat2,lon2):
	theta=float(lon1)-float(lon2)
	dist= math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2)) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.cos(deg2rad(theta))
	#dist=math.floor(dist*100)/100
	if dist > 1.0 : 
		return 0.0
	else : 
		dist = math.acos(dist)
		dist = rad2deg(dist)
		dist = dist * 60 * 1.1515
		dist = dist * 1.609344
		return dist

def daily_stats(request):
	log_per_day = []
	log_per_bus = []
	delta = datetime.timedelta(days=-1)
	temp=[]	

	num_of_buses=RouteDetail.objects.count()

	for ctr in range(1,num_of_buses+1):

		dateobj = datetime.datetime.now()
		log_per_day = []
		for i in range(5):
			morning_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,05,00)
			morning_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,9,00)
			evening_lower_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,15,00)
			evening_upper_threshold = datetime.datetime(dateobj.year,dateobj.month,dateobj.day,20,00)	

			bus_name=RouteDetail.objects.get(pk=ctr)
			morning_query = BusTravelLog.objects.filter(time__gt=morning_lower_threshold).filter(valid="YES").filter(time__lt=morning_upper_threshold).filter(bus_id=ctr)
			evening_query = BusTravelLog.objects.filter(time__gt=evening_lower_threshold).filter(valid="YES").filter(time__lt=evening_upper_threshold).filter(bus_id=ctr)
			counter=0;
			morn_dist=0;
			temp.append(str(dateobj)+" morning")
			for ctr2 in morning_query:
				if counter == 0 :
					lastlat=ctr2.lat
					lastlon=ctr2.lon
					start_time=ctr2.time
				else :
					val=computedisplacement(ctr2.lat, ctr2.lon, lastlat, lastlon)
					morn_dist=morn_dist+val
					lastlat=ctr2.lat
					lastlon=ctr2.lon
					temp.append(str(ctr2.lat)+" "+str(ctr2.lon)+" "+lastlat+" "+lastlon+" "+str(val))
					end_time=ctr2.time
				counter=counter+1
			if counter > 0 :	
				morn_time=end_time-start_time	
			else :
				morn_time=0
			even_dist=0;	
			counter=0;	
			temp.append("**************************"+str(dateobj)+" morning = "+str(morn_dist))

			temp.append(str(dateobj)+" evening")
			for ctr2 in evening_query:
				if counter == 0 :
					lastlat=ctr2.lat
					lastlon=ctr2.lon
					start_time=ctr2.time
				else :
					val=computedisplacement(ctr2.lat, ctr2.lon, lastlat, lastlon)
					even_dist=even_dist+val
					lastlat=ctr2.lat
					lastlon=ctr2.lon
					end_time=ctr2.time
					temp.append(str(ctr2.lat)+" "+str(ctr2.lon)+" "+lastlat+" "+lastlon+" "+str(val))
				counter=counter+1
			if counter > 0 :
				even_time=end_time-start_time
			else :
				even_time=0
			temp.append("**************************"+str(dateobj)+" evening = "+str(even_dist))
			morn_dist=math.ceil(morn_dist*100)/100
			even_dist=math.ceil(even_dist*100)/100	
			morn_time=morn_time.hour+" hours "+morn_time.minute+" minutes"
			data = {
				'name' : str(bus_name.number),
				'date' : str(evening_upper_threshold.strftime("%B %d, %Y")),
				'morning' : morn_dist,
				'evening' : even_dist,
				'morningtime' : morn_time,
				'eveningtime' : even_time,
			}
			dateobj = dateobj + delta
			log_per_day.append(data)
		final_log = {
				'buslogger' : log_per_day ,
				'name' : str(bus_name.number)

		}
		log_per_bus.append(final_log)
#	return HttpResponse("<br>".join(temp))
	return render_to_response('management/daily_stats.html', {'buslog': log_per_bus, 'request':request,})