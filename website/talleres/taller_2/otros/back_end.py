# Back_end
# Aqui estan las funciones que va a necesitar el front (por ahora)

from taller_2.models import Review, User Business




def usuario_existe(id_usuario):
	'''
	Metodo que devuelve si un usuario existe o no

	Parametros
	------------
	id_usuario : string
		El id del ususario

	Devuelve
	----------
	Booleano
	'''

	# TODO: Yacir

	# Mock

	return(True)




def dar_usuario(id_usuario):
	'''
	Metodo que devuelve un usuario dado su id

	Parametros
	------------
	id_usuario : string
		El id del ususario

	Levanta
	-----------
	Error en caso de no existir ususario con ese id

	Devuelve
	----------
	El elemento de tipo models.User correspondiente
	'''


	# TODO: Yacir

	# Mock

	user = User(name = 'James Rodriguez', yelping_since = '12/12/2020')
	return(user)



def dar_negocio(id_negocio):
	'''
	Metodo que devuelve un negocio dado su id

	Parametros
	------------
	id_negocio : string
		El id del negocio

	Levanta
	-----------
	Error en caso de no existir negocio con ese id

	Devuelve
	----------
	El elemento de tipo models.Business correspondiente
	'''


	# TODO: Yacir

	# Mock

	neg = Business(name = 'Drogas la Rebaja', stars = 5, state = 'NV')
	return(neg)




def dar_ultimas_resenhas_usuario(id_usuario, cantidad = 10):
	'''
	Metodo que devuelve las ultimas resenhas hechas por el usuario dado.

	Si e piden mas de las que hay, devolver las que hay

	Parametros
	------------
	id_usuario : string
		El id del ususario
	cantidad : int
		La cantidad de resenhas a incluir

	Levanta
	-----------
	Error en caso de no existir ususario con ese id

	Devuelve
	----------
	Lista con la cantidad de elementos modelo.Review ordenados de mas reciente a menos reciente
	'''


	# TODO: Yacir

	# Mock
	resp = []
	for i in range(cantidad):
		res = Review(user_id = 'KSADFHAKLSDHFKASD', business_id = 'askjfhdklas', last_review = '12/12/2020', starts = '5')
		resp.append(res)


	return(res)




def dar_mejores_negocios_por_lugar(lugar, cantidad = 10):
	'''
	Metodo que devuelve los mejores lugares (mas populares) por ciudad.

	Si se piden mas de los que hay, devolver los que hay

	Yacir: Te dejo a que definas 'mejor'. Puede ser mejor ranqueado, mas resenhas etc... lo que quieras



	Parametros
	------------
	lugar : string
		El identificador del estado. Recordar que puede llevar el identificador: 'OTHER', que significa mirar en 
		los estados: ['CA', 'TX', 'NY', 'CO', 'XWY', 'GA', 'BC', 'YT', 'HPL', 'AL', 'UT', 'VT', 'WA', 'NE', 'DOW', 'MI', 'FL', 'AR', 'HI', 'MB', 'OR', 'AK', 'VA', 'CT', 'MO', 'DUR'] 
		y se deben tratar cmo uno solo.

	cantidad : int
		La cantidad de negocios a incluir

	Levanta
	-----------
	Error en caso de no existir el id solicitado

	Devuelve
	----------
	Lista con la cantidad de elementos modelo.Business ordenados de mejor a peor
	'''

	other_states = ['CA', 'TX', 'NY', 'CO', 'XWY', 'GA', 'BC', 'YT', 'HPL', 'AL', 'UT', 'VT', 'WA', 'NE', 'DOW', 'MI', 'FL', 'AR', 'HI', 'MB', 'OR', 'AK', 'VA', 'CT', 'MO', 'DUR']

	# TODO: Yacir

	# Mock
	resp = []
	for i in range(cantidad):
		neg = Business(name = 'Drogas la Rebaja', stars = 5, state = 'NV')
		resp.append(neg)


	return(res)




def dar_negocios_favoritos_de_usuario(lugar, cantidad = 10):
	'''

	Metodo que devuelve los negocios favoritos de un usuario

	Si se piden mas de las que hay, devolver las que hay

	Parametros
	------------
	id_usuario : string
		El id del ususario
	cantidad : int
		La cantidad de negocios a incluir

	Levanta
	-----------
	Error en caso de no existir ususario con ese id

	Devuelve
	----------
	Lista con la cantidad de elementos modelo.Business ordenados de favorito a menos favorito
	'''


	# TODO: Yacir

	# Mock
	resp = []
	for i in range(cantidad):
		neg = Business(name = 'Olimpica', stars = 5, state = 'NV')
		resp.append(neg)


	return(res)
