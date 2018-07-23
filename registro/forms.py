from django.forms import ModelForm, TextInput, EmailField
from .models import Visitante


class VisitanteForm(ModelForm):
    class Meta:
        model = Visitante
        fields = ('nome', 'email', 'telefone', 'celular', 'observacoes',)

        widgets = {
            'nome': TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'telefone': TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg phone',
                'type': 'text', }),
            'celular': TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg phone',
                'type': 'text', }),
            'observacoes': TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
        }
