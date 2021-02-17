from django.shortcuts import render, redirect
from core.models import (
    New,
    Course,
    Certificate,
    Post,
    Registration,
    Event,
    Image,
    CourseType,
)

# Create your views here.


def index(request):
    noticias = New.objects.all().filter(visibility="C").order_by("-posted_in")[:6]
    posts = Post.objects.all().filter(visibility="C").order_by("-posted_in")[:6]
    tipos_de_cursos = CourseType.objects.all()

    dados = {
        "noticias": noticias,
        "posts": posts,
        "tipos_de_cursos": tipos_de_cursos,
    }

    return render(request, "pages/core/index.html", dados)


def blog(request):
    return render(request, "pages/core/blog.html")


def post(request, id):
    return render(request, "pages/core/post.html")


def criar_post(request):
    return render(request, "pages/core/criar_post.html")


def noticia(request, id):
    return render(request, "pages/core/noticia.html")


def criar_noticia(request):
    return render(request, "pages/core/criar_noticia.html")


def cursos(request):
    return render(request, "pages/core/cursos.html")


def curso(request, id):
    return render(request, "pages/core/curso.html")


def criar_curso(request):
    return render(request, "pages/core/criar_curso.html")


def olimpiadas(request):
    return render(request, "pages/core/olimpiadas.html")


def olimpiada(request, id):
    return render(request, "pages/core/olimpiada.html")


def calendario(request):
    return render(request, "pages/core/calendario.html")


def evento(request, id):
    return render(request, "pages/core/evento.html")


def dashboard(request):
    return render(request, "pages/core/dashboard.html")


def images(request):
    return render(request, "pages/core/images.html")


def image(request, id):
    return render(request, "pages/core/image.html")


def upload_image(request):
    return render(request, "pages/core/upload_image.html")
