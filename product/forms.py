# -*- coding: utf-8 -*-

from django import forms

class FormProducts(forms.Form):
  name = forms.CharField(max_length=50)
  note = forms.CharField(max_length=200)