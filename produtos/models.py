#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from galeria.models import Album

class CategoriaProduto(models.Model):
    nome = models.CharField(verbose_name=u'Nome',max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Categoria Produto'
        verbose_name_plural = u'Categoria Produto'
        ordering = ['nome']
        db_table = u'CategoriaProduto'

class Produto(models.Model):

    nome = models.CharField(u'Nome', max_length=255, unique=True)
    descricao = models.TextField(verbose_name=u'Descrição', blank=True)
    categoria = models.ForeignKey(CategoriaProduto, verbose_name=u'Categoria', related_name='Produto')
    album = models.ForeignKey(Album, null=True, blank=True, verbose_name=u'Álbum')
    datacadastro = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)
    publico = models.BooleanField(verbose_name='Público?', default=True)

    @models.permalink
    def get_absolute_url(self):
        return ('produto_detalhes', (), {'pk': self.pk}) 

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'
        ordering = ['nome']
        db_table = u'Produto'
