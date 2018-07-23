from django.db import models
from django.utils import timezone


class Visitante(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    observacoes = models.TextField(blank=True)
    data_hora = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "visitantes"

    def publish(self):
        self.data_hora = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
