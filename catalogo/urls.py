from django.urls import path
from .views import registrar, login_view, home_antes_do_login, home_depois_do_login

urlpatterns = [
    path('', home_antes_do_login, name='home_antes_do_login'),
    path('home/', home_depois_do_login, name='home_depois_do_login'),
    path('registrar/', registrar, name='registrar'),
    path('login/', login_view, name='login'),
]