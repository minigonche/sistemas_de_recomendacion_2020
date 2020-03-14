from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from taller_1.models import User, Homologacion_user, User_info


# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Otros
import taller_1.otros.back_end as back_end
import taller_1.otros.back_end_2 as back_end_2
import taller_1.otros.image_finder as image_finder


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

			# Lleva a la pagina de bienvenida
			return(bienvenida(request, id_usuario))

		else:
			return HttpResponse('Contrasenha equivocada')

	except ObjectDoesNotExist:
		usuario_no_existe()



def crear_usuario(request):
	'''
	Metodo para crear un nuevo usuario.

	Debe verificar que no existe el id del susuario solicitado.

	TODO: Verificar que no existe el ususario actual y crearlo.
	'''

	# Extrae los datos
	id_usuario = request.POST.get('id_ususario_nuevo')
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
		user = User.objects.get(user_id=id_usuario)
		return HttpResponse('Usuario: {} ya existe'.format(id_usuario))
	except ObjectDoesNotExist:

		id_pos = len(User.objects.all())
		user = User(user_id= id_usuario, 
				    password= pwd,
				    date_join= fecha_registro,
				    age= edad,
				    sex= sexo,
				    country= pais)

		user.save()

		# Homologacion
		homo = Homologacion_user(user_id = id_usuario,
						  new_user_id = id_pos)

		homo.save()

		user_info = User_info(user_id = id_usuario, numero_artistas = 0, numero_reproducciones = 0)
		user_info.save()



	# Lleva a la pagina de bienvenida
	return(cold_start(request, id_usuario))




def bienvenida(request, id_usuario):
	'''
	Metodo que devuelve la bienvenida del usuario

	'''

	try:
		user = User.objects.get(user_id=id_usuario)

		# Visualiza el usuario
		# Caracteristicas del ususario
		context = {}
		context['user_id'] = id_usuario
		context['fecha'] = user.dar_fecha()
		context['edad'] = user.dar_edad()
		context['pais'] = user.dar_pais()
		context['sexo'] = user.dar_sexo()


		# Las ultimas reproducciones
		context['reproducciones'] = back_end.dar_ultimas_reproducciones(id_usuario, top = 5)

		return render(request, 'taller_1/user_view.html', context)


	except ObjectDoesNotExist:
		return(usuario_no_existe())



	
def mi_espacio(request, id_usuario):
	'''
	Metodo que devuelve el espacio del usuario

	'''

	# Visualiza el usuario
	context = {'user_id' : id_usuario}

	# ZOna de resumen

	context['num_reproducciones'] = back_end.dar_numero_de_reproducciones(id_usuario)
	context['num_artistas'] = back_end.dar_numero_de_artistas(id_usuario)


	# Favoritos
	context['favoritos'] = back_end.dar_artistas_favoritos(id_usuario, top = 5)

	for fav in context['favoritos']:
		fav.link_foto = image_finder.get_image(fav.artist_name)

	# Favoritos
	context['menos_favoritos'] = back_end.dar_artistas_menos_favoritos(id_usuario, top = 5)

	for fav in context['menos_favoritos']:
		fav.link_foto = image_finder.get_image(fav.artist_name)


	return render(request, 'taller_1/my_space.html', context)


def usuario_no_existe():
	'''
	TODO: Devilver pagina donde usuario no existe
	'''
	return HttpResponse('No Existe')





def recomendaciones(request, id_usuario):
	'''
	Metodo que devuelve el espacio del usuario

	'''

	# Visualiza el usuario
	context = {'user_id' : id_usuario}

	usuario_esta = back_end_2.esta_en_el_modelo(id_usuario)
	context['esta'] = usuario_esta

	if usuario_esta:

		# Por usuario
		context['recomendaciones_usuario'] = back_end_2.dar_recomendaciones_por_usuario(id_usuario)

		for d in context['recomendaciones_usuario']:
			d['primero'] = False
			d['artista'].link_foto = image_finder.get_image(d['artista'].artist_name)

		context['recomendaciones_usuario'][0]['primero'] = True

		# Por Item
		#context['recomendaciones_item'] = back_end_2.dar_recomendaciones_por_item(id_usuario)

		#for d in context['recomendaciones_item']:
		#	d['primero'] = False
		#	for art in d['vecinos']:
		#		art.link_foto = image_finder.get_image(art.artist_name)
		#		
		#	d['artista'].link_foto = image_finder.get_image(d['artista'].artist_name)

		#context['recomendaciones_item'][0]['primero'] = True

	return render(request, 'taller_1/recomendaciones.html', context)

def cold_start(request, id_usuario):
	'''
	Metodo para el cold start de un usuario
	'''

	context = {'user_id' : id_usuario}

	# Extrae los que no ha calificado

	todos = back_end_2.dar_artistas_aleatorios(id_usuario, num_artistas = 8)
	# Favoritos
	context['por_calificar_1'] = todos[0:4]

	for fav in context['por_calificar_1']:
		fav.link_foto = image_finder.get_image(fav.artist_name)

	context['por_calificar_2'] = todos[4:8]

	for fav in context['por_calificar_2']:
		fav.link_foto = image_finder.get_image(fav.artist_name)

	return render(request, 'taller_1/cold_start.html', context)




def calificar(request, id_usuario):
	'''
	Metodo que devuelve el espacio del usuario

	'''

	# Visualiza el usuario
	context = {'user_id' : id_usuario}
	resp = ''
	for key, value in request.POST.items():
		if key.startswith('artist_id:'):
			artist_id = key[len('artist_id:'):]
			rating = int(value)

			if rating > 0:
				back_end_2.calificar_item(id_usuario, artist_id, rating)

	
	if request.method == 'POST':
	    if request.POST.get("mas"):
	    	# Otra vez cold start
	    	return(cold_start(request, id_usuario))
	        

	    elif request.POST.get("inicio"):  
	    	# Va al inicio
	        return(bienvenida(request, id_usuario))

	    elif request.POST.get("recomendaciones"):  
	    	# Va al inicio
	        return(recomendaciones(request, id_usuario))

	    else:
	    	raise ValueError('Boton seleccionado no es reconocido')

	