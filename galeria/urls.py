#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('galeria.views',
    url(r'^(?P<pk>\d+)/$', 'album', name='galeria_album'),
)
