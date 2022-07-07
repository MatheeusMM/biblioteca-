from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('', views.LivroList.as_view(), name='livro'),
    path('cadastro/', views.ClienteCreate.as_view(), name='cadastro'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete'),
]