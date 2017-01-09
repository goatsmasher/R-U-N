from django.shortcuts import render, redirect
import re, bcrypt, datetime
from ..users.models import User
from ..events.models import Event
from .weather_api import Weather
from .google_maps import geocode


def index(request):
    try:
        request.session['user_id']
    except:
        return redirect('user:index')
    context = {
        "upcoming" : Event.objects.filter(created_by_id=request.session['user_id']),
    }
    return render(request, 'main_app/index.html', context)
