# Back_end
# Aqui estan las funciones que va a necesitar el front (por ahora)

from taller_2.models import Review, User, Business




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
	res = User.objects.filter(user_id = id_usuario).exists()


	# Mock

	return(res)




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
	usuario_pedido = User.objects.all().get(user_id=id_usuario)
	# Mock

	#user = User(name = 'James Rodriguez', yelping_since = '12/12/2020')
	return(usuario_pedido)



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
	negocio_pedido = Business.objects.all().get(business_id=id_negocio)

	# Mock

	#neg = Business(name = 'Drogas la Rebaja', stars = 5, state = 'NV')
	#print(type(neg))
	return(negocio_pedido)




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
	usuario_reviews = Review.objects.filter(user_id=id_usuario).order_by('-last_review')
	res = []
	if len(usuario_reviews)<cantidad:
		res = list(usuario_reviews)
	else:
		res = list(usuario_reviews[:cantidad])

	# Mock
	#resp = []
	#for i in range(cantidad):
	#	res = Review(user_id = 'KSADFHAKLSDHFKASD', business_id = 'askjfhdklas', last_review = '12/12/2020', starts = '5')
	#	resp.append(res)


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
	negocios_populares = None
	if lugar == 'OTHER':
		negocios_populares = Business.objects.filter(state__in=other_states).order_by('-review_count')
	else:
		negocios_populares = Business.objects.filter(state=lugar).order_by('-review_count')

	cantidad_extra = 2*cantidad
	res = []
	if len(negocios_populares) < cantidad_extra:
		if len(negocios_populares) < cantidad:
			res = list(negocios_populares.order_by('-stars'))
		else:
			res = list(negocios_populares.order_by('-stars')[:cantidad])
	else:
		cantidad_extra_inf =  cantidad_extra-1
		limite_popular = negocios_populares[cantidad_extra_inf:cantidad_extra][0].review_count
		res = list(negocios_populares.filter(review_count__gte=limite_popular).order_by('-stars')[:cantidad])
	# Mock
	#resp = []
	#for i in range(cantidad):
	#	neg = Business(name = 'Drogas la Rebaja', stars = 5, state = 'NV')
	#	resp.append(neg)


	return(res)




def dar_negocios_favoritos_de_usuario(id_usuario, cantidad = 10):
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
	usuario_negocios_favoritos = Review.objects.filter(user_id=id_usuario).order_by('-stars').values_list('business_id', flat=True)
	res = []
	if len(usuario_negocios_favoritos) < cantidad:
		res = list(Business.objects.filter(business_id__in=usuario_negocios_favoritos))
	else:
		usuario_negocios_favoritos = usuario_negocios_favoritos[:cantidad]
		res = list(Business.objects.filter(business_id__in=usuario_negocios_favoritos))

	# Mock
	#resp = []
	#for i in range(cantidad):
	#	neg = Business(name = 'Olimpica', stars = 5, state = 'NV')
	#	resp.append(neg)


	return(res)
