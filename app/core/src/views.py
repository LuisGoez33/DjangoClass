from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni': 'los saluda Luis Pablo Goez', 'titulo2': 'Clases de python'})

class QuienesSomosPageView(TemplateView):

    template_name = "quienes_somos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulonosotros': 'Acerca de nosotros', 'descripcion': 'Somos asi'})