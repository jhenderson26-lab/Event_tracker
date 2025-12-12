from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
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
        

