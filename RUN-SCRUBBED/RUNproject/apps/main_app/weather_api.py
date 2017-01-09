from django.db import models
# import requests

api_key = '24f4931aaa798b5bb5ea5e03bca530c0'

class Weather():
   def DisplayCurrent(city):
       weather = requests.post('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,api_key), json={"key": "value"})
       return weather.json

## depending on the information we can retrieve from the google api we can change the 'city' to the actual address/zip information
