#encoding: utf-8

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class ContatoForm(forms.Form):
    nome = forms.CharField(label=u'Nome')
    email = forms.EmailField(label=u'E-mail')
    mensagem = forms.CharField(label=u'Mensagem', widget=forms.Textarea)

    def send_mail(self):
        subject = u'E-mail de Contato de %s' % self.cleaned_data['nome']
        context = {
            'nome': self.cleaned_data["nome"],
            'email': self.cleaned_data["email"],
            'mensagem': self.cleaned_data["mensagem"],
        }
        mensagem = render_to_string("contato_mail.txt", context)
        mensagem_html = render_to_string("contato_mail.html", context)
        msg = EmailMultiAlternatives(subject, mensagem, 'lino@umuarama.pr.gov.br',['lino@umuarama.pr.gov.br'])
        msg.attach_alternative(mensagem_html, "text/html")
        msg.send()
