from pyexpat import model
from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano = models.DateField(auto_now_add=True)
    classificacao = models.DecimalField(max_digits=2, decimal_places=1)
    data_cadastro = models.DateField(auto_now=True)
    observacao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Livro'

    def __str__(self):
        return self.titulo