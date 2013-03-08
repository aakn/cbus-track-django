from django.contrib import admin
from mapsapi.models import MapsAPIUsageCounter, MapsAddressCache

class MapsAPIUsageCounterAdmin(admin.ModelAdmin):
	list_display = ('time',)
	list_filter = ('time',)
	date_hierarchy = 'time'
	ordering = ('-time',)

class MapsAddressCacheAdmin(admin.ModelAdmin):
	list_display = ('lat', 'lng', 'address', 'time')
	list_filter = ('time',)
	date_hierarchy = 'time'
	ordering = ('-time',)

admin.site.register(MapsAPIUsageCounter, MapsAPIUsageCounterAdmin)
admin.site.register(MapsAddressCache, MapsAddressCacheAdmin)