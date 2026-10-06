from django.shortcuts import render, redirect
import requests
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho
from .forms import ArquivoAtividadeForm, ArquivoTrabalhoForm

# Create your views here.

def lista_periodos(request):
    periodos = Periodo.objects.all()

    return render(request, "periodos.html", {"periodos": periodos})
def lista_materias(request, id):
    materias = Materia.objects.filter(ID_periodo=id)

    return render(request, "materias.html", {"materias": materias})
def detalhes_materia(request, id):
    atividades = Atividade.objects.filter(ID_materia=id)
    trabalhos = Trabalho.objects.filter(ID_materia=id)

    return render(request, "atividades_trabalhos.html", {"atividades": atividades, "trabalhos": trabalhos})
def detalhes_atividade(request, id):
    arquivos = Arquivo_atividade.objects.filter(ID_atividade=id)

    if (request.method == "POST"):
        form = ArquivoAtividadeForm(request.POST, request.FILES)

        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.ID_atividade_id = id
            arquivo.save()

            return redirect("detalhes_atividade", id=id)
    else:
        form = ArquivoAtividadeForm()

    return render(request, "arquivo_atividade.html", {"arquivos":arquivos, "form":form})
def detalhes_trabalho(request, id):
    arquivos = Arquivo_trabalho.objects.filter(ID_trabalho=id)

    if (request.method == "POST"):
        form = ArquivoTrabalhoForm(request.POST, request.FILES)

        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.ID_trabalho_id = id
            arquivo.save()

            return redirect("detalhes_trabalho", id=id)
    else:
        form = ArquivoTrabalhoForm()

    return render(request, "arquivo_trabalho.html", {"arquivos":arquivos, "form":form})