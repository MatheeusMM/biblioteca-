from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from biblioteca.models import Livros


class LivroList(ListView):
    model = Livros
    queryset = Livros.objects.all()
    template_name = 'home.html'

class ClienteCreate(CreateView):
    model = Livros 
    fields = '__all__'
    template_name = 'create_form.html'
    success_url = reverse_lazy('livro')

class ClienteUpdate(UpdateView):
    model = Livros
    fields = '__all__'
    template_name = 'editar.html'
    success_url = reverse_lazy('livro')

class ClienteDetail(DetailView):
    queryset = Livros.objects.all()
    template_name = 'detail.html'

class ClienteDelete(DeleteView):
    queryset = Livros.objects.all()
    template_name = 'delete.html'
    success_url = reverse_lazy('livro')
