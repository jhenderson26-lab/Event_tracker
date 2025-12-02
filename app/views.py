from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_view(request):
    form = UserCreationForm()
    context = { 'form': form }
    return render(request, 'Login&SignUp/signup.html', context)

def login_view(requset):
    pass