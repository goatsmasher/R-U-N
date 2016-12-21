from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import re, bcrypt, datetime
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db.models import Count
from .forms import AddForm, EditForm
from .models import Appointments
from ..user.models import User


def index(request):
    if 'user_id' not in request.session:
        return redirect('user:index')
    today = datetime.datetime.today()
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'thisday': datetime.datetime.today(),
        'addForm': AddForm(),
        'today': Appointments.objects.filter(user=request.session['user_id']).filter(date__day=today.day).filter(date__month=today.month).order_by('time'),
        'future': Appointments.objects.filter(user=request.session['user_id']).exclude(date__day=today.day).exclude(date__month=today.month).order_by('date','time'),
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

def add(request):
    viewsReponse = Appointments.objects.add(request.POST)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')

def update(request, apt_id):
    viewsReponse = Appointments.objects.update(request.POST, apt_id)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'task': Appointments.objects.get(id=apt_id),
            }
    return render(request, 'appointments/edit.html', context)

def delete(request, apt_id):
    viewsReponse = Appointments.objects.delete(apt_id)
    if viewsReponse['status']:
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('apt:index')
