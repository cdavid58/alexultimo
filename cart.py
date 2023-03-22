from django.http import HttpResponseRedirect
from decimal import Decimal
from django.conf import settings
from datetime import date
from datetime import datetime
from inventory.models import Inventory

class Carrito(object):
	def __init__(self,request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart
		self.request = request

	def save(self):
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modified = True

	def add(self,product,quanty):

		total = float(product.price) * float(quanty)
		if str(product.pk) in self.cart:
			if int(quanty) == 0:
				del self.cart[str(product.pk)]
				if int(self.request.session['carrito']) > 0:
					n = int(self.request.session['carrito']) - 1
					self.request.session['carrito'] = n
				self.save()
			else:
				total = float(product.price) * float(quanty)
				self.cart[str(product.pk)]['quanty'] = quanty
				self.cart[str(product.pk)]['total'] = total
				self.save()

		else:
			if int(quanty) >= 1:
				self.request.session['carrito'] +=1
				self.cart[str(product.pk)] = {'pk':product.pk,'code':product.code,'product':product.name,'quanty':quanty,'price':product.price,
															'total':total,'img':'http://localhost:8000'+product.img.url,'shipping_price':product.shipping_price,'user':product.user.pk}
		print(self.cart)
		self.save()

	def remove(self,product):
		product_id = str(product.pk)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		product_ids = self.cart.keys()
		products = Inventory.objects.filter(id__in=product_ids)
		'''for product in products:
			self.cart[str(product.id)]['product']=product'''

		for item in self.cart.values():
			#item['precio']=Decimal(item['precio'])
			#item['total']=item['precio']*item['cantidad']
			yield item


	def __len__(self):
		return sum(int(item['quanty']) for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True