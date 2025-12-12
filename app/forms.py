from django import forms
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'set_date']
        labels = {
            'title': 'Event Name',
            'set_date': 'Set Date',
        }
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')