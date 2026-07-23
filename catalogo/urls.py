from django.urls import path
from .views import registrar, login_view, logout_view, home_antes_do_login, home_depois_do_login, avaliar_filme, listar_filmes_favoritos, adicionar_filmes_favoritos, remover_filmes_favoritos, debug_auth, buscar_filme

urlpatterns = [
    path('', home_antes_do_login, name='home_antes_do_login'),
    path('home/', home_depois_do_login, name='home_depois_do_login'),
    path('registrar/', registrar, name='registrar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('avaliacao/', avaliar_filme, name='avaliar_filme'),
    path('filmes_favoritos/', listar_filmes_favoritos, name='listar_filmes_favoritos'),
    path('adicionar_filmes_favoritos/', adicionar_filmes_favoritos, name='adicionar_filmes_favoritos'),
    path('remover_filmes_favoritos/', remover_filmes_favoritos, name='remover_filmes_favoritos'),
    path('debug_auth/', debug_auth, name='debug_auth'),  # Para debug apenas
    path('procurarfilmes/', buscar_filme, name='procurar_filme'),
]