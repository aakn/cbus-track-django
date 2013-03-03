from django.contrib import admin
from track.models import RouteDetail, BusTravelLog, Balance

class RouteDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')

class BusTravelLogAdmin(admin.ModelAdmin):
	list_display = ('bus', 'lat', 'lon', 'speed', 'time')
	list_filter = ('time',)
	date_hierarchy = 'time'
	ordering = ('-time',)
	# filter_horizontal = ('bus_id',)

class BalanceAdmin(admin.ModelAdmin):
	list_display = ('bus', 'time', 'balance')
	ordering = ('-time',)

admin.site.register(RouteDetail, RouteDetailAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(BusTravelLog, BusTravelLogAdmin)