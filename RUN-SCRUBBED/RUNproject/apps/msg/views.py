from django.shortcuts import render, redirect
from ..users.models import User
from ..events.models import Event
from ..msg.models import Message, Comment


def add_message(request):
    message = Message.objects.addPost(request.POST, request.session['user_id'])
    return redirect('event:detail')
    
def delete_message(request, message_id):
    response = {}
    response['message'] = Message.objects.deletePost(request.POST, message_id)
    return redirect('event:detail')

def add_comment(request):
    comment = Comment.objects.deletePost(request.POST, request.session['user_id'])
    return redirect('event:detail')

def delete_comment(request, comment_id):
    response = {}
    response['comment'] = Comment.objects.deletePost(request.POST, comment_id)
    return redirect('event:detail')
