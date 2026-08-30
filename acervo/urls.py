from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('', views.lista_livros, name='inicio'),

    path('livros/', views.lista_livros, name='livros'),
    path('livros/<int:id>/', views.detalhe_livro, name='livro_detalhes'),

    path('autores/', views.lista_autores, name='autores'),
    path('autores/<int:id>/', views.detalhe_autor, name='autor_detalhes'),
]