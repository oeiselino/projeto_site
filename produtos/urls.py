#encoding: utf-8

from django.conf.urls import patterns, include, url
from views import ProdutoListView, ProdutoDetailView

urlpatterns = patterns('produtos.views',
    url(r'^$', ProdutoListView.as_view(), name='produtos'),
    url(r'^(?P<pk>\d+)/$', ProdutoDetailView.as_view(), name='produto_detalhes'),
)
