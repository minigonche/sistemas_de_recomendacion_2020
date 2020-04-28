from django.urls import path

from . import views

app_name = 'taller_2'

urlpatterns = [
    path('', views.index, name='index'),
    path('bienvenido', views.entrada, name='entrada'),
    path('recomendaciones/<str:id_usuario>/', views.recomendaciones, name='recomendaciones'),
]
