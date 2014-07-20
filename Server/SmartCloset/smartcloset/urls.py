from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^type/(\d+)/$', 'wear.views.type', name='type'),
    # url(r'^place/(\d+)/$', 'wear.views.place', name='place'),
    url(r'^$', 'wear.views.home', name='home'),
    url(r'^ropero-admin/$', 'wear.views.roperoAdmin', name='ropero-admin'),
    url(r'^ropero-admin/registrar-tipo-ropa/$', 'wear.views.registrarTipoRopa'),
    url(r'^ropero-admin/registrar-tipo-ropa/post/$', 'wear.views.registrarTipoRopaPost'),
    url(r'^ropero-admin/registrar-tipo-material/$', 'wear.views.registrarTipoMaterial'),
    url(r'^ropero-admin/registrar-tipo-material/post/$', 'wear.views.registrarTipoMaterialPost'),
    url(r'^ropero-admin/registrar-tipo-lugar/$', 'wear.views.registrarTipoLugar'),
    url(r'^ropero-admin/registrar-tipo-lugar/post/$', 'wear.views.registrarTipoLugarPost'),
    url(r'^ropero-admin/registrar-ropa/$', 'wear.views.registrarRopa'),
    url(r'^ropero-admin/registrar-ropa/post/$', 'wear.views.registrarRopaPost'),
    url(r'^json-ropa/', 'wear.views.jsonRopa'),
    url(r'^admin/', include(admin.site.urls)),
)