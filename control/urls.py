from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control.views.home', name='home'),
    # url(r'^control/', include('control.foo.urls')),
    (r'^$', 'views.index'),
    
    (r'^product/$', 'product.views.products_list'),
    (r'^product/add_product/$', 'product.views.add_product'),
        
    (r'^client/$', 'client.views.list_client'),
    (r'^client/add_client/$', 'client.views.add_client'),
    
    (r'^order/$' , 'order.views.add_order'),
    #(r'^order/add_order/$' , 'order.views.add_order'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
