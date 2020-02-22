from django.urls import path

from . import views

app_name = 'taller_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('bienvenida/<str:id_usuario>/', views.bienvenida, name='bienvenida'),
    path('mi_espacio/<str:id_usuario>/', views.mi_espacio, name='mi_espacio')
    
]