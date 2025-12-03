from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'set_date']
        labels = {
            'title': 'Event Name',
            'set_date': 'Set Date',
        }