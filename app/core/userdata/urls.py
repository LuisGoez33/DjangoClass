from django.urls import path
from . import views
from .views import IndexListView

urlpatterns = [
  
  path('quienes_somos/', views.QuienesSomosPageView.as_view(), name = 'quienes_somos'),

]