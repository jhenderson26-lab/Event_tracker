from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Log_In(models.Model):
    username = models.TextField(max_length=30)
    password = models.TextField(max_length=20)
    email = models.TextField(max_length=50)

class User(models.Model):
    user= models.ForeignKey(Log_In, on_delete=models.CASCADE)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    set_date = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(null=True, blank=True)

    @property
    def until_event(self):
        today = date.today()
        if self.event_date != None:
            until = self.event_date - today
            until_stripped = str(until).split("day", 1)[0]
            num_until = until_stripped.strip()
            return num_until