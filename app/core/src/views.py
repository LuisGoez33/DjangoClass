from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactoForm
from django.core.mail import EmailMessage

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
            nombre = request.POST.get('nombre', '')
            correo = request.POST.get('correo', '')
            tipomsj = request.POST.get('tipomsj', '')
            descripcion = request.POST.get('descripcion', '')

            # Creamos el objeto con las variables del formulario:
            email = EmailMessage(
                "UpLine: Tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nTipo de mensaje:\n{}\n\nEscribió:\n\n{}".format(nombre, correo, tipomsj, descripcion),
                "no-contestar@inbox.mailtrap.io",
                ["lpgoez7@misena.edu.co"],
                reply_to=[correo]
            )

            # Enviamos el email

            try:
                email.send()
                # Se envio el correo
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se envio el correo
                return redirect(reverse('contacto')+"?fail")

    return render(request, 'contacto.html', {'formulario': formContacto})
