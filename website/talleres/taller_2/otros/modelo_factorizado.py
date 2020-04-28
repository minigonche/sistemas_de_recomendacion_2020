# Script Modelo Por Contexto
# Scripts para el modelo por contenido


import json
import os
import pandas as pd
import numpy as np



todos_lugares = set(['OTHER', 'NC', 'AZ', 'QC', 'NV', 'IL', 'ON', 'AB', 'PA', 'WI', 'SC', 'OH'])

ubication_datos = ''

                

def dar_recomendaciones(lugar, usuario, top = 50):
	'''
	Metodo que devuelve el numero de lugares solicitado de ids de lugares, ordenados de mejor a peor.

	El metodo devuelve un codigo indicando lo sucedido. Asi son los codigos:
		(Libre de poner lo que quiera, pero es para usar en la siguiente capa, por si algo. Puede mirar los que yo puse en modelo_ponderado.dar_recomendaciones())
	Returns
	--------
	Devuelve lo siguiente
		- array string: una lista con los ids de los lugares
		- array float: una lista con las calificaciones correpsondientes
		- string: codigo indicando lo que sicedio
		- string: explicacion

	'''

	# TODO: GIO
	pass