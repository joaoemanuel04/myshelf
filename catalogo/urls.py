from django.urls import path
from .views import CatalogoView, registrar, login_view

urlpatterns = [
    path('home/', CatalogoView.as_view(), name='catalogo-home'),
    path('registrar/', registrar, name='registrar'),
    path('login/', login_view, name='login'),
]