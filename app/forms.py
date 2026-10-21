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

    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if not nome.strip():
            raise forms.ValidationError("O nome da atividade não pode ficar vazio.")

        return nome

class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalho
        fields = ["nome", "tipo"]

    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if not nome.strip():
            raise forms.ValidationError("O nome do trabalho não pode ficar vazio.")

        return nome

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ["nome", "ano"]