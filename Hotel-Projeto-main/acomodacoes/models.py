from django.db import models


class TipoAcomodacao(models.Model):
    tipo = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.tipo

class Acomodacao(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(TipoAcomodacao, on_delete=models.PROTECT)

# Create your models here.
