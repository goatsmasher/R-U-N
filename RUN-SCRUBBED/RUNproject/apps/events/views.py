from django.shortcuts import render, redirect
from ..users.models import User
from .models import Event

# Create your views here.
def create(request):
    context = {
        "range" : range(1,12),
        "minutes" : ('00', 15, 30,45)
    }
    return render(request, 'main_app/event_page.html', context)

def invite(request):
    return render(request, 'main_app/invite_friends.html')

def create_new(request):
    new_event = Event.objects.new_event(request.POST, request.session['user_id'])
    return redirect('main:index')
    