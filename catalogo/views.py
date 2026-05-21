from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Filmes, Genero, Avaliacao, FilmesFavoritos
from django.contrib import messages 
from .urls import *
from .forms import RegistrarForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

def home_antes_do_login(request):
    try:
        return render(request, 'base.html')
    except Exception as e:
        return HttpResponse(f"Erro ao carregar a página inicial.  Erro em: {str(e)}.")

def home_depois_do_login(request):
    try:
        return render(request, 'home.html')
    except Exception as e:
        return HttpResponse(f"Erro ao carregar a página inicial.  Erro em: {str(e)}.")

def avaliar_filme(request):
    filmes = Filmes.objects.all().order_by('nome') # Trazendo os filmes do banco de dados para a view de forma ordenada.

    if request.method == 'POST':
        # Obtendo dados do formlário aplicado.
        filme_id = request.POST.get('filme-id')
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')
        
        #Validando os dados coletados do formulário.
        try:
            filme = Filmes.objects.get(id_filmes=filme_id)
        except Filmes.DoesNotExist:
            messages.error(request, 'Filme não encontrado.')
            return redirect('avaliar-filme')
        
        if not nota or not comentario:
            messages.error(request, 'Insira um nota ou comentário válido para avaliar o filme.')
            return redirect('avaliar-filme')
        
        # Criando uma avaliação sobre os filmes.
        Avaliacao.objects.create(
            filme=filme,
            nota=nota,
            comentario=comentario,
            usuario=None # Não será necessário login para avaliar, logo, virá como None.
        )
        
        messages.success(request, 'Avaliação registrada com sucesso !')
        return redirect('home_depois_do_login')
    
    return render(request, 'avaliar_filme.html', {'filmes': filmes})

def listar_filmes_favoritos(request):
    filmes = Filmes.objects.all().order_by('nome') # Trazendo os filmes do banco de dados para a view de forma ordenada.
    return render(request, 'filmes_favoritos.html', {'filmes': filmes})

def adicionar_filmes_favoritos(request): 
    if request.method == 'POST':

        filme_id = request.POST.get('filme-id')
        try:
            usuario = request.user
            id_usuario = usuario.id_usuario

            FilmesFavoritos.objects.create(
                filme_id=filme_id,
                usuario_id=id_usuario
            )

            messages.success(request, 'Filme adicionado aos favoritos com sucesso!')
            return redirect('listar_filmes_favoritos')
        except Exception as e:
            messages.error(request, f'Erro ao adicionar filme aos favoritos: {str(e)}')
            return redirect('listar_filmes_favoritos')
    
    return render(request, 'filmes_favoritos.html')

def remover_filmes_favoritos(request): 
    if request.method == 'POST':
        filme_id = request.POST.get('filme-id')
        try:
            usuario = request.user
            id_usuario = usuario.id_usuario

            favorito = FilmesFavoritos.objects.get(filme_id=filme_id, usuario_id=id_usuario)
            favorito.delete()

            messages.success(request, 'Filme removido dos favoritos com sucesso!')
            return redirect('listar_filmes_favoritos')
        except FilmesFavoritos.DoesNotExist:
            messages.error(request, 'Filme favorito não encontrado.')
            return redirect('listar_filmes_favoritos')
        except Exception as e:
            messages.error(request, f'Erro ao remover filme dos favoritos: {str(e)}')
            return redirect('listar_filmes_favoritos')

    
    return render(request, 'filmes_favoritos.html')
        

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
        email_digitado = request.POST.get('email')
        senha_digitada = request.POST.get('password')

        # O backend customizado usa 'username' para o email
        user = authenticate(request, username=email_digitado, password=senha_digitada)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Bem-vindo de volta!')
            return redirect('home_depois_do_login')
        else:
            messages.error(request, 'E-mail ou senha incorretos.')
            return redirect('login')

    return render(request, 'login.html')



 