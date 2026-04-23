from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Filmes, Genero, Usuario, UsuarioManager,  Avaliacao
from django.contrib import messages 
from .urls import *
from django import forms 
from django.contrib.auth import authenticate, login

class CatalogoView(TemplateView):
    template_name = 'catalogo/homecatalogo.html'

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'nickname', 'password']

    def save(self, commit=True):
        # Agora o super() vai encontrar o método save do ModelForm
        user = super(RegistrarForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

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



 