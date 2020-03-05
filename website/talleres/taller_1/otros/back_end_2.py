# Script con los metodos de Back-End

from datetime import datetime



from taller_1.models import User

import random

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

		self.artist_id = random.randint(0,100)
		self.artist_name = artist_name
		self.user_rating = user_rating
		self.global_rating = global_rating
		





## ---------------------------------------
# Metodos

def dar_recomendaciones_por_usuario(id_usuario, num_recomendaciones = 5):
	'''
	Metodo que utiliza el modelo usuario usuario para dar recomendaciones. La idea de este metodo es que devuelva
	los artistas recomendados y los nombres de los usuarios que se utilizaron para predecir cada uno de los elementos.


	Parametros
	----------
	id_usuario : string
		El id del usuario
	num_recomendaciones : int > 0
		El numero de recomendaciones que se quiere

	Devuelve
	---------
	list of Dictionarios
		Una lista de diccionarios, donde cada diccionario debe tener la siguiente estructura:
		- 'artista' : Elemento de tipo Artista con el artista recomendado.
		- 'vecinos' : Lista de elementos tipo Models.User con los vecinos responsables de la recomendacion.
		- 'prediccion' : Float con el rating predecido que dice el modelo


	# TODO: back-end

	# Implementacion mock 
	'''

	respuesta = []

	for i in range(num_recomendaciones):
		artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
		global_rating = random.choice([1.2,2.3,3.5,4.1,5])

		artista = Artista(artist_name, global_rating = global_rating)

		vecinos = []
		for j in range(5):
			vecinos.append(User.objects.all()[random.randint(1,100)])

		prediccion = random.choice([1.2,2.3,3.5,4.1,5])

		respuesta.append({'artista' : artista, 'vecinos': vecinos, 'prediccion': prediccion})

	return(respuesta)




def dar_recomendaciones_por_item(id_usuario, num_recomendaciones = 5):
	'''
	Metodo que utiliza el modelo item para dar recomendaciones. La idea de este metodo es que devuelva
	los artistas recomendados y los nombres de los artistas similares que se utilizaron para predecir cada uno de los elementos.


	Parametros
	----------
	id_usuario : string
		El id del usuario
	num_recomendaciones : int > 0
		El numero de recomendaciones que se quiere

	Devuelve
	---------
	list of Dictionarios
		Una lista de diccionarios, donde cada diccionario debe tener la siguiente estructura:
		- 'artista' : Elemento de tipo Artista con el artista recomendado.
		- 'vecinos' : Lista de elementos tipo Artista con los vecinos responsables de la recomendacion.
		- 'prediccion' : Float con el rating predecido que dice el modelo


	# TODO: back-end

	# Implementacion mock 
	'''

	respuesta = []

	for i in range(num_recomendaciones):
		artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
		global_rating = random.choice([1.2,2.3,3.5,4.1,5])

		artista = Artista(artist_name, global_rating = global_rating)

		vecinos = []
		for j in range(5):
			artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
			global_rating = random.choice([1.2,2.3,3.5,4.1,5])

			vecinos.append(Artista(artist_name, global_rating = global_rating))

		prediccion = random.choice([1.2,2.3,3.5,4.1,5])

		respuesta.append({'artista' : artista, 'vecinos': vecinos, 'prediccion': prediccion})

	return(respuesta)


def dar_artistas_aleatorios(id_usuario, num_artistas = 10):
	'''
	Metodo que devuelve un numero de artistas aleatorio (sin repetecion!), que el usuario no haya calificado. Esto se utilizara para el cold start
	
	Parametros
	----------
	id_usuario : string
		El id del usuario
	num_artistas : int > 0
		El numero de artistas que se quiere

	Devuelve
	---------
	list of Artsita
		Lista de elementos de tipo artista


	# TODO: back-end

	# Implementacion mock 
	'''


	respuesta = []
	for i in range(num_artistas):

		artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
		user_rating = random.choice([1.2,2.3,3.5,4.1,5])
		art = Artista(artist_name, user_rating)
		art.artist_id = i
		respuesta.append(art)

	return(respuesta)



def calificar_item(id_usuario, id_item, calificacion):
	'''
	Metodo que asigna una calificacion a un item
	
	Parametros
	----------
	id_usuario : string
		El id del usuario
	id_item : string
		El id del artista
	calificacion : float
		Calificacion que se le quiere asignar. De 1 a 5



	# TODO: back-end

	# Implementacion mock 
	'''


	pass