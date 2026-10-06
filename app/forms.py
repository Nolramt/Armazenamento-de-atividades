from django import forms
from .models import Arquivo_atividade, Arquivo_trabalho

class ArquivoAtividadeForm(forms.ModelForm):
    class Meta:
        model = Arquivo_atividade
        fields = {"nome", "arquivo"}
class ArquivoTrabalhoForm(forms.ModelForm):
    class Meta:
        model = Arquivo_trabalho
        fields = {"nome", "arquivo"}