from django import forms

class FormClient(forms.Form):
  Nome = forms.CharField(max_length=50)
  Telefone = forms.IntegerField()