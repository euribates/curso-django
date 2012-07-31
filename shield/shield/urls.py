from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shield.views.home', name='home'),
    # url(r'^shield/', include('shield.foo.urls')),
    (r'^/ejemplo/$', 'shield.views.ejemplo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^/?$', 'shield.views.homepage'),
    url(r'^heroes/?$', 'shield.views.heroes'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
