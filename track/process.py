from track.models import BusStop, User

def process_new_coordinate(bus_number, lat, lon):
	stops = BusStop.objects.all()
	for stop in stops:
		distance = is_close(lat, lon, stop.lat, stop.lon)
		if distance != 0:
			send_update(stop, distance, bus_number)

	return "Done"

def is_close(current_lat, current_lon, stop_lat, stop_lon):
	return True

def send_update(stop, distance, bus_number):
	users = User.objects.filter(stop=stop)
	gcm_list = []
	for user in users:
		gcm_list.append(user.gcm)

	# Send update via GCM to all the User