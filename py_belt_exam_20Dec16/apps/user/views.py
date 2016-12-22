from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import re, bcrypt
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db.models import Count
from .forms import SignupForm, SigninForm
from .models import User






# from ..wish_list.models import Item, List


MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('apt:index')

    signupForm = SignupForm()
    signinForm = SigninForm()
    context = {
        'signupForm': signupForm,
        'signinForm': signinForm
        }

    return render(request, 'user/index.html', context)

def signup(request):
    # if
    if request.method == "POST":
        print(request.POST)
        viewsReponse = User.objects.signup(request.POST)
        
        if viewsReponse['status']:
            request.session['user_id'] = viewsReponse['user'].id
            return redirect ('apt:index')
        else:
            for error in viewsReponse['errors']:
                messages.error(request, error)
            return redirect('user:signup')
    # return redirect('user:signup')
    return render(request, 'user/signup.html')

    # print(request.POST)
    # viewsReponse = User.objects.signup(request.POST)
    # if viewsReponse['status']:
    #     request.session['user_id'] = viewsReponse['user'].id
    #     return redirect ('user:index')
    # else:
    #     for error in viewsReponse['errors']:
    #         messages.error(request, error)
    #     return redirect('user:index')
    # return redirect('apt:index')

def signin(request):
    viewsReponse = User.objects.signin(request.POST)
    if viewsReponse['status']:
        request.session['user_id'] = viewsReponse['user_id']
        return redirect('apt:index')
    else:
        for error in viewsReponse['errors']:
            messages.error(request, error)
    return redirect('user:index')

def signout(request):
    request.session.clear()
    return redirect('user:index')
