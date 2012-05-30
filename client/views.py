from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from forms import FormClient
from client.models import Client

def list_client(request):
  list_itens = Client.objects.all()
  return render_to_response("client_list.html", 
     {'list_itens': list_itens})
  
def add_client(request):
  
  form = FormClient(request.POST, request.FILES)
  
  if form.is_valid():
    values = form.cleaned_data
    item = Client(name=values['name'], tel=values['tel'])
    item.save()
      
    return render_to_response("save.html", {})
  
  else:
    form = FormClient()
    return render_to_response("add_client.html", {'form' : form}, context_instance=RequestContext(request))
