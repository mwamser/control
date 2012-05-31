# -*- coding: utf-8 -*-

from django import forms

from client.models import Client

class FormProducts(forms.Form):
  name = forms.CharField(max_length=50)
  note = forms.CharField(max_length=200)
  client = forms.ModelChoiceField(queryset=Client.objects.all())
  #client = forms.ManyToManyField(Client)