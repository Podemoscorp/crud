from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.


class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField()
    arquivo = models.FileField(upload_to="%Y/%m/%d/", blank=True)
    postado_em = models.DateTimeField(default=timezone.now, blank=True)
    postador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    criado_em = models.DateTimeField(default=timezone.now, blank=True)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now, blank=True)


class Certificado(models.Model):
    titulo = titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to="%Y/%m/%d/", blank=True)
    professor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Professor"
    )
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Alunos")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.titulo
