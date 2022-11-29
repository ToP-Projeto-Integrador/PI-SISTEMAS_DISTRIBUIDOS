import os

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"product_{instance.name}_{instance.id:0>4}.{ext}"
    return os.path.join('uploads', filename)


class Produto(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.PROTECT)
    icon = models.FileField(upload_to=content_file_name, max_length=100)
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

    tipo_produto_choices = [
        ('0', 'Não'),
        ('1', 'Sim')
    ]

    Perecivel = models.CharField(
        choices=tipo_produto_choices,
        max_length=3,
        default=0
    )

    validade = models.DateField(
        auto_now=False,
        auto_now_add=False
    )

    quantidade = models.IntegerField()

class UploadFile(models.Model):
    file = models.FileField(upload_to="backup", null=False)