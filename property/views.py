from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from user.models import User
from settings.models import Movement_History

def List_Ads(request):
	__property = Property.objects.filter(user = User.objects.get(pk = request.session['pk_user']))
	return render(request,'ads/list_ads.html',{'property':__property})

def Create_Ads(request):
	start_1 = 75000
	start_2 = 89000
	start_3 = 90000
	start_4 = 187000
	result = False
	if request.is_ajax():		
		try:
			__property = Property.objects.filter(complete = False).last()
		except Property.DoesNotExist as e:
			print(e)
			__property = None

		if __property is None:
			Property(
				space=Space.objects.get(code = request.GET['id']),
				user = User.objects.get(pk = request.session['pk_user'])
			).save()
			__property = Property.objects.filter(complete = False).last()
			request.session['pk_property'] = __property.pk
			Information(propertys=__property).save()
			Infomation_addtional(propertys=__property).save()
			Security_elements(propertys=__property).save()
			result = True
		elif __property.complete:
			Property(
				space=Space.objects.get(code = request.GET['id']),
				user = User.objects.get(pk = request.session['pk_user'])
			).save()
			__property = Property.objects.filter(complete = False).last()
			request.session['pk_property'] = __property.pk
			Information(propertys=__property).save()
			Infomation_addtional(propertys=__property).save()
			Security_elements(propertys=__property).save()
			result = True
		return HttpResponse(result)
	return render(request,'ads/create_ads.html',{
			'start_1':start_1,'start_2':start_2,'start_3':start_3,'start_4':start_4
	})

def Create_Hosting_Space(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		__property.hosting_space = Hosting_Space.objects.get(code = request.GET['id'])
		__property.save()
		return HttpResponse(True)

def Save_Address(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		__property.street = request.GET['street']
		# __property.street_optional = request.GET['street_optional']
		__property.city = request.GET['city']
		__property.departament = request.GET['departament']
		__property.country = request.GET['country']
		__property.postcode = request.GET['postcode']
		__property.save()
		return HttpResponse(True)

def Update_Informations(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		inf = Information.objects.get(propertys = __property)
		inf.room = request.GET['room']
		inf.beds = request.GET['beds']
		inf.resident = request.GET['resident']
		inf.bathrooms = request.GET['bathrooms']
		inf.save()
		return HttpResponse()

def Gallery(request):
	if request.method == 'POST':
		__property = Property.objects.filter(complete = False).last()
		print(__property)
		Photo(
			img = request.FILES['file'],
			propertys = __property
		).save()
		return HttpResponse()

def Elements(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		inf = Information.objects.get(propertys = __property)
		number = int(request.GET['id'])
		print(number)
		if number == 1:
			if inf.wifi:
				inf.wifi = False
			else:
				inf.wifi = True
		if number == 2:
			if inf.tv:
				inf.tv = False
			else:
				inf.tv = True
		if number == 3:
			if inf.kitchen:
				inf.kitchen = False
			else:
				inf.kitchen = True
		if number == 4:
			if inf.washing_machine:
				inf.washing_machine = False
			else:
				inf.washing_machine = True
		if number == 5:
			if inf.parking:
				inf.parking = False
			else:
				inf.parking = True		
		if number == 6:
			if inf.air_conditioning:
				inf.air_conditioning = False
			else:
				inf.air_conditioning = True
		if number == 6:
			if inf.work_zone:
				inf.work_zone = False
			else:
				inf.work_zone = True
		inf.save()
		del inf
		inf = Infomation_addtional.objects.get(propertys = __property)
		if number == 8:
			if inf.pool:
				inf.pool = False
			else:
				inf.pool = True
		if number == 9:
			if inf.jacuzzi:
				inf.jacuzzi = False
			else:
				inf.jacuzzi = True
		if number == 10:
			if inf.terrace:
				inf.terrace = False
			else:
				inf.terrace = True
		if number == 11:
			if inf.grill:
				inf.grill = False
			else:
				inf.grill = True
		if number == 12:
			if inf.campfire_place:
				inf.campfire_place = False
			else:
				inf.campfire_place = True
		if number == 13:
			if inf.pool_table:
				inf.pool_table = False
			else:
				inf.pool_table = True
		if number == 14:
			if inf.indoor:
				inf.indoor = False
			else:
				inf.indoor = True
		inf.save()
		del inf
		return HttpResponse()
		
def UpdateTitle(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		__property.title = request.GET['title']
		__property.save()
		return HttpResponse()

def UpdateDescription(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		__property.description = request.GET['title']
		__property.save()
		return HttpResponse()

def UpdatePrice(request):
	if request.is_ajax():
		__property = Property.objects.filter(complete = False).last()
		__property.price = request.GET['price']
		__property.price_clean = request.GET['fee_start']
		__property.price_entrada = request.GET['price_clean']
		__property.complete = True
		__property.save()
		Movement_History(
			user = __property.user,
			description = "Se registro la propiedad codigo:"+str(__property.pk)
		).save()
		return HttpResponse()

def Detaild_ADS(request,pk):
	if int(pk) == 0:
		pk = request.session['pk_property']
	else:
		request.session['pk_property'] = pk
	__property = Property.objects.get(pk = pk)
	gallery = Photo.objects.filter(propertys = __property)
	inf = Information.objects.get(propertys = __property)
	inf_2 = Infomation_addtional.objects.get(propertys = __property)
	return render(request,'ads/details.html',{'gallery':gallery,'property':__property,'inf':inf,'inf_2':inf_2})
