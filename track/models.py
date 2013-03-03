# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
# import datetime

class RouteDetail(models.Model):
    number = models.CharField(max_length=150)

    def __unicode__(self):
        return "%s" % ( self.number)

class Balance(models.Model):
    bus = models.ForeignKey(RouteDetail)
    time = models.DateTimeField(auto_now_add = True)
    balance = models.CharField(max_length=150)

    def __unicode__(self):
        return "%s %s %s" % (self.bus, self.balance, self.time)

class BusTravelLogManager(models.Manager):
    def get_last_trip(self, bus):
        from track.last_trip import my_calc_func
        return my_calc_func(bus)

class BusTravelLog(models.Model):
    bus = models.ForeignKey(RouteDetail)
    lat = models.CharField(max_length=90)
    lon = models.CharField(max_length=90)
    speed = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add = True)
    bal = models.CharField(max_length=15000)
    objects = BusTravelLogManager()

    def __unicode__(self):
        return "%s %s %s" % (self.lat, self.lon, self.time)