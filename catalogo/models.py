from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# 1. Gênero
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, db_column='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'genero'

# 2. Filmes
class Filmes(models.Model):
    id_filmes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, db_column='Nome')
    ano = models.CharField(max_length=4, blank=True, null=True, db_column='Ano')
    duracao = models.TimeField(blank=True, null=True, db_column='duracao')
    faixa_etaria = models.IntegerField(blank=True, null=True, db_column='faixa_etaria')
    sinopse = models.TextField(blank=True, null=True, db_column='Sinopse')
    
    # Campo Extra para o seu Front-end 
    url_capa = models.URLField(max_length=500, blank=True, null=True)

    # Relacionamento Muitos-para-Muitos 
    generos = models.ManyToManyField(Genero, related_name='filmes')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'filmes'

# 3. Usuário 
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um e-mail')
        user = self.model(email=self.normalize_email(email), nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, db_column='Nome')
    email = models.EmailField(max_length=100, unique=True)
    nickname = models.CharField(max_length=45, unique=True, db_column='Nickname')
    
    # O campo password já vem embutido no AbstractBaseUser, 
    # por isso não precisamos declarar o campo 'senha' manualmente.

    objects = UsuarioManager()

    USERNAME_FIELD = 'email' # O que ele vai usar para logar
    REQUIRED_FIELDS = ['nickname', 'nome']

    class Meta:
        db_table = 'usuario'

# 4. Avaliação
class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    NOTAS_CHOICES = [(i, str(i)) for i in range(1, 6)] 
    nota = models.IntegerField(choices=NOTAS_CHOICES)
    
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes')

    class Meta:
        db_table = 'avaliacao'

# 5. Filmes Favoritos
class FilmesFavoritos(models.Model):
    id_filme_fav = models.AutoField(primary_key=True)
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'filmes_favoritos'