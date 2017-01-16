from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
import re, datetime, bcrypt

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

class MessageManager(models.Manager):
    def addPost(postData, user_id):
        response = {}
        validateResponse = validateLength(postData)
        if validateResponse['status']:
            self.create(
                message=postData['content'],
                created_by=User.objects.get(id=user_id),
                event=Event.objects.get(id=postData['event_id'])
                )
        else:
            response['errors']=validateResponse['errors']
            response['status']=validateResponse['status']
        return response

    def deletePost(postData, message_id):
        response = {}
        response['status'] = False
        print ('Need to code delete block')
        return response
        
class CommentManager(models.Manager):
    def addComment(postData, user_id):
        validateResponse = validateLength(postData)
        if validateResponse['status']:
            self.create(
                comment=postData['content'],
                created_by=User.objects.get(id=user_id,),
                related_message=Message.objects.get(id=postData['message_id'])
                )
        else:
            response['errors']=validateResponse['errors']
            response['status']=validateResponse['status']
        return response


    def deleteComment(postData, comment_id):
        response = {}
        response['status'] = False
        print ('Need to code delete block')
        return response
