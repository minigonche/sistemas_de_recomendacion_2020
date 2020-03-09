from django.db import models




# User
class User(models.Model):

	# User ID
	user_id = models.CharField(max_length=20)
	# Password
	password = models.CharField(max_length=20)
	# Date the user joined
	date_join = models.DateField(null=True)
	# Age
	age = models.PositiveIntegerField(null=True)
	# Sex
	sex = models.NullBooleanField(null=True)
	#country
	country = models.CharField(max_length=5, null=True)


	def dar_sexo(self):

		sexo = 'No hay informacion'
		if self.sex is not None:
			if self.sex:
				sexo = 'Hombre'
			else:
				sexo = 'Mujer'

		return(sexo)


	def dar_pais(self):

		pais = 'No hay informacion'
		if self.country is not None:
			pais = self.country

		return(pais)

	def dar_fecha(self):

		fecha_registro = 'No tiene'
		if self.date_join is not None:
			fecha_registro = self.date_join.strftime('%Y-%m-%d')

		return(fecha_registro)


	def dar_edad(self):

		edad = 'No hay informacion'
		if self.age > 0:
			edad = self.age

		return(edad)


	def __str__(self):

		usuario = self.user_id
		pwd = self.password

		return('Usuario: {}, Pwd: {}, Fecha Registro: {}, Edad: {}, Sexo: {}, Pais: {}'.format(usuario, pwd, self.dar_fecha(), self.dar_edad(), self.dar_sexo(), self.dar_pais()))


class User_info(models.Model):

	# User ID
	user_id = models.CharField(max_length=20)
	# Password
	numero_artistas = models.IntegerField()
	# Date the user joined
	numero_reproducciones = models.IntegerField()
	# Age
#Reproduccion
class Reproduction(models.Model):

	# User ID
	user_id = models.CharField(max_length=20)
	# Song name
	song_name = models.CharField(max_length=20)
	# Song id
	song_id = models.CharField(max_length=20)
	# Date of the reproduction
	date = models.DateTimeField(null=True)
	# Name of the artist
	artist_name = models.CharField(max_length=20)
	# Artist id
	artist_id = models.CharField(max_length=20)

	def dar_fecha(self):
		fecha = 'No tiene'
		if self.date is not None:
			fecha = self.date.strftime('%Y-%m-%d')

		return (fecha)

	def to_dict(self):
		'''
		Vuelve la clase un diccionario
		'''

		resp = {}
		resp['user_id'] = self.user_id
		resp['song_name'] = self.song_name
		resp['song_id'] = self.song_id
		resp['artist_name'] = self.artist_name
		resp['artist_id'] = self.artist_id
		resp['date'] = self.dar_fecha()
		return resp

class Artist(models.Model):
	'''
	Clase que modela un artista (con un rating asociado)
	'''
	# Artist name
	artist_name = models.CharField(max_length=20)
	# Artist id
	artist_id = models.CharField(max_length=20)
	# Rating of the user
	user_rating = models.IntegerField(null=True)
	# Global rating
	global_rating = models.IntegerField(null=True)

	def to_dict(self):
		'''
		Vuelve la clase un diccionario
		'''

		resp = {}
		resp['artist_name'] = self.artist_name
		resp['user_rating'] = self.user_rating
		resp['global_rating'] = self.global_rating
		return resp



