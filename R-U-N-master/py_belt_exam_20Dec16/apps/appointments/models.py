from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
import re, datetime, bcrypt
from ..user.models import User


def convertDateTime(date, time):
    return datetime.datetime.strptime(date + '-' + time, '%m/%d/%Y-%H:%M')

def convertDate(date):
    return datetime.datetime.strptime(date, '%m/%d/%Y')

def convertTime(time):
    return datetime.datetime.strptime(time, '%H:%M')

class AppointmentManager(models.Manager):
    def add(self, postData):
        errors = []
        response = {}

        if convertDateTime(postData['date'], postData['time']) < datetime.datetime.now():
            errors.append('Date/Time invalid. Check your formatting and ensure it\'s in the future!')
        if not len(postData['task']):
            errors.append('Task must have a description!')

        if Appointments.objects.filter(date=convertDate(postData['date']),time=convertTime(postData['time'])):
            errors.append('You already have a task at that time!')

        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            Appointments.objects.create(
                date=convertDate(postData['date']),
                time=convertTime(postData['time']),
                task=postData['task'],
                status='Pending',
                user=User.objects.get(id=postData['user_id']))
        return response

    def update(self,postData, apt_id):
        errors = []
        response = {}

        if convertDateTime(postData['date'], postData['time']) < datetime.datetime.now():
            errors.append('Date/Time invalid. Check your formatting and ensure it\'s in the future!')
        if not len(postData['task']):
            errors.append('Task must have a description!')

        if Appointments.objects.exclude(id=apt_id).filter(date=convertDate(postData['date']),time=convertTime(postData['time'])):
            errors.append('You already have a task at that time!')

        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            Appointments.objects.filter(id=apt_id).update(
                date=convertDate(postData['date']),
                time=convertTime(postData['time']),
                task=postData['task'],
                status=postData['status']
                )
        return response

    def delete(self, postData):
        errors = []
        response = {}
        response['status'] = True
        response['view'] = self.filter(id=postData).delete()
        return response

class Appointments(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField(default='11/07/2017')
    time = models.TimeField(default='18:57')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user.User')

    objects = AppointmentManager()
