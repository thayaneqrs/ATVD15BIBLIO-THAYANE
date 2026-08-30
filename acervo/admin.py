
# Register your models here.
from django.contrib import admin
from .models import Livro, Autor


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_lancamento', 'editora')
    search_fields = ('titulo', 'editora')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ano_nascimento')
    search_fields = ('nome', 'email')