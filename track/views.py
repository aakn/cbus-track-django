from django.http import HttpResponse
from django.shortcuts import render_to_response
from track.models import Balance, BusTravelLog, RouteDetail
from mapsapi.models import MapsAddressCache
from track.convert_coordinates import convert
import pusher, datetime
from track import SocketBox, gcm, process


def stats(request):
	routes = RouteDetail.objects.all()
	return render_to_response('track/stats.html', { 'page': 'stats', 'request': request, 'routes': routes, })

def index(request):
	routes = RouteDetail.objects.all()
	return render_to_response('track/index.html', { 'page': 'home', 'request': request, 'routes': routes, })

def about(request):
	return render_to_response('track/about.html', { 'page': 'about', 'request': request })

def add(request, bus, lat, lon, speed, balance, valid='A'):
	speed = float(speed)
	speed = round(speed*1.852)

	if valid[-1:] == '/':
		valid = valid[:-1]

	if valid == "A":
		valid = "YES"
	else:
		valid = "NO"

	lat = convert(lat)
	lon = convert(lon)

	route = RouteDetail.objects.get(pk=bus)
	log = BusTravelLog(bus=route, lat=lat, lon=lon, speed=speed, valid=valid)
	log.save()
	#bal = Balance(bus=route, balance=balance)
	#bal.save()
	if valid == 'NO':
		return HttpResponse("Invalid")

	address = MapsAddressCache.objects.get_address(lat, lon)

	# PUSHER CODE
	data = {
		'bus_id': bus,
		'lat': lat,
		'lon': lon,
		'time': str(datetime.datetime.now())[:19],
		'speed': speed,
		'address': address,
	}

	pusher.app_id = '37147'
	pusher.key = '38c410e14df2239c04ab'
	pusher.secret = '1d1ce5aa951f5eb5350a'
	p = pusher.Pusher()
	p['track-channel'].trigger('bus-moved', data)


	# Custom Socket Function
	SocketBox.trigger('track-channel', 'bus-moved', data)

	# Process the new coordinate
	process.process_new_coordinate(route.number, lat, lon)
	

	return HttpResponse("Success")

def deploy(request):
	# Commands
	commands = [
		'echo $PWD',
		'whoami',
		'git pull',
		'git status',
		'git submodule sync',
		'git submodule update',
		'git submodule status',
	]
	text = ""
	import subprocess
	for command in commands:
		proc = subprocess.Popen(command,
			shell=True,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
		)
		stdout_value, stderr_value = proc.communicate('through stdin to stdout')
		text+=str(repr(stdout_value)) + "<br/>"
		text+=str(repr(stderr_value)) + "<br/>"
		# print '\tstderr      :', repr(stderr_value)
		# text += str(result)+"<br/>"

	return HttpResponse("%s" % text)

def socketbox_test(request):
	data = {
		'bus_id': '1',
		'lat': 12.8980033333,
		'lon': 77.5863583333,
		'time': str(datetime.datetime.now())[:19],
		'speed': '66',
		'address': '{"address": "G-02, Rose Garden Road, JP Nagar 5th Phase, Bangalore, Karnataka 560078, India"}',
	}
	
	result = SocketBox.trigger('track-channel', 'bus-moved', data)
	return HttpResponse(result)

def gcm_test(request):

	result = process.process_new_coordinate('KA 41 38', 13.01467, 77.555025)

	# reg_id = [
	# 	'APA91bFVPSD2W4cLyg9JLOcHfQyXcbnqdUfPwUMjWVTQsE0N3my5lI_Iyht1fpnFIRAPbwWwK2vhTbaca1FPkP2ZFVih0wKXxpRrrlik6qPsat4GUuAvZ7hcxbL0nQTwylmjfGrRAm1bXISKSGSeVP-5iAVs03rj3g'
	# ]
	# data = {
	# 	"data" : 'hello world',
	# 	"message": "a message",
	# }
	# result = result + "  " + gcm.make_request(reg_id, data)
	return HttpResponse(result)

def php_add(request):
	if 'id' in request.GET:
		bus = request.GET['id']
	else:
		bus = 1

	if 'text' in request.GET:
		text = request.GET['text']
	else:
		text = " $ "
	if 'speed' in request.GET:
		speed = request.GET['speed']
	else:
		speed = ""
	if 'bal' in request.GET:
		balance = request.GET['bal']
	else:
		balance = ""
	if 'v' in request.GET:
		valid = request.GET['bal']
	else:
		valid = "A"


	text = text.split('$')
	lat = text[0]
	lon = text[1]

	add(request, bus, lat, lon, speed, balance, valid)
	return HttpResponse("1")	

#prash added
def daily_req(request):
	from django.db.models import Count
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
	
	return render_to_response('track/daily_count.html', {'counter': log, 'request':request,})