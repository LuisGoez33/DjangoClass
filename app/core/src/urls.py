from django.urls import path
from . import views

urlpatterns = [
  
  path('', views.HomePageView.as_view(), name = 'index'),
  path('contacto/', views.contacto, name = 'contacto'),
  path('diccionario_datos/', views.DiccionarioDatosPageView.as_view(), name = 'diccionario_datos'),
  path('esquema/', views.EsquemaPageView.as_view(), name = 'esquema')

]