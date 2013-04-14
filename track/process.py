from track.models import BusStop, User
import datetime
from track import gcm
from math import radians, cos, sin, asin, sqrt

def process_new_coordinate(bus_number, lat, lon):
	allstops = BusStop.objects.all()
	stops = []

	response = ""

	for stop in allstops:
		users = User.objects.filter(stop=stop)
		if len(users) > 0:
			stops.append(stop)

	for stop in stops:
		distance = haversine(lat, lon, float(stop.lat), float(stop.lon))
		if distance != 0:
			response = response + " " + send_update(stop, distance, bus_number)

	return response

def is_close(current_lat, current_lon, stop_lat, stop_lon):
	return 10

def send_update(stop, distance, bus_number):
	current_date_time = datetime.datetime.now()
	users = User.objects.filter(stop=stop).filter(notify=True)
	gcm_list = []
	for user in users:
		difference = current_date_time - user.last_update_time
		seconds = difference.seconds

		if float(user.min_distance) >= float(distance) and seconds > 0*3600:
			gcm_list.append(user.gcm)

	
	if len(gcm_list) == 0:
		return "No one is close enough"

	message = "Your bus %s, is currently %s KMs away." % (bus_number, distance)
	data = {
		'message' : message,
	}

	# Send update via GCM to all the User
	return message + " " + gcm.make_request(gcm_list, data)
	# return message

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km 