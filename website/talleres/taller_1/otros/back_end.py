# Script con los metodos de Back-End
import random
import numpy as np
from taller_1.models import Reproduction, User_info, Ratings
from datetime import datetime




# Clases que el front end esta utilizando:

# Lo hice con clases para garantizar desacoplamiento entre el front y el back. Si en algun momento consideramos 
# que es mejor pasarlas como modelos, lo podemos hacer sin danhar el front.

class Reproduccion():
	'''
	Clase quue modela la reproduccion de una cancion por parte de un usuario.
	'''

	def __init__(self, user_id, song_name, artist_name, date):
		'''
		Inicializador de la clase.

		Parametros
		----------
		user_id : string
			Id del usuario

		song_name : string
			Nombre de la cancion
		
		artist_name : string
			El nombre del artista

		date: datetime
			Fecha en que fue resproducida la cancion
		'''

		self.user_id = user_id
		self.song_name = song_name
		self.artist_name = artist_name
		self.date = date



	def dar_fecha(self):

		fecha = 'No tiene'
		if self.date is not None:
			fecha = self.date.strftime('%Y-%m-%d')

		return(fecha)

	def to_dict(self):
		'''
		Vuelve la clase un diccionario
		'''

		resp = {}
		resp['user_id'] = self.user_id
		resp['song_name'] = self.song_name
		resp['artist_name'] = self.artist_name
		resp['date'] = self.dar_fecha()

class Artista():
	'''
	Clase que modela un artista (con un rating asociado)
	'''

	def __init__(self, artist_name, user_rating = -1, global_rating = -1):

		self.artist_name = artist_name
		self.user_rating = user_rating
		self.global_rating = global_rating
		





## ---------------------------------------
# Metodos

def dar_ultimas_reproducciones(id_usuario, top = 5):
	'''
	Metodo que devuelve las ultimas reproducciones del usuario

	Parametros
	----------
	id_usuario : string
		El id del usuario
	top : int > 0
		La cantidad de reproducciones a incluir.

	Devuelve
	---------
	list of Reproduccion
		Lista con elementos de tipo: Reproduccion, ordenadas de mas reciente a menos reciente.
		En caso de solicitar mas reproducciones de las que existen, devuelve las que haya. Si el usuario no tiene reproducciones o si no existe,
		debe devolver una lista vacia.

	'''

	# TODO: back-end
	ultimas_reproducciones = list(Reproduction.objects.all().filter(user_id = id_usuario))
	print("tamaño respuesta:", len(ultimas_reproducciones))
	res = []
	for i in ultimas_reproducciones:
		res.append(Reproduccion(i.user_id,i.song_name,i.artist_name,i.date))


	# Implementacion mock

	#respuesta = []
	#for i in range(top):

	#	user_id = 'usuario_prueba'
	#	song_name = random.choice(['Heroe','Un Monton de Estrellas','Eye of the Tiger','Cuando tenga la Tierra'])
	#	artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','J Balvin'])
	#	date = datetime.now()

	#	respuesta.append(Reproduccion(user_id, song_name, artist_name, date))

	return(res)




def dar_numero_de_artistas(id_usuario):
	'''
	Metodo que devuelve el numero de artistas que ha oido un usuario

	Parametros
	----------
	id_usuario : string
		El id del usuario

	Devuelve
	---------
	int
		El numero de artistas que ha oido el usuario. Si este no existe, debe devolver 0.
	'''
	# TODO: back-end

	# Implementacion mock
	return(User_info.objects.all().get(user_id=id_usuario).numero_artistas)




def dar_numero_de_reproducciones(id_usuario):
	'''
	Metodo que devuelve el numero de reproducciones que ha oido un usuario

	Parametros
	----------
	id_usuario : string
		El id del usuario

	Devuelve
	---------
	int
		El numero de reproducciones que ha oido el usuario. Si este no existe, debe devolver 0.
	'''
	# TODO: back-end

	# Implementacion mock
	return(User_info.objects.all().get(user_id=id_usuario).numero_reproducciones)



def dar_artistas_favoritos(id_usuario, top = 5):
	'''
	Metodo que devuelve los artistas favoritos de un usuario. Cada Artista debe ser inicializado con el 
	user_rating del usuario reecibido como parametro.

	Parametros
	----------
	id_usuario : string
		El id del usuario
	top : int > 0
		La cantidad de artsitas a incluir.

	Devuelve
	---------
	list of Artista
		Lista con elementos de tipo: Artista, ordenados de mejor user_rating a peor user_rating.
		Si el usuario no tiene reproducciones o si no existe, debe devolver una lista vacia.

	'''

	# TODO: back-end [:30]
	usuario_ratings = Ratings.objects.filter(user_id=id_usuario).order_by('-rating_lineal')
	res = []
	if len(usuario_ratings)<5:
		for i in usuario_ratings:
			res.append(Artista(i.artist_name, i.rating_lineal))
	else:
		for i in usuario_ratings[:5]:
			res.append(Artista(i.artist_name, i.rating_lineal))
	return(res)



def dar_artistas_menos_favoritos(id_usuario, top = 5):
	'''
	Metodo que devuelve los artistas menos favoritos de un usuario. Cada Artista debe ser inicializado con el 
	user_rating del usuario reecibido como parametro.

	Parametros
	----------
	id_usuario : string
		El id del usuario
	top : int > 0
		La cantidad de artsitas a incluir.

	Devuelve
	---------
	list of Artista
		Lista con elementos de tipo: Artista, ordenados de peor user_rating a mejor user_rating.
		Si el usuario no tiene reproducciones o si no existe, debe devolver una lista vacia.

	'''

	# TODO: back-end

	usuario_ratings = Ratings.objects.filter(user_id=id_usuario).order_by('rating_lineal')
	res = []
	if len(usuario_ratings) < 5:
		for i in usuario_ratings:
			res.append(Artista(i.artist_name, i.rating_lineal))
	else:
		for i in usuario_ratings[:5]:
			res.append(Artista(i.artist_name, i.rating_lineal))
	return (res)