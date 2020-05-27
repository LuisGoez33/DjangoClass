from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
# Crear la estructura de la aplicacion en el modelo de datos

class Roles(models.Model):
    RoleName = models.CharField(max_length = 50, verbose_name = "Nombre del Rol")

    # Clase Meta

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"

    # Creo la funcion para llamar atributos:
    def __str__(self):
        return self.RoleName

class DatosUser(models.Model):
    usuarioId = models.CharField(max_length = 35, verbose_name = "Identificacion")
    nomUser = models.CharField(max_length = 256, null = "True", verbose_name = "Nombres")
    apeUser = models.CharField(max_length = 256, null = "True", verbose_name = "Apellidos")
    profeUser = models.CharField(max_length = 100, null = "True", verbose_name = "Profesion")
    FotoUser = models.ImageField(default = 'user.png', verbose_name = "Foto de perfil", upload_to = "img/perfiles")
    TeleUser = models.CharField(max_length = 45, verbose_name = "Numero de Teléfono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = "Otro", verbose_name = "Género")
    addData = models.DateTimeField(auto_now_add = True, null = "True", verbose_name = "Creado el")
    UpdAddData = models.DateTimeField(auto_now = True, null = "True", verbose_name = "Modificado el")

    # Clase Meta

    class Meta:
         verbose_name = "Datos de Usuario"
         verbose_name_plural = "Informacion"

    # Funcion
    def __str__(self):
        return self.nomUser

class HabilUser(models.Model):
    nombHabil = models.CharField(max_length = 155, verbose_name = "Nombre de la Habilidad")
    DescHabil = models.TextField(default = "Desarrollador...", verbose_name = "Descripcion de la habilidad")

    # Clase Meta

    class Meta:
        verbose_name = "Habilidades del usuario"
        verbose_name_plural = "Competencias"

    # Funcion
    def __str__(self):
        return self.nombHabil

# Modelos de detalle

class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Id del Rol")
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Id del Usuario")
    Agregado = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Agregado el")
    udtAgregado = models.DateTimeField(auto_now = True, verbose_name = "Modificado el")
    EstaRol = models.CharField(max_length = 45, verbose_name = "Estado del Rol")

    # Clase Meta

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"

    # Funcion de mostrar

    def __unicode__(self):
        return self.idUsuarios

class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE, verbose_name = "Id de la Habilidad")
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Id del Usuario")
    PrcHabil = models.DecimalField(max_digits = 2, decimal_places = 1, verbose_name = "Porcentaje de la Habilidad") # 99,9
    udtHabil = models.DateTimeField(auto_now = True, verbose_name = "Actualizacion del Porcentaje")

    # Clase Meta

    class Meta:
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuarios"

    # Funcion

    def __unicode__(self):
        return self.idUsuarios