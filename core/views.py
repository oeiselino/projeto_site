#encoding: utf-8

from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from forms import ContatoForm
from eventos.models import Evento

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self). get_context_data(**kwargs)
        context['evento'] = Evento.objects.filter(publico=True)[:4]
        return context

class ContatoView(FormView):
    
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = '/contato/enviado/'

    def form_valid(self, form):
        form.send_mail()
        return super(ContatoView, self).form_valid(form)

class ContatoEnviado(TemplateView):

    template_name = 'contatoenviado.html'

    def get_context_data(self, **kwargs):
        context = super(ContatoEnviado, self). get_context_data(**kwargs)
        return context

