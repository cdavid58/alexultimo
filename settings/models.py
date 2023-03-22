from django.db import models
from user.models import User
from property.models import Property
from reservation.models import Reservation

class Percentage(models.Model):
	porcentaje_x_persona = models.FloatField(default = 0.2)
	porcentaje_subtotal_reservacion = models.FloatField(default = 0.03)

class History_Transaccion(models.Model):
	amount_total = models.FloatField()
	amount_me = models.FloatField()
	amount_property = models.FloatField()
	date_register = models.DateField(auto_now_add = True)
	date_payment = models.DateField(auto_now_add = True)
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE,null = True, blank = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE,null = True, blank = True)
	reservation = models.ForeignKey(Reservation, on_delete = models.CASCADE,null = True, blank = True)

class Movement_History(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	description= models.CharField(max_length =  250)


class Token(models.Model):
	token = models.CharField(max_length = 96)

class Referens(models.Model):
	number = models.IntegerField(default = 10001)

	def Update_Number(self):
		n = self.number
		self.number = n + 1
		self.number.save()



	