# Scripts de los modelos ponderados


import numpy as np
import pandas as pd
import taller_2.otros.modelo_contenido as modelo_contenido 
import taller_2.otros.modelo_factorizado as modelo_factorizado 

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
	usuario_completo = be.dar_usuario(usuario)
	alfa = 0.5

	# Recomendaciones por el modelo de contenido
	ids, calif, _, _ = modelo_contenido.dar_recomendaciones(lugar, usuario, top = 50)

	# Valores Modelo Factorizado
	calif_svd = modelo_factorizado.dar_calificacion([usuario]*len(ids), ids)

	df_final = pd.daatFrame({'business_id':ids, 'calif_con': calif, 'calif_fac':calif_svd})

	
	df_final['calif'] = alpha*df_final.calif_con + (1-alpha)*df_final.calif_fac
	df_final.sort_values('calif', ascending = False, inplace = True)
	

	df_final = df_final.iloc[0:min(top, df_final.shape[0])]

	negocios = []
	for ind, row in df_final.iterrows():
		
		business_id = row.business_id

		neg = be.dar_negocio(business_id)

		neg.predicted_stars = np.round(row.calif,2)

		if neg.categories is None:
			neg.categoria = 'Ninguna'
		else: 
			neg.categoria = neg.categories.split(',')[0]

		negocios.append(neg)

	return(negocios)
