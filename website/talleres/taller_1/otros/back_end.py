# Script con los metodos de Back-End

from datetime import datetime

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

	# Implementacion mock

	respuesta = []
	for i in range(top):

		user_id = 'usuario_prueba'
		song_name = random.choice(['Heroe','Un Monton de Estrellas','Eye of the Tiger','Cuando tenga la Tierra'])
		artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','J Balvin'])
		date = datetime.now()

		respuesta.append(Reproduccion(user_id, song_name, artist_name, date))

	return(respuesta)		




