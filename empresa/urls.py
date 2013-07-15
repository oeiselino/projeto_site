#encoding: utf-8

from django.conf.urls import patterns, include, url
from views import EmpresaListView

urlpatterns = patterns('empresa.views',
    url(r'^$', EmpresaListView.as_view(), name='empresa'),
)
