from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'set_date']
        labels = {
            'title': 'Event Name',
            'set_date': 'Set Date',
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Your Email Address")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Choose a Username"
        self.fields['password2'].label = "Confirm Password"
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
        self.fields['username'].help_text = ""

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email