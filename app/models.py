from django.db import models

# Create your models here.

class Periodo(models.Model):
    ID_periodo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
class Materia(models.Model):
    ID_materia = models.AutoField(primary_key=True)
    ID_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=50)
    ultima_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):

    TIPOS = [
            ("avaliativa", "Avaliativa"),
            ("normal", "Normal"),
        ]
    
    ID_atividade = models.AutoField(primary_key=True)
    ID_materia = models.ForeignKey(
        Materia, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=50)
    data_criacao = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=30, choices=TIPOS)

    def __str__(self):
        return self.nome
    
class Trabalho(models.Model):

    TIPOS = [
            ("avaliativa", "Avaliativa"),
            ("normal", "Normal"),
        ]
    
    ID_trabalho = models.AutoField(primary_key=True)
    ID_materia = models.ForeignKey(
        Materia, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=50)
    data_criacao = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=30, choices=TIPOS)

    def __str__(self):
        return self.nome
    
class Arquivo_atividade(models.Model):
    ID_arquivo = models.AutoField(primary_key=True)
    ID_atividade = models.ForeignKey(
        Atividade, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to="atividades/")
    data_anexo = models.DateField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Arquivo_trabalho(models.Model):
    ID_arquivo = models.AutoField(primary_key=True)
    ID_trabalho = models.ForeignKey(
        Trabalho, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to="trabalhos/")
    data_anexo = models.DateField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
