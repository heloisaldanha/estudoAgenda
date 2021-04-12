from django.contrib import admin
from .models import Categoria, Contato
# (1) - contatos/README.md


class ContatoAdmin(admin.ModelAdmin):  # (2) - contatos/README.md
    # mostra os atributos (que desejar) da classe contato.
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'mostrar')

    # Deixa ESSES atributos linkados
    list_display_links = ('id', 'nome', 'sobrenome')

    # Filtrar por atributos
    # list_filter = ('nome', 'sobrenome')

    # Mostrar x elementos por página
    list_per_page = 10

    # buscar
    search_fields = ('nome', 'sobrenome')

    # para editar sem precisar abrir o formulário
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)  # precisa passar ContatoAdmin como parâmetro também (lembrar)
