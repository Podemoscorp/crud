from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.utils import timezone
from crud.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect
import datetime


def cadastro(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        ...

    return render(request, "pages/cadastro.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    # print(request.is_ajax())

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        if email == "" or password == "":
            menssagem = _("Os campos email e senha não podem ficar em branco")
            messages.error(request, menssagem)
            return redirect("login")

        if User.objects.filter(email=email).exists():
            email = email
        elif User.objects.filter(cpf=email).exists():
            email = User.objects.filter(cpf=email).values_list("email", flat=True).get()
        else:
            messages.error(request, "Usuario não encontrado")
            return redirect("login")

        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            menssagem = _("login realizado com sucesso")
            messages.success(request, menssagem)

            if not user.is_trusty:
                menssagem = _("Confirme seu email para ter acesso")
                messages.error(request, menssagem)

            return redirect("dashboad")

    return render(request, "pages/login.html")


def logout(request):
    auth.logout(request)
    return redirect("index")


def confirma_email(request, token):
    messages.success(request, "Email confirmado com sucesso")
    return redirect("login")


def reset_password(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        email = request.POST["email"]

        user = None

        try:
            user = get_object_or_404(User, email=email)
        except:
            return redirect("reset_password_done")

        token = str(user.get_reset_password_token())

        new_token = ""
        for i in range(2, len(token) - 1):
            new_token += token[i]

        path = request.build_absolute_uri()
        path = path.strip(request.get_full_path())
        path += "/user/reset_password_confirm/"

        link = path + new_token

        user.email_user(
            "Resetar senha",
            strip_tags(
                render_to_string(
                    "email/reset_password_email.html",
                    {"link": link, "user": user},
                )
            ),
            EMAIL_HOST_USER,
        )

        return redirect("reset_password_done")

    return render(request, "pages/reset_password.html")


def reset_password_done(request):
    return render(request, "pages/reset_password_done.html")


def reset_password_confirm(request, token):
    user = User()
    payload = user.verify_reset_password_token(token)

    if payload == None:
        messages.success(request, "Token Invalido")
        return redirect("login")

    if type != 0:
        messages.success(request, "Token Invalido")
        return redirect("login")

    data_atual = str(timezone.now)
    data_atual = data_atual.split(".")[0]
    data_atual = datetime.strptime(data_atual, "%Y-%m-%d %H:%M:%S")
    data = payload["expira"].split(".")[0]
    data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    tempo = ((data_atual - data).total_seconds()) / 60

    if tempo > 60:
        messages.success(request, "Token Expirado")
        return redirect("login")

    user = None

    try:
        user = get_object_or_404(User, pk=payload["id"])
    except:
        messages.success(request, "Token Invalido")
        return redirect("login")

    return render(request, "pages/reset_password_confirm")


def confirma_email(request, token):
    user = User()

    payload = user.verify_confirm_email_token(token)

    if payload == None:
        messages.success(request, "Token Invalido")
        return redirect("login")

    if type != 1:
        messages.success(request, "Token Invalido")
        return redirect("login")

    data_atual = str(timezone.now)
    data_atual = data_atual.split(".")[0]
    data_atual = datetime.strptime(data_atual, "%Y-%m-%d %H:%M:%S")
    data = payload["expira"].split(".")[0]
    data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    tempo = ((data_atual - data).total_seconds()) / 60

    if tempo > 60:
        messages.success(request, "Token Expirado")
        return redirect("login")

    user = None

    try:
        user = get_object_or_404(User, pk=payload["id"])
    except:
        messages.success(request, "Token Invalido")
        return redirect("login")

    user.is_trusty = 1
    user.save()
    messages.success(request, "Email confirmado com sucesso")
    return redirect("login")


def perfil(request, id):
    visit_user = User.objects.get(pk=id)

    if visit_user == None:
        messages.success(request, "User não encontrado")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return render(request, "pages/perfil.html", visit_user)


def editar_perfil(request):
    return render(request, "pages/editar_perfil.html")
