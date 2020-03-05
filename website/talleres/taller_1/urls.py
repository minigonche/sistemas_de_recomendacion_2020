from django.urls import path

from . import views

app_name = 'taller_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('bienvenida/<str:id_usuario>/', views.bienvenida, name='bienvenida'),
    path('recomendaciones/<str:id_usuario>/', views.recomendaciones, name='recomendaciones'),
    path('mi_espacio/<str:id_usuario>/', views.mi_espacio, name='mi_espacio'),
    path('calificar/<str:id_usuario>/', views.calificar, name='calificar'),
    path('cold_start/<str:id_usuario>/', views.cold_start, name='cold_start')
    
]