from django.db import models
from user.models import User

class Space(models.Model):
	code = models.IntegerField(default = 0)
	type_space = models.CharField(max_length = 50)
	img = models.ImageField(upload_to = "ImageCategory",null = True, blank = True)

	def __str__(self):
		return self.type_space

class Hosting_Space(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 50)
	description = models.TextField()

	def __str__(self):
		return self.name

class Tag_Description(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Extras(models.Model):
	security_cameras = models.BooleanField(default = False)
	weapons = models.BooleanField(default = False)
	dangerous_animals = models.BooleanField(default = False)

class Property(models.Model):
	space = models.ForeignKey(Space, on_delete = models.CASCADE, null = True, blank=True,related_name='space')
	title = models.CharField(max_length = 150, null = True, blank=True)
	hosting_space = models.ForeignKey(Hosting_Space, on_delete = models.CASCADE, null = True, blank=True,related_name='hosting_space')
	street = models.CharField(max_length = 150, null = True, blank=True)
	street_optional = models.CharField(max_length = 150, null = True, blank=True)
	city = models.CharField(max_length = 150, null = True, blank=True)
	departament = models.CharField(max_length = 150, null = True, blank=True)
	country = models.CharField(max_length = 150, null = True, blank=True)
	tag_description = models.ForeignKey(Tag_Description, on_delete = models.CASCADE, null = True, blank=True,related_name='tag_description')
	description = models.TextField(default="")
	price = models.FloatField(default=0)
	extras = models.ForeignKey(Extras,on_delete=models.CASCADE, null = True, blank=True,related_name='extras')
	complete = models.BooleanField(default = False)
	discoun = models.FloatField(default = 0)
	user = models.ForeignKey(User, on_delete = models.CASCADE,  null = True, blank=True,related_name='User')
	available = models.BooleanField(default = False)
	postcode = models.CharField(max_length = 10,null = True, blank=True)
	price_clean = models.IntegerField(default = 0)
	price_entrada = models.IntegerField(default = 0)
	btn_clean = models.BooleanField(default = False)
	cod_ref = models.IntegerField(default = 0)

	def PriceWithDiscount(self):
		return self.price - (self.price * (self.discoun / 100))


class Information(models.Model):
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)
	resident = models.IntegerField(default=0, null = True, blank=True)
	room = models.IntegerField(default=0, null = True, blank=True)
	beds = models.IntegerField(default=0, null = True, blank=True)
	bathrooms = models.IntegerField(null = True, blank=True)
	wifi = models.BooleanField(default=False)
	tv = models.BooleanField(default=False)
	parking = models.BooleanField(default=False)
	kitchen = models.BooleanField(default=False)
	washing_machine = models.BooleanField(default=False)
	parking = models.BooleanField(default=False)
	paid_parking = models.BooleanField(default=False)
	air_conditioning = models.BooleanField(default=False)
	work_zone = models.BooleanField(default=False)

class Infomation_addtional(models.Model):
	pool = models.BooleanField(default = False)
	jacuzzi = models.BooleanField(default = False)
	terrace = models.BooleanField(default = False)
	grill = models.BooleanField(default = False)
	outdoor = models.BooleanField(default = False)
	campfire_place = models.BooleanField(default = False)
	pool_table = models.BooleanField(default = False)
	indoor = models.BooleanField(default = False)
	piano = models.BooleanField(default = False)
	exersice = models.BooleanField(default = False)
	lake = models.BooleanField(default = False)
	beach = models.BooleanField(default = False)
	entrace = models.BooleanField(default = False)
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)


class Security_elements(models.Model):
	smoke_detector = models.BooleanField(default = False)
	first_aid_kit = models.BooleanField(default = False)
	fire_extinguisher = models.BooleanField(default = False)
	carbon_monoxide_detector = models.BooleanField(default = False)
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)

class Photo(models.Model):
	img = models.ImageField(upload_to = "Gallery")
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)


class Comments(models.Model):
	message = models.TextField()
	user_email = models.EmailField(null=True, blank = True)
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE,null=True, blank = True)
