from django.db import models
from property.models import Property
from user.models import User
from from_number_to_letters import Thousands_Separator

class Reservation(models.Model):
	date_enter = models.CharField(max_length = 12)
	date_exit = models.CharField(max_length = 12)
	user_email = models.EmailField()
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)
	propietrio = models.ForeignKey(User, on_delete = models.CASCADE,null = True, blank = True)
	boys = models.IntegerField()
	adult = models.IntegerField()
	price = models.IntegerField()
	hour_input = models.CharField(max_length = 20)
	note = models.TextField()
	days = models.IntegerField(default = 1)
	status = models.CharField(max_length = 45, default="En espera")
	limpieza = models.IntegerField(default = 0,null=True,blank=True)
	money_returned = models.IntegerField(default = 0)
	name_user = models.CharField(max_length = 50, null=True,blank=True)
	cancelled = models.BooleanField(default = False)

	def Total_Payment(self):
		return Thousands_Separator(self.days * self.price)

	def Price(self):
		return Thousands_Separator(self.price)

	def CargoMe(self,p):
		return int(self.price * p)

	def amount_property(self,p):
		return int(self.price - (self.price * p))