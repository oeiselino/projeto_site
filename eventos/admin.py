#encoding: utf-8

from django.contrib import admin
from models import Evento, CategoriaEvento

def mark_private(modeladmin, request, queryset):
    queryset.update(publico=False)
    modeladmin.message_user(request, u'Eventos atualidos com sucesso')
mark_private.short_description = u'Marcar como evento privado'


class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'publico']
    search_fields = ['nome']
    actions = [mark_private]

admin.site.register(Evento, EventoAdmin)

class CategoriaEventoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(CategoriaEvento, CategoriaEventoAdmin)
