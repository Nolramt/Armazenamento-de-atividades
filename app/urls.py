from django.urls import path
from .views import lista_periodos, lista_materias, detalhes_materia, detalhes_atividade, detalhes_trabalho

urlpatterns = [
    path("", lista_periodos, name="lista_periodos"),
    path("periodo/<int:id>/", lista_materias, name="lista_materias"),
    path("materia/<int:id>/", detalhes_materia, name="detalhes_materia"),
    path("atividade/<int:id>/", detalhes_atividade, name="detalhes_atividade"),
    path("trabalho/<int:id>/", detalhes_trabalho, name="detalhes_trabalho"),
]