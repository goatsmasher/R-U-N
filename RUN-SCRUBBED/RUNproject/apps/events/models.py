from __future__ import unicode_literals
from ..users.models import User
from django.db import models
import re, datetime, bcrypt
from ..main_app.messages import MessageManager, CommentManager
from ..main_app.google_maps import geocode
from ..main_app.weather_api import Weather

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SPACE_REGEX = re.compile(r'\S+')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.+=_-]+$')
UPPER_CASE_REGEX = re.compile(r'[A-Z]')
NUMBER_REGEX = re.compile(r'[0-9]+')
ILLEGAL_REGEX = re.compile(r'[~`()+={}|\\:;\'\"<>,.?/]')

def validateLengthX(value):
    if len(value) < 4:
        raise ValidationError('{} must be longer than 3 characters'.format(value))

def validateLength(postData):
    valid = True
    errors = []
    if len(postData['content'] < 1):
        errors.append('You didn\'t type anything!')
        valid = False
    response = {
        'errors': errors,
        'status': valid
        }
    return response

def convertDate(value):
    return datetime.datetime.strptime(value, '%m/%d/%Y')

def validateSignup(data):
    valid = True
    errors = []
    if len(data['first_name']) < 1:
        errors.append("First name must not be empty!")
        valid = False
    elif not NAME_REGEX.match(data['first_name']):
        errors.append("First name must contain letters only!")
        valid = False
    if len(data['last_name']) < 1:
        errors.append("Last name must not be empty")
        valid = False
    elif not NAME_REGEX.match(data['last_name']):
        errors.append("Last name must contain letters only!")
        valid = False
    if len(data['email']) < 1:
        errors.append("Email must not be empty!")
        valid = False
    elif not EMAIL_REGEX.match(data['email']):
        errors.append("Email must be valid")
        valid = False
    if len(data['password']) < 8:
        errors.append("Password must be more than 8 characters!")
        valid = False
    elif not UPPER_CASE_REGEX.search(data['password']):
        errors.append("Must contain at least 1 uppercase letter.")
        valid = False
    elif not NUMBER_REGEX.search(data['password']):
        errors.append("Must contain at least 1 number.")
        valid = False
    elif ILLEGAL_REGEX.search(data['password']):
        errors.append("Password must not contain illegal characters (~`()+={}|\\:;\'\"<>,.?/)") #~`()+={}|\\:;\'\"<>,.?/
        valid = False
    if data['confirm_password'] != data['password']:
        errors.append("Password not confirmed.")
        valid = False
    # if convertDate(data['dob']) > datetime.datetime.today():
    #     errors.append("Date invalid. Check format and ensure it's in the past.")
    #     valid = False

    response = {
        'errors': errors,
        'status': valid,
    }
    return response


class EventManager(models.Manager):
    def new_event(self, postData, user_id):
        location = Address.objects.addAddress(postData)
        response = {}
        # validateResponse = validateLength(postData)
        validateResponse = {'status':True}
        if validateResponse['status']:
            location=Address.objects.addAddress(postData)
            response['event'] = self.create(
                name=postData['event_name'],
                description=postData['event_description'],
                created_by=User.objects.get(id=user_id),
                datetime_start=postData['date_from'],
                datetime_end=postData['date_to'],
                # allow_others=postData['allow_others'],
                # creater_approve_other_invites=postData['creater_approve_other_invites'],
                address=location['address']
                )
            response['status'] = validateResponse['status']
        else:
            response['errors']=validateResponse['errors']
            response['status'] = validateResponse['status']
        return response

        #
        # self.create(
        #     name = postData['event_name'],
        #     description = postData['event_description'],
        #     datetime_start = postData['date_from'],
        #     datetime_end = postData['date_to'],
        #     # time_start = postData['hour'] +":" + postData['minutes'],
        #     created_by = User.objects.get(id=user_id),
        # )

class AddressManager(models.Manager):
    def addAddress(self, postData):
        response = {}
        validateResponse = {'status':True}
        if validateResponse['status']:
            # print(postData['event_place'])
            geo_place = geocode.place(postData['event_place'])
            # geo_place = geo_place.json()
            # print(geo_place)
            place_address = geo_place['result']['address_components']
            # geonames = filter(lambda x: len(set(x['types']).intersection(types)), place_address)
            # print(geonames)

            # Parse Google's address components into diction with types as keys
            parsed_address = {}
            for key in place_address:
                parsed_address[key['types'][0]] = key['short_name']
            print(parsed_address)
            response['address'] = self.create(
                google_id=geo_place['result']['place_id'],
                location_name=geo_place['result']['name'],
                address_primary=parsed_address['street_number'],
                address_street=parsed_address['route'],
                address_city=parsed_address['locality'],
                address_state=parsed_address['administrative_area_level_1'],
                address_neighborhood=parsed_address['neighborhood'],
                lng=geo_place['result']['geometry']['location']['lng'],
                lat=geo_place['result']['geometry']['location']['lat'],
                postal_code=parsed_address['postal_code']
                )
        else:
            response['errors']=validateResponse['errors']
            response['status']=validateResponse['status']
        return response

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_by = models.ForeignKey(User)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateField()
    # time_start = models.TimeField()
    # invited_users = ManyToManyField()
    # allow_others = models.BooleanField(deafult=False)
    # creater_approve_other_invites = models.BooleanField(deafult=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey('Address')
    objects = EventManager()

class Address(models.Model):
    location_name = models.CharField(max_length=50)
    address_primary = models.CharField(max_length=50) #read it is better to save these fields as text because what if address has a 1/2 or 123'B' Street Ave
    address_street = models.CharField(max_length=50)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15)
    address_neighborhood = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    google_id = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    objects = AddressManager()

class Message(models.Model):
    message = models.CharField(max_length=1000)
    created_by = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    related_message = models.ForeignKey(Message)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

# class Poll(models.Model):
