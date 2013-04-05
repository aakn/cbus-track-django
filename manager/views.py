import json, urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapsapi.models import MapsAPIUsageCounter, MapsAddressCache# Create your views here.

def show_stats(request):
	from django.db.models import Count
	count = MapsAPIUsageCounter.objects.extra({'date' : "date(time)"}).values('date').annotate(counter=Count('id'))

	return render_to_response('manager/count.html', {'counter': count,})