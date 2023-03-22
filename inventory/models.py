from django.db import models
from user.models import User, Shipping_Address


class Categories(models.Model):
	name = models.CharField(max_length = 40)
	img = models.ImageField(upload_to = "Category",blank = True,null = True)

	def __str__(self):
		return self.name 

class Subcategories(models.Model):
	name = models.CharField(max_length = 40)
	img = models.ImageField(upload_to = "Subcategory",blank = True, null = True)
	categories = models.ForeignKey(Categories, on_delete = models.CASCADE)

	def __str__(self):
		return self.name 

class Inventory(models.Model):
	code = models.CharField(unique = True, max_length = 20)
	name = models.CharField(max_length = 100)
	price = models.FloatField()
	quanty = models.IntegerField()
	img = models.ImageField(upload_to="Product")
	description = models.TextField()
	state = models.IntegerField()
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	shipping_price = models.FloatField(default= 0.0)
	subcategories = models.ForeignKey(Subcategories,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.email+' '+str(self.code)


class Gallery(models.Model):
	img = models.ImageField(upload_to = "Product_Photos")
	inventory = models.ForeignKey(Inventory, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.inventory.code)

class Consecutive(models.Model):
	number = models.IntegerField()
	user = models.ForeignKey(User,on_delete = models.CASCADE)

class PaymentForm(models.Model):
	paymentform = models.CharField(max_length = 40)



class Order(models.Model):
	number_order = models.IntegerField(default = 0)
	code_product = models.IntegerField()
	product = models.CharField(max_length = 100)
	price = models.FloatField()
	quanty = models.IntegerField(default = 0)
	coupon = models.CharField(max_length = 10)
	shipping = models.FloatField()
	description = models.TextField()
	status = models.IntegerField(default = 0)
	user_sells = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_sells')
	user_buy = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_buyls')
	date = models.DateField(auto_now_add = True)
	time = models.TimeField(auto_now_add = True)
	payment_form = models.ForeignKey(PaymentForm,on_delete=models.CASCADE,related_name='user_buyls')
	enviar_a = models.ForeignKey(Shipping_Address,on_delete=models.CASCADE,related_name='enviar_a',null= True, blank=True)

