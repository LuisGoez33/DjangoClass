from django.contrib import admin

# Importamos las clases desde los modelos

from .models import Roles, DatosUser, HabilUser, DetaRoles, Rates

# Register your models here.

# Registro del modelo de roles
class RolesModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_link = ["RoleName"]
    list_filter = ["RoleName"]
    class Meta:
        model = Roles
admin.site.register(Roles)

# Registro del modelo de DatosUser
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nomUser"]
    list_display_link = ["nomUser"]
    list_filter = ["nomUser"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)

# Registro del modelo de HabilUser
class HabilUserModel(admin.ModelAdmin):
    list_display = ["nombHabil"]
    list_display_link = ["nombHabil"]
    list_filter = ["nombHabil"]
    class Meta:
        model = HabilUser
admin.site.register(HabilUser)

# Registro del modelo de DetaRoles
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUsuarios"]
    list_display_link = ["idUsuarios"]
    list_filter = ["idUsuarios"]
    class Meta:
        model = DetaRoles
admin.site.register(DetaRoles)

# Registro del modelo de Rates
class RatesModel(admin.ModelAdmin):
    list_display = ["idUsuarios"]
    list_display_link = ["idUsuarios"]
    list_filter = ["idUsuarios"]
    class Meta:
        model = Rates
admin.site.register(Rates)