from django.contrib.gis.GeoIP2 import GeoIP2
from geopy.distance import great_circle

def ip_location ():
	#given an IP address, returns latitude and longitude of that IP address
    # Return a tuple:
    # lat_long[0] = latitude, l[1] = longitude
    g = GeoIP2()
	ip = request.META.get('REMOTE_ADDR', None)
	if ip:
		#city = g.city(ip)['city']
    	lat_long = g.coords(ip)
	else:
    	#city = 'St. Louis' # default city
    	lat_long = (38.6270, 90.1994)
    return lat_long

def distanceCalc(lat_long1, business1):
    lat_long2   = (business1.latitude, business1.longitude)
    return (great_circle(lat_long1,lat_long2).miles)
