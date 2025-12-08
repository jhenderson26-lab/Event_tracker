from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('Login&Signup/signup', register_view, name='signup'),
    path('Login&Signup/login', login_view, name='login'),
    path('events/', event_view, name='events'),
    path('create_event/', create_view, name='create_event'),
    path('delete_event/<event_id>', delete_event, name="delete"),
    path('logout/', logout_view, name='logout'),]