from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Arquivo_atividade, Arquivo_trabalho


@receiver(post_delete, sender=Arquivo_atividade)
def excluir_arquivo_atividade(sender, instance, **kwargs):
    if instance.arquivo:
        instance.arquivo.delete(save=False)


@receiver(post_delete, sender=Arquivo_trabalho)
def excluir_arquivo_trabalho(sender, instance, **kwargs):
    if instance.arquivo:
        instance.arquivo.delete(save=False)