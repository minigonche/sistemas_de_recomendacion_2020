from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Otros
import taller_2.otros.modelo_ponderado as modelo

import sys

def index(request):
	'''
	Metodo de bienvenida
	'''

	context = {}
	return render(request, 'taller_2/index.html', context)


def entrada(request):
	'''
	Metodo de bienvenida
	'''

	context = {}
	return render(request, 'taller_2/entrada.html', context)


def recomendaciones(request, id_usuario):
	'''
	Metodo que devuelve el espacio del usuario

	'''

	# Extraer Lugar
	lugar = 'NV'

	context = {}


	context['lugares'] = modelo.dar_recomendaciones(lugar, id_usuario, top = 10)

	return render(request, 'taller_2/recomendaciones.html', context)