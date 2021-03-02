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

from django.contrib import auth, messages

# Create your views here.


def index(request):
    noticias = New.objects.all().filter(visibility="C").order_by("-posted_in")[:6]
    posts = Post.objects.all().filter(visibility="C").order_by("-posted_in")[:3]
    tipos_de_cursos = CourseType.objects.all()

    dados = {
        "noticias": noticias,
        "posts": posts,
        "tipos_de_cursos": tipos_de_cursos,
    }

    return render(request, "pages/core/index.html", dados)


def blog(request):

    if request.is_ajax():
        ...

    else:
        ultimas_postagens = (
            Post.objects.all().filter(visibility="C").order_by("-posted_in")[:6]
        )
        populares = (
            Post.objects.all()
            .filter(visibility="C")
            .order_by("-views")
            .order_by("-posted_in")[:6]
        )

        postagens = None

        if "order" in request.GET:
            ...
        else:
            postagens = Post.objects.all().filter(visibility="C").order_by("-posted_in")

        dados = {
            "ultimas_postagens": ultimas_postagens,
            "populares": populares,
            "postagens": postagens,
        }

        return render(request, "pages/core/blog.html", dados)


def post(request, id):

    if not Post.objects.filter(id=id).exists():
        messages.success(request, "Postagem não encontrada.")
        return redirect("index")

    post = Post.objects.filter(id=id).get()

    if post.visibility == "A":
        if not request.user.is_authenticated():
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("login")
        if post.poster_id != request.user.id:
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("index")

    post.views = post.views + 1
    post.save()

    return render(request, "pages/core/post.html", {"post": post})


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
