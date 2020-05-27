from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni': 'los saluda Luis Pablo Goez', 'titulo2': 'Clases de python'})


#class NosotrosPageView(TemplateView):

 #   template_name = "nosotros.html"

    # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs)
    #     context['tituloIni'] = "Texto de titulo"
    #     context['titulo2'] = "Otro titulo"
    #     return context