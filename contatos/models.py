from django.db import models
from django.utils import timezone  # para importação de datas


class Categoria(models.Model):  # (3) - README - contatos/README.md
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome  # (5) - README - contatos/README.md


# a classe herda models.Model
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)  # (1) - README - contatos/README.md
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateField(default=timezone.now)  # pega a data atual
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)  # (2) - README - contatos/README.md
    mostrar = models.BooleanField(default=True)  # mostrar os dados por padrão
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')  # blank = pode ser vazia
    # upload_to (6) - README - contatos/README.md

    def __str__(self):
        return self.nome

    # python manage.py migrate (antes de começar o model)
    # python manage.py makemigrations (depois de finalizar o model)
    # python manage.py migrate (para mandar para a base de dados)
    # (4) - README - contatos/README.md
