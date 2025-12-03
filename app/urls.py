from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('Login&Signup/signup', register_view, name='signup'),
    path('Login&Signup/login', login_view, name='login'),
    path('create/', event_view, name='events'),]