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




