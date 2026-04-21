from django.shortcuts import render
from django.views.generic import TemplateView

class CatalogoView(TemplateView):
    template_name = 'catologo/homecatalogo.html'


