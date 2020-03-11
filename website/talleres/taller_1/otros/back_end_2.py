# Script con los metodos de Back-End

from datetime import datetime



from taller_1.models import *

import random
import gzip
import pickle
from taller_1.models import  User_info, Artist, Homologacion_user, Homologacion_artist, Ratings

import numpy as np
import pandas as pd
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import train_test_split
from surprise import KNNBasic
from surprise import accuracy



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
		- 'artista' : Elemento de tipo Artist con el artista recomendado.
		- 'vecinos' : Lista de elementos tipo Models.User con los vecinos responsables de la recomendacion.
		- 'prediccion' : Float con el rating predecido que dice el modelo
	# TODO: back-end
	# Implementacion mock 
	'''
	def asignar_rating(id_user:int, id_artist:int, model):
		res = -1
		try:
			res = model.predict(id_user, id_artist).est
		except:
			res = -1
		return res

	# se carga el modelo
	f = gzip.open('/home/yacirramirez/Documents/MaestriaSistemas/SistemasDeRecomendacion/sistemas_de_recomendacion_2020/website/talleres/taller_1/otros/3.Model_User_User.pklz', 'rb')
	Model_UU = pickle.load(f)
	#result = Model_UU.predict(8, 2843)
	f.close()
	#result
	usuario = Homologacion_user.objects.get(user_id=id_usuario).new_user_id

	#artistas que el usuario ha escuchado
	artistas_escuchados = []
	for item in Ratings.objects.filter(user_id=id_usuario):
		artistas_escuchados.append([item.user_id,item.artist_name, item.artist_id])
	artistas_escuchados = pd.DataFrame(artistas_escuchados, columns=["user_id", "artist_name", "artist_id"])

	# artistas que el usuario no ha escuchado
	artistas = []
	for item in Homologacion_artist.objects.all():
		artistas.append([item.artist_name, item.new_artist_id])
	artistas = pd.DataFrame(artistas, columns = ["artist_name", "new_artist_id"])
	artistas_no_escuchado = artistas[np.invert(artistas["artist_name"].isin(artistas_escuchados["artist_name"].unique()))]
	artistas_no_escuchado["rating_predicho"] = artistas_no_escuchado["new_artist_id"].apply(lambda x : asignar_rating(usuario, x, Model_UU))
	artistas_recomendar = artistas_no_escuchado.sort_values(by="rating_predicho", ascending = False).head(num_recomendaciones)
	respuesta = []
	for index, row in artistas_recomendar.iterrows():
		art = Artist.objects.get(artist_name = row.artist_name)
		#art = Artist(artist_name = row.artist_name, artist_id = str(row.new_artist_id))
		respuesta.append({"artista" : art, "vecinos" : [], "prediccion" : row.rating_predicho})

	#for i in range(num_recomendaciones):
	#	artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
	#	global_rating = random.choice([1.2,2.3,3.5,4.1,5])

	#	artista = Artist(artist_name, global_rating = global_rating)

	#	vecinos = []
	#	for j in range(5):
	#		vecinos.append(User.objects.all()[random.randint(1,100)])

	#	prediccion = random.choice([1.2,2.3,3.5,4.1,5])

	#	respuesta.append({'artista' : artista, 'vecinos': vecinos, 'prediccion': prediccion})

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
		- 'artista' : Elemento de tipo Artist con el artista recomendado.
		- 'vecinos' : Lista de elementos tipo Artist con los vecinos responsables de la recomendacion.
		- 'prediccion' : Float con el rating predecido que dice el modelo
	# TODO: back-end
	# Implementacion mock 
	'''

	respuesta = []

	for i in range(num_recomendaciones):
		artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
		global_rating = random.choice([1.2,2.3,3.5,4.1,5])

		artista = Artist(artist_name, global_rating = global_rating)

		vecinos = []
		for j in range(5):
			artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
			global_rating = random.choice([1.2,2.3,3.5,4.1,5])

			vecinos.append(Artist(artist_name, global_rating = global_rating))

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
	usuario = Homologacion_user.objects.get(user_id=id_usuario).new_user_id

	# artistas que el usuario ha escuchado
	artistas_escuchados = []
	for item in Ratings.objects.filter(user_id=id_usuario):
		artistas_escuchados.append([item.user_id, item.artist_name, item.artist_id])
	artistas_escuchados = pd.DataFrame(artistas_escuchados, columns=["user_id", "artist_name", "artist_id"])

	# artistas que el usuario no ha escuchado
	artistas = []
	for item in Artist.objects.all():
		artistas.append([item.artist_name, item.artist_id, item.global_rating])
	artistas = pd.DataFrame(artistas, columns=["artist_name", "artist_id", "global_rating"])
	artistas_no_escuchado = artistas[np.invert(artistas["artist_name"].isin(artistas_escuchados["artist_name"].unique()))]
	artistas_no_escuchado = artistas_no_escuchado.head(num_artistas)
	respuesta = []
	for index, row in artistas_no_escuchado.iterrows():
		art = Artist.objects.get(artist_id=row.artist_id)
		respuesta.append(art)
	#respuesta = []
	#for i in range(top):

	#	artist_name = random.choice(['Justin Bieber','Selena Gomez','La Tigresa del Oriente','JBalvin', 'Blink-182','SUM 41','Green Day'])
	#	user_rating = random.choice([1.2,2.3,3.5,4.1,5])

	#	respuesta.append(Artist(artist_name, user_rating))

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