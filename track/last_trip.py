# import datetime
from track.models import BusTravelLog
from django.utils import simplejson

def my_calc_func(bus):
	timeset = BusTravelLog.objects.filter(bus=bus).order_by('-time')[:1]
	for item in timeset:
		time = item.time
	time = time.date()
	logs = BusTravelLog.objects.filter(time__startswith=time).filter(bus=bus).order_by('-time')
	json = simplejson.dumps([{
		'lat': o.lat, 
		'speed': o.speed, 
		'lon': o.lon, 
		'time': str(o.time)[:19],
		} 
		for o in logs])
	return json
