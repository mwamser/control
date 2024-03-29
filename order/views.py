from django.core.urlresolvers import reverse
#from django.http import HttpReponse, HttpReponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Order
from order.forms import FormOrder

def add_order(request):
  form = FormOrder(request.POST, request.FILES)
  
  if form.is_valid():
    values = form.cleaned_data
    item = Order(quantity=values['quantity'])
    item.save()
    return render_to_response("save.html", {})
    
  else:
    form = FormOrder()
    return render_to_response("add_order.html", {'form' : form}, context_instance=RequestContext(request))
