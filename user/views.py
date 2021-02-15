from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.utils import timezone

def cadastro( request ):
    ...

def login( request ):
    if request.user.is_authenticated:
        return redirect('dashboard')
    #print(request.is_ajax())

    if request.method == "POST":


        email = request.POST['email']
        password = request.POST['password']

        if email == "" or password == "":
            menssagem = _("Os campos email e senha não podem ficar em branco")
            messages.error(request, menssagem)
            return redirect('login')

        if User.objects.filter(email=email).exists():
            email = email
        elif User.objects.filter(cpf = email).exists():
            email=User.objects.filter(cpf=email).values_list('email',flat=True).get()
        else:
            messages.error(request,"Usuario não encontrado")
            return redirect('login')

        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            menssagem = _('login realizado com sucesso')
            messages.success(request, menssagem)

                
            if not user.is_trusty:
                menssagem = _('Confirme seu email para ter acesso')
                messages.error(request,menssagem)

            return redirect('main')            

    return render(request, 'pages/login.html')

def logout ( request ):
    auth.logout(request)
    return redirect('index')

def confirma_email( request, token):
    messages.success(request,'Email confirmado com sucesso')
    return redirect('login')