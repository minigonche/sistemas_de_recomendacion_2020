from django.shortcuts import render
from django.http import HttpResponse



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

	return HttpResponse("Login Usuario \n Id: {}, pwd: {}".format(id_ususario,pwd))


def crear_usuario(request):
	'''
	Metodo para crear un nuevo usuario.

	Debe verificar que no existe el id del susuario solicitado.

	TODO: Verificar que no existe el ususario actual y crearlo.
	'''

	# Extrae los datos
	id_ususario = request.POST.get('id_ususario_nuevo')
	pwd = request.POST.get('pwd_ususario_nuevo')
	edad = request.POST.get('edad')
	sexo = request.POST.get('sexo')

	return HttpResponse("Login Usuario Viejo. Id: {}, pwd: {}, edad: {}, sexo: {}".format(id_ususario,pwd, edad, sexo))