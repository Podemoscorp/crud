from django.db.models.query import QuerySet
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
from django.core import serializers
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.


def handler404(request, *args, **argv):
    return render(request, "error/404.html", status=404)


def handler500(request, *args, **argv):
    return render(request, "error/500.html", status=500)


def handler403(request, *args, **argv):
    return render(request, "error/403.html", status=403)


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
            "posts": postagens,
        }

        return render(request, "pages/core/blog.html", dados)


def post(request, id):

    if not Post.objects.filter(id=id).exists():
        messages.success(request, "Postagem não encontrada.")
        return redirect("index")

    post = Post.objects.filter(id=id).get()

    if post.visibility == "A":
        if request.user.is_anonymous:
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
    if request.is_ajax():
        eventos = Event.objects.all()

        if "tipo" in request.GET:
            tipo = request.GET["tipo"]

            if tipo == "A":
                eventos = eventos.filter(tipo="A")
            elif tipo == "B":
                eventos = eventos.filter(tipo="B")
            elif tipo == "C":
                eventos = eventos.filter(tipo="C")

        if "regiao" in request.GET:
            regiao = request.GET["regiao"]

            if regiao == "A":
                eventos = eventos.filter(regiao="A")
            elif regiao == "B":
                eventos = eventos.filter(regiao="B")

        queryset_json = serializers.serialize("json", eventos)

        return HttpResponse(queryset_json, content_type="application/json")

    return render(request, "pages/core/calendario.html")


def evento(request, id):
    evento = Event.objects.all().filter(id=id).get()

    if evento:
        ...
    else:
        return redirect("index")

    return render(request, "pages/core/evento.html")


def dashboard(request):
    return render(request, "pages/core/dashboard.html")


def images(request):
    return render(request, "pages/core/images.html")


def image(request, id):
    return render(request, "pages/core/image.html")


def upload_image(request):
    return render(request, "pages/core/upload_image.html")
