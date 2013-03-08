from mapsapi.models import MapsAddressCache

def check_cache(lat, lng):
	lat = float(lat)
	lat = "%.3f" % lat

	lng = float(lng)
	lng = "%.3f" % lng