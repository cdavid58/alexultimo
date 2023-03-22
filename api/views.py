from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from user.models import User, Wallet
from property.models import *
from reservation.models import Reservation
from settings.models import Percentage, Movement_History

def GetInformation(propertys):
	return Information.objects.get(propertys = propertys)

@api_view(['POST'])
def GetLastProperty(request):
	url_photo = 'http://localhost:9090'
	__property = Property.objects.filter(complete = True)
	data = [
		{
			'pk':i.pk,
			'title':i.title,
			'photo':url_photo+str(Photo.objects.filter(propertys=i)[0].img.url),
			'space_code':i.space.code,
			'space_name':i.space.type_space,
			'beds':GetInformation(i).beds,
			'bathrooms':GetInformation(i).bathrooms,
			'parking':'Si' if GetInformation(i).parking else 'No',
			'price':i.price,
			'discount':i.discoun,
			'price_with_discount':i.PriceWithDiscount(),
			'street':i.street,
			'agent_photo': url_photo + i.user.img_profile.url,
			'agent_name':str(i.user.first_name)+' '+str(i.user.last_name),
			'description':i.description,
			'price_clean':i.price_clean
		}
		for i in __property
	]
	print(data)
	return Response(data)
	
@api_view(['POST'])
def GetSpace(request):
	url_photo = 'http://localhost:9090'
	space = Space.objects.all()[:5]
	data = [
		{
			'code':i.code,
			'name':i.type_space,
			'img': url_photo + str(i.img.url) if i.img else None,
			'total_property':len(Property.objects.filter(space=i))
		}
		for i in space
	]
	return Response(data)

@api_view(['POST'])
def Details_Property(request):
	url_photo = 'http://localhost:9090'
	i= Property.objects.get(pk = request.data['pk'])
	data = {
			'pk':i.pk,
			'title':i.title,
			'photo':url_photo+str(Photo.objects.filter(propertys=i)[0].img.url),
			'space_code':i.space.code,
			'space_name':i.space.type_space,
			'beds':GetInformation(i).beds,
			'bathrooms':GetInformation(i).bathrooms,
			'parking':'Si' if GetInformation(i).parking else 'No',
			'discount':i.discoun,
			'price':i.price,
			'price_with_discount':i.PriceWithDiscount(),
			'street':i.street,
			'price_clean':i.price_clean,
			'agent_photo': url_photo + i.user.img_profile.url,
			'agent_name':str(i.user.first_name)+' '+str(i.user.last_name),
			'agent_pk':i.user.pk,
			'description':i.description,
			'available':'Disponible' if i.available else 'No Disponible',
			'information':[
				{
					'resident':j.resident,
					'room':j.room,
					'wifi':'Si' if j.wifi else 'No',
					'tv':'Si' if j.tv else 'No',
					'parking':'Si' if j.parking else 'No',
					'kitchen':'Si' if j.kitchen else 'No',
					'washing_machine':'Si' if j.washing_machine else 'No',
					'parking':'Si' if j.parking else 'No',
					'paid_parking':'Si' if j.paid_parking else 'No',
					'air_conditioning':'Si' if j.air_conditioning else 'No',
					'work_zone':'Si' if j.work_zone else 'No',
				}
				for j in Information.objects.filter(propertys = i)
			],
			'information_extra':[
				{
					'pool':'Si' if j.pool else 'No',
					'jacuzzi':'Si' if j.jacuzzi else 'No',
					'terrace':'Si' if j.terrace else 'No',
					'grill':'Si' if j.grill else 'No',
					'outdoor':'Si' if j.outdoor else 'No',
					'campfire_place':'Si' if j.campfire_place else 'No',
					'pool_table':'Si' if j.pool_table else 'No',
					'indoor':'Si' if j.indoor else 'No',
					'piano':'Si' if j.piano else 'No',
					'exersice':'Si' if j.exersice else 'No',
					'lake':'Si' if j.lake else 'No',
					'beach':'Si' if j.beach else 'No',
					'entrace':'Si' if j.entrace else 'No'
				}
				for j in Infomation_addtional.objects.filter(propertys = i)
			],
			'multimedia':[
				{
					'img': url_photo + str(j.img.url)
				}
				for j in Photo.objects.filter(propertys = i)
			]
		}
	return Response(data)

@api_view(['POST'])
def GetReservations(request):
	reservation = Reservation.objects.filter(user_email = request.data['email']).order_by('-pk')
	data = [
		{
			'pk_property':i.propertys.pk,
			'title_property':i.propertys.title,
			'total_resident':i.adult,
			'price_evening':(i.price - i.limpieza) / i.days,
			'date_reservation':i.date_enter,
			'status':i.status,
			'money_returned':i.money_returned,
			'hour':i.hour_input
		}
		for i in reservation
	]
	return Response(data)

@api_view(['POST'])
def Create_Reservation(request):
	data = request.data
	user = User.objects.get(pk = data['pk_user'])
	__property = Property.objects.get(pk = data['propertys'])
	Reservation(
		date_enter = data['date_enter'],
		date_exit = data['date_exit'],
		user_email = data['user_email'],
		propertys = __property,
		propietrio = user,
		boys = data['boys'],
		adult = data['adult'],
		price = data['price'],
		hour_input = data['hour_input'],
		note = data['note'],
		days = data['days'],
		limpieza = data['clean']
	).save()
	percentage = Percentage.objects.last().porcentaje_subtotal_reservacion
	wallet = Wallet.objects.get(user = user)
	wallet.amount += ( int(data['price']) - (int(data['price']) * percentage) )
	wallet.save()
	Movement_History(
		user = user,
		description="Se reservo la propiedad codigo: "+str(__property.pk)+" a un precio de "+str(data['price'])
	).save()
	
	return Response({'result':True})
