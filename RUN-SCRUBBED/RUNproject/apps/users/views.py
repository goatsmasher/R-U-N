from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import re, bcrypt
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db.models import Count
from .forms import SignupForm, SigninForm
from .models import User
from ..events.models import Event

MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}

def index(request):
    signupForm = SignupForm()
    signinForm = SigninForm()
    context = {
        'signupForm': signupForm,
        'signinForm': signinForm
        }
    return render(request, 'user/index.html', context)

def signup(request):
    if request.method == "POST":
        print(request.POST)
        viewsReponse = User.objects.signup(request.POST)
        if viewsReponse['status']:
            request.session['user_id'] = viewsReponse['user'].id
            request.session['first_name'] = viewsReponse['user'].first_name
            request.session['logged_in'] = True
            return redirect ('main:index')
        else:
            for error in viewsReponse['errors']:
                messages.error(request, error)
            return redirect('user:signup')
    return render(request, 'user/signup.html')

def signin(request):
    viewsReponse = User.objects.signin(request.POST)
    if viewsReponse['status']:
        request.session['user_id'] = viewsReponse['user_id']
        request.session['first_name'] = User.objects.get(id=request.session['user_id']).first_name
        return redirect('main:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('user:index')

def signout(request):
    request.session.clear()
    return redirect('user:index')

def profile(request):
    user = User.objects.get(id=request.session['user_id'])
    events = Event.objects.all().filter(created_by_id=user.id)
    count = Event.objects.all().filter(created_by_id=user.id).count()
    context = {
        "first_name" : user.first_name,
        "last_name" : user.last_name,
        "email" : user.email,
        "password" : "*********",
        "user_created" : events,
        "count" : count,
    }
    return render(request, 'user/profile.html', context)
