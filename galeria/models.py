#encoding: utf-8

from django.db import models

class Album(models.Model):
    nome = models.CharField(max_length=100, verbose_name=u'Nome')
    datacadastro = models.DateTimeField(auto_now_add=True, verbose_name=u'Criado em')

    @models.permalink    
    def get_absolute_url(self):
        return ('galeria_album', (), {'pk': self.pk})

    def principal_foto(self):
        fotos = self.fotos.all()
        fotos_p = fotos.filter(principal=True)
        if fotos_p.exists():
            return fotos_p[0]
        elif fotos.exists():
            return fotos[0]
    
    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Album'
        verbose_name_plural = u'Albuns'
        

class Foto(models.Model):
    album = models.ForeignKey(Album, verbose_name=u'Album', related_name='fotos')
    nome = models.CharField(max_length=255, verbose_name=u'Nome', blank=True)
    imagem = models.ImageField(upload_to='fotos', verbose_name=u'Imagem')
    principal = models.BooleanField(default=False, verbose_name=u'Principal?')
    datacadastro = models.DateTimeField(auto_now_add=True, verbose_name=u'Criado em')
    dataatualizado = models.DateTimeField(auto_now_add=True, verbose_name=u'Atualizada em')

    def __unicode__(self):
        if self.nome:
            return self.nome
        return self.imagem.name.split('/')[-1]

    class Meta:
        verbose_name = u'Foto'
        verbose_name_plural = u'Fotos'

