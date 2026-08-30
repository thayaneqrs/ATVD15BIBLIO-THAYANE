from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/livros.html', {'livros': livros})


def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'acervo/livro_detalhes.html', {'livro': livro})


def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'acervo/autores.html', {'autores': autores})


def detalhe_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'acervo/autor_detalhes.html', {'autor': autor})