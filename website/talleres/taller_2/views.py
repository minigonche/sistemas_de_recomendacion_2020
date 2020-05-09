from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Otros
import taller_2.otros.modelo_ponderado as modelo
import taller_2.otros.modelo_contenido as modelo_contenido
import taller_2.otros.back_end as be

import sys

def index(request):
	'''
	Metodo de Inicio
	'''


	context = {}
	return render(request, 'taller_2/index.html', context)


def entrada(request):
	'''
	Metodo de bienvenida
	'''

	id_usuario = request.POST.get('id_usuario')

	print()
	print(id_usuario)

	es_numerico = False

	# Mira si es numerico
	try:
		numero = int(id_usuario)
		es_numerico = True
	except:
		pass

	if es_numerico:
		id_usuario = modelo_contenido.dar_id_usuario_por_numero(int(id_usuario))



	usuario = be.dar_usuario(id_usuario)

	context = {}
	# Usuario
	context['user'] = usuario

	# resenhas
	resenhas = be.dar_ultimas_resenhas_usuario(id_usuario)
	context['resenhas'] = resenhas

	for res in resenhas:
		neg = be.dar_negocio(res.business_id)
		res.nombre = neg.name
		res.lugar = neg.state

	return render(request, 'taller_2/entrada.html', context)


def recomendaciones(request, id_usuario):
	'''
	Metodo que devuelve el espacio del usuario

	'''

	alpha = request.POST.get('alpha')
	lugar = request.POST.get('select_lugar')

	print(lugar)
	

	if alpha is None:
		alpha = 0.58

	if lugar is None:
		lugar = 'PA'

	
	

	context = {}
	context['alpha'] = alpha
	context['lugar'] = lugar
	context['id_usuario'] = id_usuario

	context['negocios'] = modelo.dar_recomendaciones(lugar, id_usuario, alpha, top = 10)

	

	return render(request, 'taller_2/recomendaciones.html', context)