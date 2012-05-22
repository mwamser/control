from django.db import models
from product import *

IOF = 1.07

class Order(models.Model):
  product = product.Product()
  quantity = models.Integer(max_digits=50)
  sub_total = models.DecimalField(max_digits=10, decimal_places=3)
  order_status = models.CheckField()
  
  arrival_estimate = models.DateField()
  
  seller = models.CharField(max_length=50)
  
  def item_total(sub_total):
    item_total = (sub_total * IOF)
    
    return item_total
    
  def unit_price(item_total, qty):
    unit_price = item_total / qty
    
    return unit_price
