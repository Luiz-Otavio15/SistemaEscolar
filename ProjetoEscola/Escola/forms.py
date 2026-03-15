from django import forms
from .models import TarefaModel


class AdicionarTarefaForm(forms.ModelForm):
    class Meta: 
        model = TarefaModel
        fields = ['nome', 'descricao', 'situacao']