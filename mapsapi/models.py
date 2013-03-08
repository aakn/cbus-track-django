from django.db import models

class MapsAPIUsageCounter(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % ( self.time )

class CacheManager(models.Manager):
	def get_address(self, lat, lng):
		from mapsapi.cache import check_cache
		return check_cache(lat, lng)

class MapsAddressCache(models.Model):
	lat = models.CharField(max_length=90)
	lng = models.CharField(max_length=90)
	time = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=1000)
	objects = CacheManager()

	def __unicode__(self):
		return "%s %s - %s" % ( self.lat, self.lng, self.address )