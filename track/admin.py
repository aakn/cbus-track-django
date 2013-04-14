from django.contrib import admin
from track.models import RouteDetail, BusTravelLog, Balance, User, BusStop

class RouteDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')

class BusTravelLogAdmin(admin.ModelAdmin):
	list_display = ('bus', 'lat', 'lon', 'speed', 'time', 'valid')
	list_filter = ('time',)
	date_hierarchy = 'time'
	ordering = ('-time',)

class BalanceAdmin(admin.ModelAdmin):
	list_display = ('bus', 'time', 'balance')
	list_filter = ('time',)
	date_hierarchy = 'time'
	ordering = ('-time',)

class BusStopAdmin(admin.ModelAdmin):
	list_display = ('bus', 'name', 'lat', 'lon')

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'stop', 'notify', 'min_distance', 'min_time', 'last_update_time')

admin.site.register(RouteDetail, RouteDetailAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(BusTravelLog, BusTravelLogAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(BusStop, BusStopAdmin)