from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'base.html')

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home') 
    else:
        form = AuthenticationForm()
    context = { 'form': form }
    return render(request, 'Login&Signup/login.html', context)

@login_required
def event_view(request):
    return render(request, 'ceate.html')

