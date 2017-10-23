from django.db import models

from accounts.models import ServiceProvider, CustomUser
from django.contrib.auth.models import User

class Job(models.Model):
    job_type = models.CharField(max_length=150)
    provider = models.ForeignKey(CustomUser, related_name="service_provider")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.IntegerField(default=0)

    def __str__(self):
        return self.job_type


class Booking(models.Model):
    client = models.ForeignKey(CustomUser, related_name="client")
    booked_job = models.ForeignKey(Job, related_name="booked_job", blank=True, null=True)
    date = models.DateField()


# Create your models here.
