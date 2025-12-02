from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [path('Login&Signup/signup', register_view, name='signup'),
               path('Login&Signup/login', login_view, name='login')]