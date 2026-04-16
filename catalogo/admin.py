from django.contrib import admin
from .models import Filmes, Genero, Usuario, Avaliacao, FilmesFavoritos

admin.site.register(Filmes)
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Avaliacao)
admin.site.register(FilmesFavoritos)


 