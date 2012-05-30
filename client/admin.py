from django.contrib import admin

from models import Client

#class OrderClient(admin.OrderAdmin):
  
admin.site.register(Client)