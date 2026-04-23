from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Filmes, Genero, Avaliacao
from django.contrib import messages 
from .urls import *
from .forms import RegistrarForm
from django.contrib.auth import authenticate, login

class CatalogoView(TemplateView):
    template_name = 'catalogo/homecatalogo.html'

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro bem-sucedido! Faça login para continuar.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, preencha todos os campos corretamente.')
            form = RegistrarForm()  # Limpa o formulário para nova tentativa
            return redirect('registrar')
    
    return render(request, 'registrar.html', {'form': RegistrarForm()})  

def login_view(request):
    if request.method == 'POST':
        email_digitado = request.POST.get('email') # Certifique-se que o name no HTML é 'email'
        senha_digitada = request.POST.get('password')

        user = authenticate(request, email=email_digitado, password=senha_digitada)

        if user is not None:
            login(request, user)
            messages.success(request, 'Bem-vindo de volta!')
            return redirect('registrar') # Para onde ele vai após logar
        else:
            messages.error(request, 'E-mail ou senha incorretos.')
            return redirect('login')

    return render(request, 'login.html')



 