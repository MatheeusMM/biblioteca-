from django import forms

from biblioteca.models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        