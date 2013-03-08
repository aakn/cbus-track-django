# import datetime
from track.models import BusTravelLog
from django.utils import simplejson

def my_calc_func(bus, limit):
	timeset = BusTravelLog.objects.filter(bus=bus).order_by('-time')[:1]
	for item in timeset:
		time = item.time
	time = time.date()
	if limit == 0:
		logs = BusTravelLog.objects.filter(time__startswith=time).filter(bus=bus).order_by('-time')
	else:
		logs = BusTravelLog.objects.filter(time__startswith=time).filter(bus=bus).order_by('-time')[:limit]

	log_list = []
	prev_time = ""
	for o in logs:
		curr = {
			'lat': o.lat, 
			'speed': o.speed, 
			'lon': o.lon, 
			'time': str(o.time)[:19],
		}
		hour = 1*60*60;
		if prev_time == "":
			prev_time = o.time
		elif (prev_time - o.time).seconds >= hour :
			break
		log_list.append(curr)

	json = simplejson.dumps(log_list, sort_keys=True, indent=4)
	return json

def my_calc_func_old(bus):
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
