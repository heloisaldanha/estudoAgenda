from django.db import models
from contatos.models import Contato
from django import forms


class FormContato(forms.ModelForm):  
    class Meta:
        model = Contato  # esse model representa a classe Contato
        exclude = ('mostrar', )  # exclui algum campo que não queira que apareça
