from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from taller_1.models import User

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
	id_ususario = request.POST.get('id_ususario_registrado')
	pwd = request.POST.get('pwd_ususario_registrado')

	# Busca el usuario
	try:
		user = User.objects.get(user_id=id_ususario)

		# Revisa la contrasenha
		if user.password == pwd:
			return(HttpResponse(str(user)))
		else:
			return HttpResponse('Contrasenha equivocada')

	except:
		return HttpResponse('Usuario: {} si que no existe'.format(id_ususario))


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


