from django.contrib import admin
from .models import ServiceProvider, Client, CustomUser

admin.site.register(ServiceProvider)
admin.site.register(Client)
admin.site.register(CustomUser)
# Register your models here.
