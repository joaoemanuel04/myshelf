from django.urls import path
from .views import CatalogoView

urlpatterns = [
    path('', CatalogoView.as_view(), name='catalogo-home'),
]