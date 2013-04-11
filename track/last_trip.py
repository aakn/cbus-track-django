# import datetime
from track.models import BusTravelLog
from django.utils import simplejson

def my_calc_func(bus, limit, return_as_object=False):
	timeset = BusTravelLog.objects.filter(bus=bus).order_by('-time')[:1]
	for item in timeset:
		time = item.time
	time = time.date()
	if limit == 0:
		logs = BusTravelLog.objects.filter(time__startswith=time).filter(bus=bus).order_by('-time')
	else:
		logs = BusTravelLog.objects.filter(time__startswith=time).filter(bus=bus).order_by('-time')[:limit]

	log_list = []
	hour = 1*60*60

	prev_time = ""
	for o in logs:
		curr = {
			'lat': o.lat, 
			'speed': o.speed, 
			'lon': o.lon, 
			'time': str(o.time)[:19],
		}
		
		if prev_time == "":
			prev_time = o.time
		elif (prev_time - o.time).seconds >= hour :
			# return (str(o.time),(prev_time - o.time).seconds)
			break
		else:
			prev_time = o.time
		log_list.append(curr)

	if return_as_object:
		# caller doesnt want the json, but the raw object.
		return log_list

	# by default return json
	json = simplejson.dumps(log_list, check_circular=False)
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