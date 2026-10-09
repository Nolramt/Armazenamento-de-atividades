from django.shortcuts import render, redirect
import requests
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho
from .forms import PeriodoForm, MateriaForm, AtividadeForm, TrabalhoForm, ArquivoAtividadeForm, ArquivoTrabalhoForm

# Create your views here.

def lista_periodos(request):
    periodos = Periodo.objects.all()

    if (request.method == "POST"):
        form = PeriodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("lista_periodos")
    else:
        form = PeriodoForm()

    return render(request, "periodos.html", {"periodos": periodos, "form":form})

def lista_materias(request, id):
    materias = Materia.objects.filter(ID_periodo=id)

    if (request.method == "POST"):
        form = MateriaForm(request.POST)

        if form.is_valid():
            materia = form.save(commit=False)
            materia.ID_periodo_id = id
            materia.save()

            return redirect("lista_materias", id=id)
    else:
        form = MateriaForm()

    return render(request, "materias.html", {"materias": materias, "form":form})

def detalhes_materia(request, id):
    atividades = Atividade.objects.filter(ID_materia=id)
    trabalhos = Trabalho.objects.filter(ID_materia=id)

    materia = Materia.objects.get(ID_materia=id)

    atividade_form = AtividadeForm()
    trabalho_form = TrabalhoForm()

    if (request.method == "POST"):
        tipo_form = request.POST.get("tipo_form")

        if (tipo_form == "atividade"):
            atividade_form = AtividadeForm(request.POST)

            if atividade_form.is_valid():
                atividade = atividade_form.save(commit=False)
                atividade.ID_materia_id=id
                atividade.save()

                return redirect("detalhes_materia", id=id)
            
        elif (tipo_form == "trabalho"):
            trabalho_form = TrabalhoForm(request.POST)

            if trabalho_form.is_valid():

                trabalho = trabalho_form.save(commit=False)
                trabalho.ID_materia_id=id
                trabalho.save()

                return redirect("detalhes_materia", id=id)
    


    return render(request, "atividades_trabalhos.html", {"atividades": atividades, 
                                                         "trabalhos": trabalhos,
                                                         "id_periodo": materia.ID_periodo_id,
                                                         "atividade_form":atividade_form,
                                                         "trabalho_form":trabalho_form})

def detalhes_atividade(request, id):
    arquivos = Arquivo_atividade.objects.filter(ID_atividade=id)
    atividade = Atividade.objects.get(ID_atividade=id)


    if (request.method == "POST"):
        form = ArquivoAtividadeForm(request.POST, request.FILES)

        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.ID_atividade_id = id
            arquivo.save()

            return redirect("detalhes_atividade", id=id)
    else:
        form = ArquivoAtividadeForm()

    return render(request, "arquivo_atividade.html", {"arquivos":arquivos,
                                                       "form":form,
                                                       "id_materia": atividade.ID_materia_id})

def detalhes_trabalho(request, id):
    arquivos = Arquivo_trabalho.objects.filter(ID_trabalho=id)
    trabalho = Trabalho.objects.get(ID_trabalho=id)

    if (request.method == "POST"):
        form = ArquivoTrabalhoForm(request.POST, request.FILES)
        

        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.ID_trabalho_id = id
            arquivo.save()

            return redirect("detalhes_trabalho", id=id)
    else:
        form = ArquivoTrabalhoForm()

    return render(request, "arquivo_trabalho.html", {"arquivos":arquivos,
                                                     "form":form,
                                                     "id_materia":trabalho.ID_materia_id})


def editar_item(request, tipo, id):
    if (tipo == "periodo"):
        periodo = Periodo.objects.get(ID_periodo=id)

        if (request.method == "POST"):
            form = PeriodoForm(request.POST ,instance=periodo)
            if form.is_valid():
                form.save()
                return redirect("lista_periodos")
        else:
            form = PeriodoForm(instance=periodo)

    elif (tipo == "materia"):
        materia = Materia.objects.get(ID_materia=id)

        if (request.method == "POST"):
            form = MateriaForm(request.POST, instance=materia)
            if form.is_valid():
                form.save()
                return redirect("lista_materias", id=materia.ID_periodo_id)
        else:
            form = MateriaForm(instance=materia)

    elif (tipo == "atividade"):
        atividade = Atividade.objects.get(ID_atividade=id)
    elif (tipo == "trabalho"):
        trabalho = Trabalho.objects.get(ID_trabalho=id)

    
    return render(request, "editar_item.html", {"form":form, "periodo":periodo})
