from django.shortcuts import render, redirect, get_object_or_404
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho
from .forms import PeriodoForm, MateriaForm, AtividadeForm, TrabalhoForm, ArquivoAtividadeForm, ArquivoTrabalhoForm

from django.http import Http404
from django.urls import reverse

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
    periodo = get_object_or_404(Periodo, ID_periodo=id)

    if (request.method == "POST"):
        form = MateriaForm(request.POST)

        if form.is_valid():
            materia = form.save(commit=False)
            materia.ID_periodo_id = id
            materia.save()

            return redirect("lista_materias", id=id)
    else:
        form = MateriaForm()

    return render(request, "materias.html", {"materias": materias, 
                                             "form":form,
                                             "periodo":periodo})

def detalhes_materia(request, id):
    materia = get_object_or_404(Materia, ID_materia=id)
    atividades = Atividade.objects.filter(ID_materia=id)
    trabalhos = Trabalho.objects.filter(ID_materia=id)

    

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
    atividade = get_object_or_404(Atividade, ID_atividade=id)    
    arquivos = Arquivo_atividade.objects.filter(ID_atividade=atividade)

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
    trabalho = get_object_or_404(Trabalho, ID_trabalho=id)
    arquivos = Arquivo_trabalho.objects.filter(ID_trabalho=trabalho)

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
        periodo = get_object_or_404(Periodo, ID_periodo=id)
        objeto = periodo

        if (request.method == "POST"):
            form = PeriodoForm(request.POST, instance=periodo)
            if form.is_valid():
                form.save()
                return redirect("lista_periodos")
        else:
            form = PeriodoForm(instance=periodo)

    elif (tipo == "materia"):
        materia = get_object_or_404(Materia, ID_materia=id)
        objeto = materia

        if (request.method == "POST"):
            form = MateriaForm(request.POST, instance=materia)
            if form.is_valid():
                form.save()
                return redirect("lista_materias", id=materia.ID_periodo_id)
        else:
            form = MateriaForm(instance=materia)

    elif (tipo == "atividade"):
        atividade = get_object_or_404(Atividade, ID_atividade=id)
        objeto = atividade

        if (request.method == "POST"):
            form = AtividadeForm(request.POST, instance=atividade)
            if form.is_valid():
                form.save()
                return redirect("detalhes_materia", id=objeto.ID_materia_id)
        else:
            form = AtividadeForm(instance=atividade)

    elif (tipo == "trabalho"):
        trabalho = get_object_or_404(Trabalho, ID_trabalho=id)
        objeto = trabalho

        if(request.method == "POST"):
            form = TrabalhoForm(request.POST, instance=trabalho)
            if form.is_valid():
                form.save()
                return redirect("detalhes_materia", id=trabalho.ID_materia_id)
        else:
            form = TrabalhoForm(instance=trabalho)
    else:
        raise Http404("Tipo de registro não encontrado.")
    
    return render(request, "editar_item.html", {"form":form, "objeto":objeto})

def excluir_item(request, tipo, id):
    if (tipo == "periodo"):
        periodo = get_object_or_404(Periodo, ID_periodo=id)
        objeto = periodo
        voltar_url =  reverse("lista_periodos")

        if (request.method == "POST"):
            periodo.delete()

            return redirect("lista_periodos")
    elif (tipo == "materia"):
        materia = get_object_or_404(Materia, ID_materia=id)
        objeto = materia
        voltar_url = reverse("lista_materias", args=[materia.ID_periodo_id])

        if (request.method == "POST"):
            materia.delete()

            return redirect("lista_materias", id=objeto.ID_periodo_id)
    elif (tipo == "atividade"):
        atividade = get_object_or_404(Atividade, ID_atividade=id)
        objeto = atividade
        voltar_url = reverse("detalhes_materia", args=[atividade.ID_materia_id])

        if (request.method == "POST"):
            atividade.delete()

            return redirect ("detalhes_materia", id=objeto.ID_materia_id)
    elif (tipo == "trabalho"):
        trabalho = get_object_or_404(Trabalho, ID_trabalho=id)
        objeto = trabalho
        voltar_url = reverse("detalhes_materia", args=[trabalho.ID_materia_id])

        if (request.method == "POST"):
            trabalho.delete()

            return redirect("detalhes_materia", id=objeto.ID_materia_id)
    elif (tipo == "arquivo_atividade"):
        arquivo_atividade = get_object_or_404(Arquivo_atividade, ID_arquivo=id)
        objeto = arquivo_atividade
        voltar_url = reverse("detalhes_atividade", args=[arquivo_atividade.ID_atividade_id])

        if (request.method == "POST"):
            arquivo_atividade.delete()

            return redirect("detalhes_atividade", id=objeto.ID_atividade_id)
    elif (tipo == "arquivo_trabalho"):
        arquivo_trabalho = get_object_or_404(Arquivo_trabalho, ID_arquivo=id)
        objeto = arquivo_trabalho
        voltar_url = reverse("detalhes_trabalho", args=[arquivo_trabalho.ID_trabalho_id])

        if (request.method == "POST"):
            arquivo_trabalho.delete()

            return redirect("detalhes_trabalho", id=objeto.ID_trabalho_id)
    else:
        raise Http404("Tipo de registro não encontrado.")

    return render(request, "confirmar_exclusao.html", {"objeto":objeto, 
                                                       "voltar_url":voltar_url,
                                                       "tipo":tipo})

def erro_404(request, exception):
    return render(request, "erro_404.html", status=404)
    

