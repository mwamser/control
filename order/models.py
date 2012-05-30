from django.db import models
#from product import Product

class Order(models.Model):
  #product = models.ForeignKey(Product)
  quantity = models.IntegerField()
  #unity_price = models.DecimalField()
  #sub_total = models.DecimalField()
  #order_status = models.CheckField()
  date = models.DateTimeField()
  paymente_date = models.DateTimeField()
  
  arrival_estimate = models.DateField()
  
  def __unicode__(self):
    return self.quantity

class Seller(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()