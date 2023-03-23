from django.http import HttpResponse
from django.shortcuts import render
from user.models import *
from property.models import Property
import sqlite3, pandas as pd
from .models import *
from reservation.models import Reservation
from from_number_to_letters import Thousands_Separator


def Reports_property(request):
	data = [
		{
			'nombre':i.first_name,
			"email":i.email,
			'telefono':i.phone,
			'cnt_propiedades':len(Property.objects.filter(user = i)),
			'monto_en_moneda':Wallet.objects.get(user = i).amount
		}
		for i in User.objects.all()
	]
	print(data)
	df = pd.DataFrame(data)
	df.to_excel("reports.xlsx",index = False)
	return render(request,'reports/reports_property.html',{'data':data})

def Payment(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		w = Wallet.objects.get(user = user)
		w.amount = 0
		w.save()
		reservation = Reservation.objects.filter(propietrio=user)
		s = Percentage.objects.last().porcentaje_subtotal_reservacion
		for i in reservation:
			History_Transaccion(
				amount_total = Thousands_Separator(round(i.Total_Payment())),
				amount_me = Thousands_Separator(round(i.CargoMe(s))),
				amount_property = Thousands_Separator(round(i.amount_property(s))),
				propertys = i.propertys,
				user = i.propietrio,
				reservation = i
			).save()
		return HttpResponse("")

def List_Pago(request):
	data = [
		{
			"amount_total":i.amount_total,
			"amount_me":Thousands_Separator(round(i.amount_me)),
			"amount_property":Thousands_Separator(round(i.amount_property)),
			"date_register":i.date_register,
			"property":i.propertys,
			"user":i.user,
			"reservation":i.reservation,
		}
		for i in History_Transaccion.objects.all()
	]
	return render(request,'reports/transacciones.html',{'history':data})

