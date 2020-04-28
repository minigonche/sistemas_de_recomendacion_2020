# Script Modelo Por Contexto
# Scripts para el modelo por contenido


import json
import os
import pandas as pd
import numpy as np



todos_lugares = set(['OTHER', 'NC', 'AZ', 'QC', 'NV', 'IL', 'ON', 'AB', 'PA', 'WI', 'SC', 'OH'])

ubication_datos = ''



def se_tiene_soporte_lugar(lugar):
	'''
	Revisa si se tiene soporte para el lugar recibido
	'''
	if lugar not in todos_lugares:
		raise ValueError('No hay soporte para el lugar: {}'.format(lugar))
    

def dar_grupo_usuario(s , num_modules = 20):
	'''
	Da el Grupo del ususario
	'''
	return(abs(ord(s[0]) + ord(s[1]) + ord(s[-1])) % (num_modules))

def dar_negocios_calificados(usuario):
	'''
	Da los negocios calificados por un usuario
	'''
	g = dar_grupo_usuario(usuario)
	df_rev = pd.read_pickle(ubication_datos + 'data/summary_user_ratings/ratings_{}.zip'.format(g))

	return(df_rev[df_rev.user_id == usuario].copy())

def dar_perfil_usuario(usuario):

	# Extrae el grupo
	g = dar_grupo_usuario(usuario)

	df = pd.read_pickle(ubication_datos + 'data/user_content_profiles/group_{}.zip'.format(g))

	if usuario not in df.index:
		return({})

	pro = df.profile[usuario].replace("'",'"')
	
	return(json.loads(pro))



def dar_recomendaciones_por_popular(lugar, usuario, top = 50, df_visitados = None):
	'''
	Metodo que devuelve los sitios mas populares de un lugar 
	'''

	se_tiene_soporte_lugar(lugar)


	# Extracts the visited sites
	if df_visitados is None:
		df_visitados = dar_negocios_calificados(usuario)

	# Extracts all sites
	df_neg = pd.read_pickle(ubication_datos + 'data/avg_business_ratings/avg_ratings.zip')

	# Filters
	df_neg = df_neg[df_neg.state == lugar]
	df_neg = df_neg[~df_neg.business_id.isin(set(df_visitados.business_id.values))]

	if df_neg.shape[0] == 0:
		raise ValueError('El usuario: {} ya visito todos los lugares en: {}'.format(usuario, lugar))

	return(df_neg.iloc[0:(min(top, df_neg.shape[0]))])
            
    

def dar_recomendaciones(lugar, usuario, top = 50):
	'''
	Metodo que devuelve el numero de lugares solicitado de ids de lugares, ordenados de mejor a peor.

	El metodo devuelve un codigo indicando lo sucedido. Asi son los codigos:
		- OK: Todo en orden
		- NULL_INTER: no hay interseccion entre las categorias del lugar y los del usuario. Devuelve los lugares mas populares que no haya visitado.
		- NO_RATINGS: el usuario no tiene perfil de categorias. Devuelve los lugares mas populares del sitio
	Returns
	--------
	Devuelve lo siguiente
		- array string: una lista con los ids de los lugares
		- array float: una lista con las calificaciones correpsondientes
		- string: codigo indicando lo que sicedio
		- string: explicacion

	'''

	# Extracts the profile
	per = dar_perfil_usuario(usuario)
	if len(per) == 0:

		df_bus = dar_recomendaciones_por_popular(lugar, usuario, top = top, df_visitados = df_visitados)
		return(df_bus.busines_id.values, df_bus.avg_rating.values, 'NO_RATINGS', 'El usuario no tiene perfil de categorias. Devuelve los lugares mas populares del sitio')

	# Extracts the visited sites
	df_visitados = dar_negocios_calificados(usuario)

	# Construct DF
	vec = pd.DataFrame.from_dict(per, orient = 'index').rename(columns = {0 : 'val'})
	user_cat = vec.index

	# Extracts the State matrix
	matrix_location = ubication_datos + 'data/content_models_by_state/{}.zip'.format(lugar)
	if not os.path.exists(matrix_location):
		raise ValueError('No se encontro el lugar: {} '.format(lugar))

	# Reads the matrix
	matrix = pd.read_pickle(matrix_location)
	# Extracts the categories
	state_cat = matrix.columns

	final_cat = state_cat.intersection(user_cat)

	if len(final_cat) == 0:
		df_bus = dar_recomendaciones_por_popular(lugar, usuario, top = top, df_visitados = df_visitados)

		return(df_bus.busines_id.values, df_bus.avg_rating.values, 'NULL_INTER', 'No hay interseccion entre las categorias del lugar y los del usuario. Devuelve los lugares mas populares que no haya visitado.')

	#Filters out
	# Vector
	final_vec = vec.loc[final_cat]

	# Matrix
	# Categories
	final_matrix = matrix[final_cat]

	# Drops Zeros
	final_matrix = final_matrix[final_matrix.sum(axis = 1) > 0]
	# Drops Visited
	final_matrix = final_matrix.loc[final_matrix.index.difference(set(df_visitados.business_id.values))]


	# Does IDF
	features = final_matrix.sum()
	idf = np.log2(final_matrix.shape[0]/features)
	final_matrix = final_matrix.multiply(idf, axis=1)

	# lengths
	vev_l = np.sqrt((final_vec**2).sum()).values
	m_l = np.sqrt((final_matrix**2).sum(axis = 1))

	# Cosine similarity (all are positive)
	final_df = final_matrix.dot(final_vec)
	final_df['val'] = final_df.val / ((vev_l*m_l))

	# Final list
	final_df = final_df.sort_values('val', ascending = False)*5

	# Excludes
	final_df = final_df.iloc[0:(min(final_df.shape[0], top))]

	return(final_df.index.values, final_df.val.values, 'OK','Todo en Orden')
