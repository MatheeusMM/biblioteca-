from django.contrib import admin

from biblioteca.models import Livros

@admin.register(Livros)
class Pagina(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'classificacao')
    search_fields = ('titulo', 'autor', 'ano')
    list_filter = ('autor',)
    date_hierarchy = 'data_cadastro'
    