from track.models import BusStop, RouteDetail, User
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt                                          

@csrf_exempt
def add_bus_stop(request):
	if request.method == 'POST':
		if 'bus_id' in request.POST and 'lat' in request.POST and 'lng' in request.POST and 'stop_name' in request.POST:
			bus_id = request.POST['bus_id']
			lat = request.POST['lat']
			lng = request.POST['lng']
			stop_name = request.POST['stop_name']
			route = RouteDetail.objects.get(pk=bus_id)
			stop = BusStop(route, lat, lng, stop_name)
			stop.save()
			return HttpResponse(simplejson.dumps({'status' : "success"}))
	return HttpResponse(simplejson.dumps({'status' : "fail"}))


@csrf_exempt
def add_user(request):
	if request.method == 'POST':
		if 'name' in request.POST and 'gcm_id' in request.POST:
			name = request.POST['name']
			gcm_id = request.POST['gcm_id']

			user = User.objects.filter(gcm=gcm_id)

			if len(user) == 0:
				new_user = User(name=name, gcm=gcm_id)
				new_user.save()

				user = User.objects.filter(gcm=gcm_id)
			
			else:
				user.update(name=name)

			user_id = user[0].id
			return_json_object = {
				'status' : 'success',
				'user_id' : user_id,
			}
			return_json_string = simplejson.dumps(return_json_object)

			return HttpResponse(return_json_string)

	return_json_object = {
		'status' : 'fail',
	}
	return_json_string = simplejson.dumps(return_json_object)

	return HttpResponse(return_json_string)


@csrf_exempt
def update_user_stop(request, user_id):
	if request.method == 'POST':
		if 'stop_id' in request.method:
			stop_id = request.method['stop_id']

			stop = BusStop.objects.get(pk=stop_id)
			user = User.objects.filter(pk=user_id)

			if len(user) == 0:
				return HttpResponse(simplejson.dumps({'status' : "user_does_not_exist"}))

			user.update(stop=stop)

			return HttpResponse(simplejson.dumps({'status' : 'success'}))
	return HttpResponse(simplejson.dumps({'status' : 'fail'}))

