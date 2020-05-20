from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser

# Create your models here.
# Crear la estructura de la aplicacion en el modelo de datos

class TipoDocu(models.Model):
    NomTiDoc = models.CharField(max_length = 45, verbose_name = "Nombre Tipo Documentacion")

    # Clase Meta

    class Meta:
        verbose_name = "Tipo de Documuentos"
        verbose_name_plural = "Documentos"
    
    # Funcion mostrar

    def __str__(self):
        return self.NomTiDoc

class CategProye(models.Model):
    Lenguaje = models.CharField(max_length = 45, verbose_name = "Lenguaje de Programacion")
    MotorDB = models.CharField(max_length = 155, verbose_name = "Motor Base de Datos")
    Arquitecura = models.CharField(max_length = 255, verbose_name = "Arquitectura")

    # Clase Meta

    class Meta:
        verbose_name = "Categoria del Proyecto"
        verbose_name_plural = "Categorias"
    
    # Funcion mostrar

    def __str__(self):
        return self.Lenguaje

class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE, verbose_name = "Id de la Categoria")
    NombProy = models.CharField(max_length = 255, verbose_name = "Nombre del Proyecto")
    DescProy = models.TextField(default = "Programa de desarrollo de Software", verbose_name = "Descripcion del proyecto")
    ImgProye = models.ImageField(default = 'proyecto.png', verbose_name = "Foto del proyecto", upload_to = "proyectos/img")
    FechaIni = models.DateTimeField(auto_now_add = True, null = "True", verbose_name = "Inicio el")
    FechaFin = models.DateTimeField(auto_now_add= True, null = "True", verbose_name = "Finalizo el")
    UrlRepo = models.TextField(default = "No tiene repositorio en GitHub", verbose_name = "Url del Repositorio en GitHub")
    EstaProy = models.CharField(max_length = 45, verbose_name = "Estado del Proyecto")

    # Clase meta

    class Meta:
        verbose_name = "Datos del proyecto"
        verbose_name_plural = "Informacion de los Proyectos"

    # Funcion mostrar

    def __str__(self):
        return self.NombProy

class Documentos(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name = "Id Tipo Documento")
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE, verbose_name = "Id del Proyecto")
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Id del Usuario")
    NombDocu = models.CharField(max_length = 255, verbose_name = "Nombre del Documento")
    PathDocu = models.CharField(max_length = 45, verbose_name = "Ruta de almacenamiento del Documento")

    # Clase meta

    class Meta:
        verbose_name = "Datos del Documento"
        verbose_name_plural = "Informacion de los Documentos"

    # Funcion mostrar

    def __str__(self):
        return self.NombDocu