from django.shortcuts import render
import requests
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho
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
    arquivo = Arquivo_atividade.objects.filter(ID_atividade=id)

    return render(request, "arquivo_atividade.html", {"arquivos":arquivo})
def detalhes_trabalho(request, id):
    arquivo = Arquivo_trabalho.objects.filter(ID_trabalho=id)

    return render(request, "arquivo_trabalho.html", {"arquivos":arquivo})