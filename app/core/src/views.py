from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactoForm

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class QuienesSomosPageView(TemplateView):

    template_name = "quienes_somos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def contacto(request):
    formContacto = ContactoForm()

    # Validar que el formulario tenga informacion

    if request.method == "POST":
        formContacto = ContactoForm(data=request.POST)
        if formContacto.is_valid():
            nombre = request.POST.get('Nombre', '')
            correo = request.POST.get('Correo', '')
            tipomsj = request.POST.get('TipoMsj', '')
            descripcion = request.POST.get('Descrip', '')

            # Enviar el mensaje o E-Mail

            return redirect(reverse('contacto')+"?ok")



    return render(request, 'contacto.html', {'formulario':formContacto})