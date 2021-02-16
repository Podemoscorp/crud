from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.utils import timezone
from crud.settings import EMAIL_HOST_USER


def cadastro( request ):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        ...

    return render(request, "pages/cadastro.html")

def login( request ):
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


def logout( request ):
    auth.logout(request)
    return redirect("index")


def confirma_email( request , token ):
    messages.success(request, "Email confirmado com sucesso")
    return redirect("login")

def reset_password( request ):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST['email']
        user = get_object_or_404(User, email=email)

        token = str(user.get_confirm_email_token())

        new_token = ""
        for i in range(2, len(token) - 1):
            new_token += token[i]

        path = request.build_absolute_uri()
        path = path.strip(request.get_full_path())
        path+="/user/reset_password_confirm/"

        link = path+new_token

        user.email_user('Resetar senha', render(request, 'email/reset_password_email.html', {"link":link, "user_email":user}), EMAIL_HOST_USER)

        return redirect("reset_password_done")

    return render(request, "pages/reset_password.html")

def reset_password_done( request ):
    return render(request, 'pages/reset_password_done.html')