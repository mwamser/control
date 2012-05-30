from django.db import models

class Client(models.Model):
  name = models.CharField(max_length=50)
  tel = models.IntegerField()
  
  #class Meta:
    ##db_table = 'tb_clients'
