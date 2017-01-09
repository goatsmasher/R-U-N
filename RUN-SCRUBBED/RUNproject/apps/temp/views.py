from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import re, bcrypt, datetime
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db.models import Count
from .forms import AddEventForm
from .models import Event, Invited, Address, Message, Comment
from ..user.models import User
from .google_apis import geocode, Weather

def details(request, event_id):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'messages': Message.objects.filter(event=Event.objects.filter(id=event_id)),
        'comments': Comment.objects.filter(related_message__event=Event.objects.filter(id=event_id)),
    }
    return render(request, 'appointments/details.html', context)

def addEventForm(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'addEventForm': AddEventForm(),

    }
    return render(request, 'appointments/add_event.html', context)

def addEvent(request):
    viewsReponse = Event.objects.addEvent(request.POST)
    g_place = geocode.place(request.POST['place'])
    if viewsReponse['status']:
        context = {
            'place': g_place,
            # 'place2': (g_place['results'][0]['formatted_address'])
        }
        return render(request, 'appointments/add_event.html', context)
        # return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')

def index(request):
    if 'user_id' not in request.session:
        return redirect('user:index')
    # today = datetime.datetime.today()
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        # 'thisday': datetime.datetime.today(),
        # 'addForm': AddForm(),
        # 'today': Appointments.objects.filter(user=request.session['user_id']).filter(date__day=today.day).filter(date__month=today.month).order_by('time'),
        # 'future': Appointments.objects.filter(user=request.session['user_id']).exclude(date__day=today.day).exclude(date__month=today.month).order_by('date','time'),
        # 'geocode': geocode.geo('Mad Pizza, Madison Street, Seattle, WA, United States'),
        'place': geocode.place('pizza in Seattle'),
        'weather': Weather.DisplayCurrent('Seattle'),
        # 'posts': 'Hi!'
        }

    return render(request, 'appointments/index.html', context)

def edit(request, apt_id):
    if 'user_id' not in request.session:
        return redirect('user:index')
    today = datetime.datetime.today()
    todayF = datetime.datetime.strftime(today,'%Y-%m-%d')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'task': Appointments.objects.get(id=apt_id),
        }

    return render(request, 'appointments/edit.html', context)

def addMessage(request):
    viewsReponse = Message.objects.addMessage(request.POST)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')

def deleteMessage(request, message_id):
    viewsReponse = Message.objects.deleteMessage(message_id)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')

def addComment(request):
    viewsReponse = Comment.objects.addComment(request.POST)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')

def deleteComment(request, comment_id):
    viewsReponse = Comment.objects.deleteComment(comment_id)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')
