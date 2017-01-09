from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
import re, datetime, bcrypt, requests

api_key = 'AIzaSyAPyyCglxdj9LBrk0cklZFB6EQrrZNLUbk'

class geocode():
    def geo(address):
        geo = requests.post('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace(' ','+'),api_key), json={"key": "value"})
        return geo.json

    def place(search):
        geo = requests.post('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(search.replace(' ','+'),api_key), json={"key": "value"})
        geo_f = geo.json()
        # print(geo_f)
        # print(geo_f['results'][0]['place_id'])
        geo2 = requests.post('https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'.format(geo_f['results'][0]['place_id'],api_key), json={"key": "value"})

        return geo2.json()


api_key2 = '24f4931aaa798b5bb5ea5e03bca530c0'

class Weather():
   def DisplayCurrent(city):
       weather = requests.post('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,api_key2), json={"key": "value"})
       return weather.json
