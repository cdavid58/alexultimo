from django.http import HttpResponse
from django.db.models import Sum
from django.shortcuts import render, redirect
from cart import Carrito
from user.models import Shipping_Address,User
from .models import *
import json
from settings.models import Referens

def List_Product(request):
	if 'pk_user' not in request.session:
		return render('authentication/login.html')

	inventory = Inventory.objects.all()

	return render(request,'ecommerce/product_grid.html',{'i':inventory})

def Product_Details(request,pk):
	if 'pk_user' not in request.session:
			return render('authentication/login.html')
	inventory = Inventory.objects.get(pk = pk)
	gallery = Gallery.objects.filter(inventory = inventory)
	return render(request,'ecommerce/product_details.html',{'product':inventory,'gallery':gallery})

def Shopping_Cart(request):
	cart = Carrito(request)
	subtotal = 0
	shipping_price = 0
	for i in cart:
		subtotal += i['total']
		shipping_price += i['shipping_price']
	total = subtotal + shipping_price

	return render(request,'ecommerce/shopping_cart.html',{'cart':cart,'subtotal':subtotal,'shipping_price':shipping_price,'total':total,'total_items':len(cart)})

def CheckOut(request):
	cart = Carrito(request)
	if len(cart) >= 1:
		if request.is_ajax():
			request.session['enviar_a'] = request.GET['id']
			return HttpResponse('')
		if request.method == 'POST':
			sa_number = len(Shipping_Address.objects.filter(user = User.objects.get(pk = request.session['pk_user'])))
			if sa_number < 2:
				Shipping_Address(
					address = request.POST.get('address_user'),
					receiving_user = request.POST.get('receiving_user'),
					phone = request.POST.get('phone_user'),
					user = User.objects.get(pk = request.session['pk_user'])
				).save()
		sa = Shipping_Address.objects.filter(user = User.objects.get(pk = request.session['pk_user']))

		subtotal = 0
		shipping_price = 0
		for i in cart:
			subtotal += i['total']
			shipping_price += i['shipping_price']
		total = subtotal + shipping_price
		buyer = User.objects.get(pk = request.session['pk_user'])
		return render(request,'ecommerce/checkout.html',{'sa':sa,'cart':cart,'subtotal':subtotal,
																			'shipping_price':shipping_price,'total':total,
																			'total_items':len(cart),'buyer':buyer,'url':"http://localhost:8000/inventory/Order/",
																			"referens":Referens.objects.get(pk = 1).number
																		})

	return redirect('Shopping_Cart')

def Orders(request):
	from datetime import date
	cart = Carrito(request)
	values_cart = cart
	user_pk = 0
	subtotal = 0
	shipping_price = 0
	for i in cart:
		subtotal += i['total']
		shipping_price += i['shipping_price']
		print(i['shipping_price'])
		c = Consecutive.objects.get(user = User.objects.get(pk = i['user']))
		user_pk = i['user']
		Order(
			number_order = c.number,
			code_product = i['code'],
			product = i['product'],
			quanty = i['quanty'],
			price = i['price'],
			coupon = 0,
			shipping = i['shipping_price'],
			description ='',
			user_sells = User.objects.get(pk = request.session['pk_user']),
			user_buy = User.objects.get(pk = user_pk),
			payment_form = PaymentForm.objects.get(pk = 1),
			enviar_a = Shipping_Address.objects.get(pk = request.session['enviar_a'])
		).save()

	c = Consecutive.objects.get(user = User.objects.get(pk = i['user']))
	
	total = subtotal + shipping_price

	all_orden = Order.objects.filter(number_order = c.number)
	last_orden = Order.objects.filter(number_order = c.number).last()

	n = c.number + 1
	c.number = n
	c.save()
	r = Referens()
	r.Update_Number()
	cart.clear()

	f = PaymentForm.objects.get(pk = last_orden.payment_form.pk).paymentform
	request.session['carrito'] = 0

	return render(request,'ecommerce/invoice.html',{
																	'all_orden':all_orden,'last_orden':last_orden,
																	'subtotal':subtotal,'shipping_price':shipping_price,'total':total,'pf':f
																	})

def Add_Cart(request):
	if request.is_ajax():
		cart = Carrito(request)
		inventory = Inventory.objects.get(pk = request.GET.get('pk'))
		quanty = request.GET.get('quanty')
		cart.add(inventory,quanty)
		return HttpResponse(request.session['carrito'])

def Delete_Product_Shopping_Cart(request):
	if request.is_ajax():
		cart = Carrito(request)
		product = Inventory.objects.get(pk = request.GET.get('pk'))
		cart.remove(product)
		n = int(request.session['carrito']) - 1
		request.session['carrito'] = n
		subtotal = 0
		shipping_price = 0
		for i in cart:
			subtotal += i['total']
			shipping_price += i['shipping_price']
		total = subtotal + shipping_price		
		return HttpResponse(json.dumps([{'total':total,'number':request.session['carrito']}]))



def List_Orders(request):
	if request.is_ajax():
		id_order = request.GET['id'].split('.')
		order = Order.objects.filter(number_order = id_order[1])
		for i in order:
			i.status = id_order[0]
			i.save()
		return HttpResponse('')
	import sqlite3, url_request
	connect = sqlite3.connect(url_request.SQLITE3)
	cur = connect.cursor()
	cur.execute("SELECT DISTINCT number_order FROM inventory_Order")
	data = cur.fetchall()
	_data = []
	for i in data:
		o = Order.objects.filter(number_order = i[0]).last()
		price = Order.objects.filter(number_order = i[0]).aggregate(Sum('price'), Sum('quanty'))
		_data.append({
			'number_order': o.number_order,
			'user_buy':o.user_buy.user.capitalize(),
			'email':o.user_buy.email,
			'date':o.date,
			'total': price['price__sum'] * price['quanty__sum'],
			"status":o.status
		})
	print(_data)
	return render(request,'orders/order-list.html',{'data':_data})


def Order_Details(request,pk):
	return render(request,'orders/order-details.html')



def Add_Product(request):
	if request.method == 'POST':
		pass
		# Inventory(
			
		# ).save()
	if request.is_ajax():
		s = Subcategories.objects.filter(categories = request.GET.get('pk'))
		data = [{'name':i.name,'pk':i.pk} for i in s]
		return HttpResponse(json.dumps(data))

	categories = Categories.objects.all()

	return render(request,'ecommerce/addproduct.html',{'c':categories})