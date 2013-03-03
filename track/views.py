from django.http import HttpResponse
from track.models import Balance, BusTravelLog, RouteDetail
from django.shortcuts import render_to_response
import pusher, datetime


def stats(request):
	return render_to_response('index.html', { 'page': 'home' })

def add(request, bus, lat, lon, speed, balance):
	route = RouteDetail.objects.get(pk=bus)
	log = BusTravelLog(bus=route, lat=lat, lon=lon, speed=speed)
	log.save()
	bal = Balance(bus=route, balance=balance)
	bal.save()

	pusher.app_id = '37147'
	pusher.key = '38c410e14df2239c04ab'
	pusher.secret = '1d1ce5aa951f5eb5350a'

	data = {
		'bus_id': bus,
		'lat': lat,
		'lon': lon,
		'time': str(datetime.datetime.now()),
		'speed': speed
	}
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
		result = subprocess.Popen(command, shell=True)
		text += str(result)+"<br/>"

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

	text = text.split('$')
	lat = text[0]
	lon = text[1]

	add(request, bus, lat, lon, speed, balance)
	return HttpResponse("1")
