# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from product.models import Product
from forms import FormProducts

def products_list(request):
  list_itens = Product.objects.all()
  return render_to_response("products_list.html", 
     {'list_itens': list_itens})
      
def add_products(request):
  if request.method == 'POST':
    form = ProductsForm(request.POST, request.FILES)
    
    if form.is_valid():
      values = form.cleaned_data
      item = Product(name=values['name'], note=values['note'])
      item.save()
      
      return render_to_response("save.html", {})
      
    else:
      form = ProductsForm()
      
  return render_to_response("add_product.html", {'form':form}, context_instance=RequestContext(request))
