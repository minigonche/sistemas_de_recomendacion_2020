from django.urls import path

from . import views

app_name = 'taller_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    
]