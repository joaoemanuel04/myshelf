# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Avaliao(models.Model):
    idavaliaþÒo = models.IntegerField(db_column='idAvaliaþÒo', primary_key=True)  # Field name made lowercase.
    nota = models.CharField(db_column='Nota', max_length=1, blank=True, null=True)  # Field name made lowercase.
    filmes_idfilmes = models.ForeignKey('Filmes', models.DO_NOTHING, db_column='Filmes_idFilmes')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'avaliaþÒo'


class Filmes(models.Model):
    idfilmes = models.IntegerField(db_column='idFilmes', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=180)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duraþÒo = models.TimeField(blank=True, null=True)
    faixa_etßria = models.IntegerField(db_column='Faixa etßria', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sinopse = models.TextField(db_column='Sinopse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'filmes'


class FilmesFavoritos(models.Model):
    idfilmefav = models.IntegerField(db_column='idFilmeFav', primary_key=True)  # Field name made lowercase.
    filmes_idfilmes = models.ForeignKey(Filmes, models.DO_NOTHING, db_column='Filmes_idFilmes')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'filmes_favoritos'


class FilmesHasFilmes(models.Model):
    pk = models.CompositePrimaryKey('Filmes_idFilmes', 'Filmes_idFilmes1')
    filmes_idfilmes = models.ForeignKey(Filmes, models.DO_NOTHING, db_column='Filmes_idFilmes')  # Field name made lowercase.
    filmes_idfilmes1 = models.ForeignKey(Filmes, models.DO_NOTHING, db_column='Filmes_idFilmes1', related_name='filmeshasfilmes_filmes_idfilmes1_set')  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'filmes_has_filmes'


class FilmesHasGnero(models.Model):
    id_filmes_genero = models.CharField(primary_key=True, max_length=45)
    filmes_idfilmes = models.ForeignKey(Filmes, models.DO_NOTHING, db_column='Filmes_idFilmes')  # Field name made lowercase.
    gÛnero_idgÛnero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='GÛnero_idGÛnero')  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'filmes_has_gÛnero'


class Genero(models.Model):
    idgÛnero = models.IntegerField(db_column='idGÛnero', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'genero'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)
    nickname = models.CharField(db_column='Nickname', max_length=45)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'usuario'
