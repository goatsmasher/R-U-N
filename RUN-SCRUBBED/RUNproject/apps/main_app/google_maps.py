from django.db import models

api_key = 'AIzaSyCkJ-JbSNOAh_LHivQLHlkLNNFjPqzE1Ig'

class geocode():
    def geo(address):
        geo = requests.post('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,api_key), json={"key": "value"})
        return geo.json

    def place(search):
        geo = requests.post('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(search,api_key), json={"key": "value"})
        return geo.json