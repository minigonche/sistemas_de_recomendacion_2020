# Scripts de los modelos ponderados


import numpy as np
import taller_2.otros.modelo_contenido as modelo_contenido 


def dar_recomendaciones(lugar, usuario, top = 50):
	'''
	Metodo que devuelve el numero de lugares solicitado de ids de lugares, ordenados de mejor a peor.

	Segun lo ponderado por los dos modelos

	Returns
	--------
	Devuelve lo siguiente
		- Arreglo de lugares?
	'''

	# TODO
	# MOCK
	lugares = []
	for i in range(top):
		lugares.append({'lugar':'Lugar {}'.format(i), 'stars': 1 + np.random.randint(5)})

	return(lugares)

