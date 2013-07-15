#encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from models import Produto, CategoriaProduto

class ProdutoListView(ListView):

    template_name = 'produtos/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProdutoListView, self). get_context_data(**kwargs)
        context['categoria'] = CategoriaProduto.objects.all()
        context['album'] = Produto.objects.all()
        return context

    def get_queryset(self):
        produto = Produto.objects.filter(publico=True)
        searchproduto = self.request.GET.get('searchproduto')
        searchcategoria = self.request.GET.get('searchcategoria')          
      
        if searchproduto and searchcategoria:
            produto = Produto.objects.filter(nome__icontains=searchproduto, categoria__nome__icontains=searchcategoria) 
            return produto
        else:
            if not searchproduto and not searchcategoria:
                produto = Produto.objects.filter(publico=True) 
                return produto
            else:
                if not searchproduto and searchcategoria:
                    produto = Produto.objects.filter(categoria__nome__icontains=searchcategoria) 
                    return produto
                else:
                    if not searchproduto:
                        produto = Produto.objects.filter(categoria__icontains=searchcategoria) 
                        return produto
                    else:
                        if not searchcategoria:
                            produto = Produto.objects.filter(nome__icontains=searchproduto) 
                            return produto

class ProdutoDetailView(DetailView):
        
    template_name = 'produtos/detalhes.html'
    context_object_name = 'produto'
     
    def get_queryset(self):       
        if not self.request.user.is_authenticated():
            return Produto.objects.filter(publico=True)
        return Produto.objects.all()
