from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inici, name='inici'),
    path('nosaltres', views.nosaltres, name='nosaltres'),
    path('llibres', views.llibres, name='llibres'),
    path('llibres/crear', views.crear_llibre, name='crear'),
    path('llibres/editar', views.editar_llibre, name='editar'),
]
