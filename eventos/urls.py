#encoding: utf-8

from django.conf.urls import patterns, include, url
from views import EventoListaView, EventoDetalheView

urlpatterns = patterns('eventos.views',
    url(r'^$', EventoListaView.as_view(), name='eventos'),
    url(r'^(?P<pk>\d+)/$', EventoDetalheView.as_view(), name='eventos_detalhes'),
)
