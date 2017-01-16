from __future__ import unicode_literals
from ..users.models import User
from ..events.models import Event
from .messages import MessageManager, CommentManager
from django.db import models
import datetime


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
