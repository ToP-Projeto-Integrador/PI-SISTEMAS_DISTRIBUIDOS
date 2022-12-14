import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Produto(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.PROTECT)

    icon = models.FileField(upload_to="product_icons",
                            max_length=100, null=False, blank=True, default="default.jpg")

    nome = models.CharField(
        max_length=130,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    tipo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    perecivel_produto_choices = [
        ('0', 'Não'),
        ('1', 'Sim')
    ]

    perecivel = models.CharField(
        choices=perecivel_produto_choices,
        max_length=3,
        default=0
    )

    validade = models.DateField(
        auto_now=False,
        auto_now_add=False
    )

    quantidade = models.IntegerField()


class UploadFile(models.Model):
    file = models.FileField(upload_to="backup", null=True, blank=True)
