# Scripts de los modelos ponderados


import numpy as np
import taller_2.otros.modelo_contenido as modelo_contenido 

import taller_2.otros.back_end as be


def dar_recomendaciones(lugar, usuario, top = 50):
	'''
	Metodo que devuelve el numero de lugares solicitado de ids de lugares, ordenados de mejor a peor.

	Segun lo ponderado por los dos modelos

	Returns
	--------
	Devuelve lo siguiente
		- Arreglo de lugares?
	'''

	# Recomendaciones por el modelo de contenido
	ids, calif, _, _ = modelo_contenido.dar_recomendaciones(lugar, usuario, top = 50)


	negocios = []
	for i in range(len(ids)):
		business_id = ids[i]
		neg = be.dar_negocio(business_id)
		neg.predicted_stars = np.round(calif[i],2)

		if neg.categories is None:
			neg.categoria = 'Ninguna'
		else: 
			neg.categoria = neg.categories.split(',')[0]

		negocios.append(neg)

	return(negocios)
