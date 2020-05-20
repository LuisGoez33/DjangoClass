from django.contrib import admin

# Importamos las clases desde los modelos

from .models import TipoDocu, CategProye, Proyectos, Documentos

# Register your models here.

# Registro del modelo de TipoDocu
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NomTiDoc"]
    list_display_link = ["NomTiDoc"]
    list_filter = ["NomTiDoc"]
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)

# Registro del modelo de CategProye
class CategProyeModel(admin.ModelAdmin):
    list_display = ["Lenguaje"]
    list_display_link = ["Lenguaje"]
    list_filter = ["Lenguaje"]
    class Meta:
        model = CategProye
admin.site.register(CategProye)

# Registro del modelo de Proyectos
class ProyectosModel(admin.ModelAdmin):
    list_display = ["NombProy"]
    list_display_link = ["NombProy"]
    list_filter = ["NombProy"]
    class Meta:
        model = Proyectos
admin.site.register(Proyectos)

# Registro del modelo de Documentos
class DocumentosModel(admin.ModelAdmin):
    list_display = ["NombDocu"]
    list_display_link = ["NombDocu"]
    list_filter = ["NombDocu"]
    class Meta:
        model = Documentos
admin.site.register(Documentos)