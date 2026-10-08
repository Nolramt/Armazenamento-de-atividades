from django import forms
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho

class ArquivoAtividadeForm(forms.ModelForm):
    class Meta:
        model = Arquivo_atividade
        fields = ["nome", "arquivo"]

class ArquivoTrabalhoForm(forms.ModelForm):
    class Meta:
        model = Arquivo_trabalho
        fields = ["nome", "arquivo"]

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nome"]

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ["nome", "tipo"]

class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalho
        fields = ["nome", "tipo"]

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ["nome", "ano"]