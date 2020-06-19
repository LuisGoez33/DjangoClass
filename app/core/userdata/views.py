from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse

# Create your views here.

class QuienesSomosPageView(TemplateView):

    template_name = "quienes_somos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)