import json
import urllib.request
import os
from os import environ
import math
import tweepy as tp
from time import sleep

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_secret = environ['access_secret']

text = "Look to the skies! The ISS is over Houston!"

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#center_lon and center_lat JSC coordinates
#latitude: 1 deg = 110.574km
#longitude: 1 deg = 111.320*cos(latitude)km
#radius of visibility = 2316.4km = 20.949deg [lat] = 20.808*cos(lat)deg [lon]
#center_lon = -95.093186
#center_lat = 29.552839
#random changes

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    x = lon
    y = lat
    if ((math.sqrt((1-(((y-29.7604) ** 2) / ((20.9485) ** 2))) * ((23.97) ** 2))-(95.3698))) >= x >= (((-math.sqrt((1-(((y-29.7604) ** 2) / ((20.9485) ** 2))) * ((23.97) ** 2)))-(95.3698))):
        print("yay", lat, lon)
        api.update_status(text)
        sleep(1800)
    else:
        print("nay", lat, lon)
        sleep(5)



 
