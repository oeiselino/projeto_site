#encoding: utf-8

from django.contrib import admin
from models import Foto, Album

class FotoInline(admin.TabularInline):
    model = Foto

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['nome', 'datacadastro']
    inlines = [FotoInline]

admin.site.register (Album, AlbumAdmin)
