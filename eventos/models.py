#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from galeria.models import Album

class CategoriaEvento(models.Model):
    nome = models.CharField(verbose_name=u'Nome',max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Categoria Evento'
        verbose_name_plural = u'Categoria Evento'
        ordering = ['nome']
        db_table = u'CategoriaEvento'

class Evento(models.Model):
    nome = models.CharField(verbose_name=u'Nome',max_length=100)
    categoria = models.ForeignKey(CategoriaEvento, verbose_name=u'Categoria', related_name='eventos')
    descricao = models.TextField(verbose_name=u'Descrição', blank=True)
    datacadastro = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)
    hora = models.TimeField(verbose_name=u'Horário')
    data = models.DateField(verbose_name=u'Data')
    publico = models.BooleanField(verbose_name='Público?', default=True)
    album = models.ForeignKey(Album, null=True, blank=True, verbose_name=u'Álbum')

    @models.permalink
    def get_absolute_url(self):
        return ('eventos_detalhes', (), {'pk': self.pk}) 

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'
        ordering = ['nome']
        db_table = u'Eventos'
