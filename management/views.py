import datetime
import math

from django.shortcuts import render_to_response

from track.models import BusTravelLog, RouteDetail


def show_stats(request):  # Create your views here.
    routes = RouteDetail.objects.all()
    return render_to_response('management/trip_map.html', {'page': 'stats', 'request': request, 'routes': routes, })


def deg2rad(deg):
    return float(deg) * float(math.pi) / float(180.0)


def rad2deg(rad):
    return rad * 180.0 / math.pi


def computedisplacement(lat1, lon1, lat2, lon2):
    theta = float(lon1) - float(lon2)
    dist = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2)) + \
           math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.cos(deg2rad(theta))
    #dist=math.floor(dist*100)/100
    if dist > 1.0:
        return 0.0
    else:
        dist = math.acos(dist)
        dist = rad2deg(dist)
        dist = dist * 60 * 1.1515
        dist *= 1.609344
        return dist


def fetch_daily_stats(start_date):
    log_per_bus = []
    delta = datetime.timedelta(days=-1)
    temp = []
    if start_date is None or start_date == "":
        date_obj = datetime.datetime.now()
    else:
        date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")

    num_of_buses = RouteDetail.objects.count()

    for ctr in range(1, num_of_buses + 1):

        log_per_day = []
        for i in range(5):
            morning_lower_threshold = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 05, 00)
            morning_upper_threshold = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 9, 00)
            evening_lower_threshold = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 15, 00)
            evening_upper_threshold = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 20, 00)

            bus_name = RouteDetail.objects.get(pk=ctr)
            morning_query = BusTravelLog.objects.filter(time__gt=morning_lower_threshold).filter(valid="YES")\
                .filter(time__lt=morning_upper_threshold).filter(bus_id=ctr)
            evening_query = BusTravelLog.objects.filter(time__gt=evening_lower_threshold).filter(valid="YES")\
                .filter(time__lt=evening_upper_threshold).filter(bus_id=ctr)
            counter = 0
            morn_dist = 0
            morn_speed = 0
            temp.append(str(date_obj) + " morning")
            for ctr2 in morning_query:
                cur_speed = float(ctr2.speed)
                if counter == 0:
                    last_lat = ctr2.lat
                    last_lon = ctr2.lon
                    start_time = ctr2.time
                    morn_speed = cur_speed
                else:
                    val = computedisplacement(ctr2.lat, ctr2.lon, last_lat, last_lon)
                    morn_dist += val
                    last_lat = ctr2.lat
                    last_lon = ctr2.lon
                    temp.append(str(ctr2.lat) + " " + str(ctr2.lon) + " " + last_lat + " " + last_lon + " " + str(val))
                    end_time = ctr2.time
                    if morn_speed < cur_speed:
                        morn_speed = cur_speed
                counter += 1
            if counter > 0:
                morn_time = end_time - start_time
            else:
                morn_time = date_obj - date_obj
            even_dist = 0
            counter = 0
            even_speed = 0
            temp.append("**************************" + str(date_obj) + " morning = " + str(morn_dist))

            temp.append(str(date_obj) + " evening")
            for ctr2 in evening_query:

                cur_speed = float(ctr2.speed)
                if counter == 0:
                    last_lat = ctr2.lat
                    last_lon = ctr2.lon
                    start_time = ctr2.time
                    even_speed = cur_speed
                else:
                    val = computedisplacement(ctr2.lat, ctr2.lon, last_lat, last_lon)
                    even_dist += val
                    last_lat = ctr2.lat
                    last_lon = ctr2.lon
                    end_time = ctr2.time
                    if even_speed < cur_speed:
                        even_speed = cur_speed

                    temp.append(str(ctr2.lat) + " " + str(ctr2.lon) + " " + last_lat + " " + last_lon + " " + str(val))
                counter += 1
            if counter > 0:
                even_time = end_time - start_time
            else:
                even_time = date_obj - date_obj
            temp.append("**************************" + str(date_obj) + " evening = " + str(even_dist))
            morn_dist = math.ceil(morn_dist * 100) / 100
            even_dist = math.ceil(even_dist * 100) / 100
            #morn_time=morn_time.hour+" hours "+morn_time.minute+" minutes"
            if morn_time.seconds > 0:
                seconds = morn_time.seconds
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                morn_time = str(h) + " hours and " + str(m) + " minutes"
            else:
                morn_time = "Not travelled"
            if even_time.seconds > 0:
                seconds = even_time.seconds
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                even_time = str(h) + " hours and " + str(m) + " minutes"
            else:
                even_time = "Not Travelled"
            data = {
                'name': str(bus_name.number),
                'date': str(evening_upper_threshold.strftime("%B %d, %Y")),
                'morning': morn_dist,
                'evening': even_dist,
                'morning_time': morn_time,
                'evening_time': even_time,
                'morn_speed': morn_speed,
                'even_speed': even_speed
            }
            date_obj += delta
            log_per_day.append(data)
        final_log = {
            'bus_logger': log_per_day,
            'name': str(bus_name.number)

        }
        log_per_bus.append(final_log)
    return log_per_bus


def daily_stats(request):

    log_per_bus = fetch_daily_stats("2013-06-21")
    return render_to_response('management/daily_stats.html', {'bus_log': log_per_bus, 'request':request})