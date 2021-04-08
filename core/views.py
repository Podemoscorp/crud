from user.models import User
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
from django.core.paginator import Paginator

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
        populares = (
            Post.objects.all()
            .filter(visibility="C")
            .order_by("-posted_in")
            .order_by("-views")[:6]
        )

        postagens = Post.objects.all().filter(visibility="C")

        if "order" in request.GET:
            ...
        else:
            postagens.order_by("-posted_in")

        paginator = Paginator(postagens, 30)
        page_number = 1
        if "page" in request.GET:
            page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        dados = {
            "populares": populares,
            "posts": page_obj,
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
    if not New.objects.filter(id=id).exists():
        messages.success(request, "Postagem não encontrada.")
        return redirect("index")

    new = New.objects.filter(id=id).get()

    if new.visibility == "A":
        if request.user.is_anonymous:
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("login")
        if new.poster_id != request.user.id:
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("index")

    new.views = new.views + 1
    new.save()

    return render(request, "pages/core/noticia.html", {"new": new})


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

    if not evento:
        return redirect("index")

    return render(request, "pages/core/evento.html", {"evento":evento})


def dashboard(request):
    if request.user.is_authenticated:
        certificados = Certificate.objects.all().filter(student=request.user).count()
        matriculas = Registration.objects.all().filter(student=request.user).count()
        posts = Post.objects.all().filter(poster=request.user).count()
        news = New.objects.all().filter(poster=request.user).count()
        cursos_lecionados = Course.objects.all().filter(teacher=request.user).count()
        cursos_em_andamento = Registration.objects.all().filter(finished=None).count()
        cursos_terminados = matriculas - cursos_em_andamento

        dados = {
            "certificados": certificados,
            "matriculas": matriculas,
            "posts": posts,
            "news": news,
            "cursos_lecionados": cursos_lecionados,
            "cursos_em_andamento": cursos_em_andamento,
            "cursos_terminados": cursos_terminados,
        }

        return render(request, "pages/core/dashboard.html", dados)

    else:
        return redirect("index")


def ranking(request):
    users = User.objects.all().order_by("classification")

    paginator = Paginator(users, 30)
    page_number = 1
    if "page" in request.GET:
        page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/core/ranking.html", {"users": page_obj})


def images(request):
    return render(request, "pages/core/images.html")


def image(request, id):
    return render(request, "pages/core/image.html")


def upload_image(request):
    return render(request, "pages/core/upload_image.html")

def update_ranking(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            users = User.objects.all().order_by("-points")
            ct = 1
            
            for i, user in enumerate(users):
                if i == 0:
                    user.classification = 1
                else:
                    if user.points == users[i-1].points:
                        user.classification = ct
                    else:
                        ct+=1
                        user.classification = ct

                user.save()

            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('index')
