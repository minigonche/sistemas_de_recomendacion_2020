from django.db import models




# User
class Review(models.Model):
	'''
	Clase que modela un review
	'''
	# User ID
	user_id = models.CharField(max_length=40)
	# business_id
	business_id = models.CharField(max_length=40)
	# Date the of review
	last_review = models.DateField(null=True)
	# anno de l review
	year_review = models.PositiveIntegerField(null=True)
	# rating
	stars = models.PositiveIntegerField(null=True)
	# votos al review
	attractive_count = models.PositiveIntegerField(null=True)
	#review_id
	review_id = models.CharField(max_length=40, null=True)

class User(models.Model):
	'''
	Clase que modela un user
	'''
	average_stars = models.FloatField(null=True)
	compliment_cool = models.IntegerField(null=True)
	compliment_cute = models.IntegerField(null=True)
	compliment_funny = models.IntegerField(null=True)
	compliment_hot = models.IntegerField(null=True)
	compliment_list = models.IntegerField(null=True)
	compliment_more = models.IntegerField(null=True)
	compliment_note = models.IntegerField(null=True)
	compliment_photos = models.IntegerField(null=True)
	compliment_plain = models.IntegerField(null=True)
	compliment_profile = models.IntegerField(null=True)
	compliment_writer = models.IntegerField(null=True)
	cool = models.IntegerField(null=True)
	fans = models.IntegerField(null=True)
	funny = models.IntegerField(null=True)
	name = models.CharField(max_length=40)
	review_count = models.IntegerField(null=True)
	useful = models.IntegerField(null=True)
	user_id = models.CharField(max_length=40)
	yelping_since = models.DateField(null=True)

class Business(models.Model):
	'''
	Clase que modela un business
	'''
	address = models.CharField(max_length=40)
	business_id = models.CharField(max_length=40)
	categories = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	is_open = models.IntegerField(null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	name = models.CharField(max_length=40)
	postal_code = models.CharField(max_length=40)
	review_count = models.IntegerField(null=True)
	stars = models.FloatField(null=True)
	state = models.CharField(max_length=40)







