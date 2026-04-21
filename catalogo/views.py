from django.shortcuts import render
from django.views.generic import TemplateView

class catalogoView(TemplateView):
    template_name = 'homecatalogo.html'


