from django.db import models

class MapsAPIUsageCounter(models.Model):
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s" % ( self.time )

	class Meta:
		verbose_name="Maps API Usage Counter"
		verbose_name_plural="Maps API Usage Counter"

class CacheManager(models.Manager):
	def get_address(self, lat, lng):
		from mapsapi.cache import check_cache
		return check_cache(lat, lng)

class MapsAddressCache(models.Model):
	lat = models.DecimalField(max_digits=10, decimal_places=3)
	lng = models.DecimalField(max_digits=10, decimal_places=3)
	time = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=1000)
	objects = CacheManager()

	def __unicode__(self):
		return "%s %s - %s" % ( self.lat, self.lng, self.address )

	class Meta:
		verbose_name="Maps API Cache"
		verbose_name_plural="Maps API Cache"
		ordering = ['-time']
		# Remember to update it in the database by using 
		# from south.db import db
		# db.create_index('mapsapi_mapsaddresscache', ['lat', 'lng'], unique=True)
		index_together = [
			["lat", "lng"],
		]
