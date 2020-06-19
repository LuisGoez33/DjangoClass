from django.urls import path
from . import views

urlpatterns = [
  
  path('quienes_somos/', views.QuienesSomosPageView.as_view(), name = 'quienes_somos'),

]