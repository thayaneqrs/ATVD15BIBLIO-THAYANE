from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ano_nascimento = models.IntegerField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    data_lancamento = models.DateField()
    resumo = models.TextField()
    editora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo