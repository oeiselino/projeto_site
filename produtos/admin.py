#encoding: utf-8

from django.contrib import admin
from models import Produto, CategoriaProduto

def mark_private(modeladmin, request, queryset):
    queryset.update(publico=False)
    modeladmin.message_user(request, u'Produtos atualidas com sucesso')
mark_private.short_description = u'Marcar como produtos privado'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'publico', 'categoria']
    search_fields = ['nome']
    actions = [mark_private]

class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(CategoriaProduto, CategoriaProdutoAdmin)
