# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=50)
  note = models.CharField(max_length=200)
  
  class Meta:
    db_table = 'tb_products'
  
