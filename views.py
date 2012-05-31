from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from client.forms import FormClient
#from client.models import Client
from product.models import Product

def index(request):
  return render_to_response("index.html", {})
  