from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceProvider(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.CharField(max_length=1000)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    city = models.CharField(max_length=30, blank=True, null=True)

class Client(models.Model):
    previous_buys = models.IntegerField(blank=True, null=True, default=0)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12, blank=True, null=True)
    bank_account = models.CharField(max_length=16, blank=True, null=True)
    customer = models.OneToOneField(Client, blank=True, null=True)
    provider = models.OneToOneField(ServiceProvider, blank=True, null=True)

    def __str__(self):
        try:
            return "Username: {0}, city: {1}".format(self.username, self.provider.city)
        except:
            return self.username
# Create your models here.
