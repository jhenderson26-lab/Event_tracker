from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
from datetime import date
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from app.forms import *

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def getting_user(request):
    user_id = request.user.id
    owner = models.User.objects.get(id=user_id)
    return owner

def home(request):
    if request.user.is_authenticated:
        owner = getting_user(request)
        context = {'owner': owner}
    else:
        context = None
    return render(request, 'base.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    context = { 'form': form }
    return render(request, 'Login&Signup/signup.html', context) 

def check_event(day):
    int_date = int((f'{day.event_date.year}' + f'{day.event_date.month}' + f'{day.event_date.day}'))
    tday = date.today()
    int_today = int((f'{tday.year}' + f'{tday.month}' + f'{tday.day}'))
    if int_date > int_today:
        day.save()
    else:
        day.delete()

@login_required(login_url='home')
def event_view(request):
    if request.user.is_authenticated:
        event = forms.EventForm()
        ower = getting_user(request)
        event_list = models.Event.objects.filter(user=ower)
        list_order = models.Event.objects.filter(user=ower).order_by("event_date")
        for events in event_list:
            if events.until_event == None:
                events.delete()
            check_event(events)
        context = {'event': event, 'text': list_order}
    else:
        context = {'text': 'Sorry, you need to login in.'}
    return render(request, 'events.html', context)


@login_required
def create_view(request):
    if request.method == 'POST':
        ower = getting_user(request)
        form = forms.EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = ower
            event.save()
            for day in models.Event.objects.filter(user=ower):
                day.event_date = day.created_at.date() + timedelta(days=day.set_date)
                day.save()
                check_event(day)

    return redirect('events')
    

def delete_event(request, event_id):
    event = models.Event.objects.get(id=event_id)
    event.delete()
    return redirect('events')

def logout_view(request):
    logout(request)
    return redirect('home')
    

# add confetti