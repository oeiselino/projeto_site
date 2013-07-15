#encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.views.generic import ListView, DetailView
from models import Evento

class EventoListaView(ListView):

    template_name = 'eventos/index.html'
    paginate_by = 10
    
    def get_queryset(self):
        events = Evento.objects.filter(publico=True)
        searchano = self.request.GET.get('searchano')
        searchmes = self.request.GET.get('searchmes')          
      
        if searchano and searchmes:
            events = Evento.objects.filter(data__year=searchano, data__month=searchmes) 
            return events
        else:
            if not searchano and not searchmes:
                events = Evento.objects.filter(publico=True) 
                return events
            else:
                if not searchano:
                    events = Evento.objects.filter(data__month=searchmes) 
                    return events
                else:
                    if not searchmes:
                        events = Evento.objects.filter(data__year=searchano) 
                        return events

    def get_context_data(self, **kwargs):
        context = super(EventoListaView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class EventoDetalheView(DetailView):
        
    template_name = 'eventos/detalhes.html'
    context_object_name = 'evento'
        
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Evento.objects.filter(publico=True)
        return Evento.objects.all()
