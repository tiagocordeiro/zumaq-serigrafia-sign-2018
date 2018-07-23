from django.contrib import admin
from .models import Visitante


class VisitanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'celular',)


admin.site.register(Visitante, VisitanteAdmin, )
