from django.shortcuts import render
from .models import Reservation
from property.models import *

def List_Reservations(request):
	list_reservation = Reservation.objects.all()
	return render(request,'reservation/list_reservations.html',{'list':list_reservation})

def Details_Reservation(request,pk):
	reservation = Reservation.objects.get(pk = pk)
	inf_1 = Information.objects.get(propertys=reservation.propertys)
	inf_2 = Infomation_addtional.objects.get(propertys=reservation.propertys)
	return render(request,'reservation/details.html',{'r':reservation,'i1':inf_1,'i2':inf_2})
