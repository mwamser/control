# -*- coding: utf-8 -*-

from django import forms

class FormOrder(forms.Form):
  quantity = forms.IntegerField()
  