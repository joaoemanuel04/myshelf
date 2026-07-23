import requests
from django.core.management.base import BaseCommand
from catalogo.models import Filmes, Genero
from datetime import datetime
import os
from dotenv import load_dotenv

class Command(BaseCommand):
    help = 'Busca filmes de uma API externa (TMDB) e alimenta o banco de dados do MyShelf'

    def handle(self, *args, **options):
        # 1. Configurações da API externa (TMDB)
        # Substitua pelo seu token/chave gerado no painel do TMDB
        load_dotenv()
        API_KEY = os.getenv('api_key')
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=pt-BR&page=1'

        self.stdout.write(self.style.WARNING('Iniciando requisição para a API externa...'))

        try:
            # 2. Fazendo a requisição HTTP GET
            response = requests.get(URL)
            response.raise_for_status() # Lança um erro se a requisição falhar
            dados = response.json()     # Converte a resposta bruta em um dicionário Python
            
            filmes_lista = dados.get('results', [])
            
            self.stdout.write(self.style.SUCCESS(f'Conexão bem-sucedida! {len(filmes_lista)} filmes encontrados.'))

            # 3. Iterando sobre cada filme recebido da API
            for item in filmes_lista:
                nome_filme = item.get('title')
                sinopse = item.get('overview')
                
                # O TMDB retorna a data completa (AAAA-MM-DD), vamos extrair apenas o ano
                data_lancamento = item.get('release_date', '')
                ano = data_lancamento.split('-')[0] if data_lancamento else None
                
                # Construindo a URL completa da imagem da capa
                caminho_poster = item.get('poster_path')
                url_capa = f'https://image.tmdb.org/t/p/w500{caminho_poster}' if caminho_poster else None

                # 4. Salvando ou atualizando o Filme no Banco de Dados
                # O update_or_create evita duplicar filmes se você rodar o script mais de uma vez
                filme, criado = Filmes.objects.update_or_create(
                    nome=nome_filme,
                    defaults={
                        'ano': ano,
                        'sinopse': sinopse,
                        'url_capa': url_capa,
                        'duracao': None,       # A rota "popular" não traz a duração, precisaria de outra requisição por ID
                        'faixa_etaria': None,  # Mapeado como None inicialmente
                    }
                )

                if criado:
                    self.stdout.write(self.style.SUCCESS(f'Filme adicionado: "{nome_filme}"'))
                else:
                    self.stdout.write(self.style.WARNING(f'Filme atualizado: "{nome_filme}"'))

            self.stdout.write(self.style.SUCCESS('Processo de alimentação concluído com sucesso!'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Erro de comunicação com a API: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))