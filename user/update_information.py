from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def Update_See_Your_Profile(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		syp = See_Your_Profile.objects.get(user = user)
		value = int(request.GET.get('value'))
		if value == 1:
			syp.alls = True
			syp.followers = False
			syp.only_me = False
		elif value == 2:
			syp.all = False
			syp.followers = True
			syp.only_me = False
		elif value == 3:
			syp.all = False
			syp.followers = False
			syp.only_me = True
		syp.save()
	return HttpResponse('')

def Update_Tag_You(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		tag = Tag_You.objects.get(user = user)
		value = int(request.GET.get('value'))
		if value == 1:
			tag.alls = True
			tag.group = False
		elif value == 2:
			tag.alls = False
			tag.group = True
		tag.save()
	return HttpResponse('')



def Update_Account_Settings(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		account_settings = Account_Settings.objects.get(user = user)
		value = int(request.GET.get('value'))

		if value == 1:
			account_settings.show_followers = False if account_settings.show_followers else True
		elif value == 2:
			account_settings.show_emai = False if account_settings.show_emai else True
		elif value == 3:
			account_settings.show_experiences = False if account_settings.show_experiences else True
		elif value == 4:
			account_settings.show_number_phone = False if account_settings.show_number_phone else True
		elif value == 5:
			account_settings.show_follow_you = False if account_settings.show_follow_you else True

		account_settings.save()
		return HttpResponse('')

def Update_Password(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		message = "Contraseña Incorrecta,error"
		if request.GET.get('old_pass') == user.pswd:
			user.pswd = request.GET.get('new_pass')
			user.save()
			message = "Contraseña Actualizada,success"
			del request.session['email_user']
			del request.session['photo_user']
			del request.session['pk_user'] 
			return HttpResponse(message)
		return HttpResponse(message)




