from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse
from .models import DatosUser

# Create your views here.

class QuienesSomosPageView(TemplateView):

    template_name = "quienes_somos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class IndexListView(ListView):
    model = DatosUser
    template_name: 'quienes_somos.html'