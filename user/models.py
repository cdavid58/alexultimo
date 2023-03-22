from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=30, blank = True)
	second_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length= 30, blank = True)
	last_second_name = models.CharField(max_length=30,blank=True)
	email = models.EmailField(unique=True)
	code_area = models.CharField(max_length= 5, blank = True)
	phone = models.CharField(max_length= 20, unique=True)
	user = models.CharField(max_length=50)
	pswd = models.CharField(max_length = 50)
	img_profile = models.ImageField(upload_to = "Img_Profile",default = "Img_Profile/without.jpg", blank = True)
	img_cover = models.ImageField(upload_to = "Img_Cover",default = "Img_Cover/cover.jpg", blank = True)
	description = models.TextField(blank = True)
	disable = models.BooleanField(default = False)
	active = models.BooleanField(default = False)
	verified = models.BooleanField(default = False)
	type_user = models.IntegerField(default = 2)

	def __str__(self):
		return self.email



class Wallet(models.Model):
	amount = models.IntegerField(default = 0)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

class Education(models.Model):
	school = models.CharField(max_length = 150)
	titulo = models.CharField(max_length = 150)
	froms = models.CharField(max_length = 10)
	to = models.CharField(max_length = 10)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email

class Work_Experience(models.Model):
	company = models.CharField(max_length = 150)
	cargo = models.CharField(max_length = 150)
	description = models.TextField()
	froms = models.CharField(max_length = 10)
	to = models.CharField(max_length = 10)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email


class See_Your_Profile(models.Model):
	alls = models.BooleanField(default = True)
	followers = models.BooleanField(default= False)
	only_me = models.BooleanField(default= False)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email

class Tag_You(models.Model):
	alls = models.BooleanField(default = True)
	group = models.BooleanField(default = False)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email


class Account_Settings(models.Model):
	show_followers = models.BooleanField(default=True)
	show_emai = models.BooleanField(default=True)
	show_experiences = models.BooleanField(default=True)
	show_number_phone = models.BooleanField(default=True)
	show_follow_you = models.BooleanField(default=True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email


class Shipping_Address(models.Model):
	address = models.CharField(max_length = 150)
	receiving_user = models.CharField(max_length=40)
	phone = models.CharField(max_length = 20)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email