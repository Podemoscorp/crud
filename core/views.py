from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "pages/core/index.html")


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
