from django import forms

class FormClient(forms.Form):
  name = forms.CharField(max_length=50)
  tel = forms.IntegerField()