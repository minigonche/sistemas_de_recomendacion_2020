from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from taller_1.models import User


# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Otros
import taller_1.otros.back_end as back_end

import sys

def index(request):
	'''
	Metodo de bienvenida
	'''

	context = {}
	return render(request, 'taller_1/index.html', context)




def iniciar_sesion(request):
	'''
	Metodo para crear una nueva sesion. 
	Debe verificar el ususario y la contrasenha

	TODO: Verificar usuario existente y contrasenha correcta
	'''

	# Extrae los datos
	id_usuario = request.POST.get('id_ususario_registrado')
	pwd = request.POST.get('pwd_ususario_registrado')

	# For testing
	if id_usuario is None:
		id_usuario = 'minigonche'
		pwd = 'minigonche'

	# Busca el usuario
	try:
		user = User.objects.get(user_id=id_usuario)

		# Revisa la contrasenha
		if user.password == pwd:
			
			# Visualiza el usuario
			# Caracteristicas del ususario
			context = {}
			context['user_id'] = id_usuario
			context['fecha'] = user.dar_fecha()
			context['edad'] = user.dar_edad()
			context['pais'] = user.dar_pais()
			context['sexo'] = user.dar_sexo()


			# Las ultimas reproducciones
			#context['reproducciones'] = [rep.to_dict() for rep in back_end.dar_ultimas_reproducciones(id_usuario, top = 5)]
			context['reproducciones'] = back_end.dar_ultimas_reproducciones(id_usuario, top = 5)

			return render(request, 'taller_1/user_view.html', context)

		else:
			return HttpResponse('Contrasenha equivocada')

	except ObjectDoesNotExist:
		return HttpResponse('No Existe')



def crear_usuario(request):
	'''
	Metodo para crear un nuevo usuario.

	Debe verificar que no existe el id del susuario solicitado.

	TODO: Verificar que no existe el ususario actual y crearlo.
	'''

	# Extrae los datos
	id_ususario = request.POST.get('id_ususario_nuevo')
	pwd = request.POST.get('pwd_ususario_nuevo')
	
	sexo = request.POST.get('sexo')

	if sexo == 'Hombre':
		sexo = True
	elif sexo == 'Mujer':
		sexo = False
	else:
		sexo = None

	edad = request.POST.get('edad')
	try:
		edad = int(edad)
	except:
		edad = 0


	pais = request.POST.get('pais')
	fecha_registro = datetime.now()

	# Mira si el usuario ya existe
	try:
		user = User.objects.get(user_id=id_ususario)
		return HttpResponse('Usuario: {} ya existe'.format(id_ususario))
	except:

		user = User(user_id= id_ususario, 
				    password= pwd,
				    date_join= fecha_registro,
				    age= edad,
				    sex= sexo,
				    country= pais)

		user.save()

		return HttpResponse(str(user))


