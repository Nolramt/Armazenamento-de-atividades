from django.contrib import admin
from .models import Periodo, Materia, Atividade, Trabalho, Arquivo_atividade, Arquivo_trabalho

# Register your models here.

admin.site.register(Periodo)
admin.site.register(Materia)
admin.site.register(Atividade)
admin.site.register(Trabalho)
admin.site.register(Arquivo_atividade)
admin.site.register(Arquivo_trabalho)
