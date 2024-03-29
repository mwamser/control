from models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['quantity']}), 
    (None, {'fields': ['arrival_estimate']}), 
    #('Seller information', {'fields': ['name']}),
    #('Seller information', {'fields': ['email']}),
  ]

admin.site.register(Order, OrderAdmin)