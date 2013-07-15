#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from galeria.models import Album

class Empresa(models.Model):
    nome = models.CharField(u'Título',max_length=255,unique=True)
    descricao = models.TextField(verbose_name=u'Descrição', blank=True)
    album = models.ForeignKey(Album, null=True, blank=True, verbose_name=u'Álbum')
    datacadastro = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)
    publico = models.BooleanField(verbose_name='Público?', default=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Empresa'
        verbose_name_plural = u'Empresa'
        ordering = ['nome']
        db_table = u'Empresa'
