from django.db import models

class UsuarioLogado(models.Model):
    email = models.EmailField(unique=True)
    data_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='jogos/')

    def __str__(self):
        return self.nome