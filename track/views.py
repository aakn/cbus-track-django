from django.http import HttpResponse
from django.shortcuts import render_to_response
from track.models import Balance, BusTravelLog, RouteDetail
from mapsapi.models import MapsAddressCache
from track.convert_coordinates import convert
import pusher, datetime

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

	MapsAddressCache.objects.get_address(lat, lon)

	log.save()
	bal = Balance(bus=route, balance=balance)
	bal.save()

	# PUSHER CODE
	data = {
		'bus_id': bus,
		'lat': lat,
		'lon': lon,
		'time': str(datetime.datetime.now())[:19],
		'speed': speed
	}

	pusher.app_id = '37147'
	pusher.key = '38c410e14df2239c04ab'
	pusher.secret = '1d1ce5aa951f5eb5350a'
	p = pusher.Pusher()
	p['track-channel'].trigger('bus-moved', data)

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