#encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from models import Empresa

class EmpresaListView(ListView):

    template_name = 'empresa/index.html'

    def get_queryset(self):
        empresa = Empresa.objects.filter(publico=True)
        return empresa
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self). get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter(publico=True)[:4]
        return context
