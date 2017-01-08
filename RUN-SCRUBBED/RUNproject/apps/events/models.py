from __future__ import unicode_literals
from ..users.models import User
from django.db import models

# Create your models here.
class EventManager(models.Manager):
    def new_event(self, postData, user_id):
        self.create(
            name = postData['event_name'],
            description = postData['event_description'],
            datetime_start = postData['date_from'],
            datetime_end = postData['date_to'],
            # time_start = postData['hour'] +":" + postData['minutes'],
            created_by = User.objects.get(id=user_id),
        )


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
    # address = models.ForeignKey(Address)
    objects = EventManager()