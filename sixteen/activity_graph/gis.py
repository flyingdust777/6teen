import re
import json
import geocoder
from urllib2 import urlopen
# aquires user IP address and returns longitude and latitude
def ip_location ():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    IP = re.compile(r'(\d+.\d+.\d+.\d+)').search(data).group(1)
    g = geocoder.ip(IP)
    return g.latlng
def distanceCalc(lat_long1, business1):
    lat_long2   = (business1.latitude, business1.longitude)
    return (great_circle(lat_long1,lat_long2).miles)