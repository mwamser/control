# -*- coding: utf-8 -*-

from django import forms

from client.models import Client
from product.models import Product

class FormOrder(forms.Form):
  product = forms.ModelChoiceField(queryset=Product.objects.all())
  quantity = forms.IntegerField()
  client = forms.ModelChoiceField(queryset=Client.objects.all())