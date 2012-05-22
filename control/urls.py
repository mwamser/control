from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control.views.home', name='home'),
    # url(r'^control/', include('control.foo.urls')),
    #(r'^$', 'product.views.index'),
    (r'^$', 'product.views.products_list'),
    (r'^add_products/$', 'product.views.add_products'),

    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)