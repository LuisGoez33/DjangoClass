from django import forms
from .tipomsj import TipoMsj

# Creamos las clases con los formularios pertinentes:

class ContactoForm(forms.Form):

    # Atributos del formulario de contacto:
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su Nombre Completo'}))
    correo = forms.EmailField(label="Correo electrónico", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese tu Correo Electronico'}))
    tipomsj = forms.ChoiceField(label="Tipo de peticion", required=True, choices=TipoMsj, widget=forms.Select(attrs={'class':'form-control'}))
    descripcion = forms.CharField(label="Descripción", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Escribe tu Mensaje'}))