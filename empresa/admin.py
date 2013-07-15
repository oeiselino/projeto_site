#encoding: utf-8

from django.contrib import admin
from models import Empresa

def mark_private(modeladmin, request, queryset):
    queryset.update(publico=False)
    modeladmin.message_user(request, u'Empresa atualidas com sucesso')
mark_private.short_description = u'Marcar como Empresa privada'


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'publico']
    search_fields = ['nome']
    actions = [mark_private]

admin.site.register(Empresa, EmpresaAdmin)
