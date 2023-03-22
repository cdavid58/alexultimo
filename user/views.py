from django.utils.crypto import get_random_string
from settings.models import Token
from django.http import HttpResponse
from django.shortcuts import render,redirect
from social.models import Followers
from inventory.models import Consecutive
from property.models import *
from settings.models import *
from .models import *
import emails

def LogOut(request):
	user = User.objects.get(pk = request.session['pk_user'])
	user.active = False
	user.save()
	del request.session['email_user']
	del request.session['photo_user']
	del request.session['pk_user']
	return redirect('Login')

def Lock_Screen(request):
	if request.is_ajax():
		message = 'Contraseña Incorrecta,error'
		try:
			user = User.objects.get(pswd = request.POST.get('pswd'))
			message = 'Contraseña Incorrecta,success'
		except User.DoesNotExist:
			pass 
		return HttpResponse(message)
	return render(request,'authentication/lock-screen.html')


def Verified_Account(request):
	pk = User.objects.get(email = request.session['email_user'])
	token = get_random_string(length=96)
	Token(token=token).save()
	emails.send_email_verified(request.session['email_user'],token,pk.pk, str(pk.first_name)+' '+str(pk.last_name))
	return render(request,'authentication/confirm-mail.html',{'email':request.session['email_user']})


def Verified_Activate(request,token,pk):
	try:
		Token.objects.get(token=token).delete()
		user = User.objects.get(pk = pk)
		request.session['photo_user'] = user.img_profile.url
		request.session['pk_user'] = user.pk
		Tag_You(user = user).save()
		See_Your_Profile(user = user).save()
		Account_Settings(user = user).save()
		Consecutive(number=1,user=user).save()
		user.active = True
		user.verified = True
		user.save()
		return redirect('Index')
	except Token.DoesNotExist:
		pass
	return redirect('Expired_Token')


def Expired_Token(request):
	return render(request,'token.html')



def Login(request):
	message = "El usuario desabilito la cuenta"
	disable = False
	if request.method == 'POST':
		try:
			user = User.objects.get(email = request.POST.get('email'),pswd = request.POST.get('pswd'), verified = True)
			if not user.disable:
				request.session['email_user'] = request.POST.get('email')
				request.session['photo_user'] = user.img_profile.url
				request.session['pk_user'] = user.pk
				request.session['type_user'] = user.type_user
				user.active = True
				user.save()
				return redirect('Index')
			else:
				disable = True
		except User.DoesNotExist as e:
			print(e)
			print("No existe")

	return render(request,'authentication/login.html',{'message':message,'disable':disable})

def Disable_Account(request):
	user = User.objects.get(email = request.session['email_user'])
	user.disable = True
	user.pswd = get_random_string(length=50)
	user.save()
	del request.session['email_user']
	del request.session['photo_user']
	del request.session['pk_user']
	return redirect('Login')

def Forgot_Password():
	pass

def Delete_Account(request):
	User.objects.get(email = request.session['email']).delete()
	del request.session['email_user']
	del request.session['photo_user']
	del request.session['pk_user']
	return redirect('Login')



def Register(request):
	term = True
	if request.method == 'POST':
		if request.POST.get('term') is not None:
			User(
				first_name = request.POST.get('firstname'),
				last_name = request.POST.get('lastname'),
				email = request.POST.get('email'),
				phone = request.POST.get('phone'),
				user = request.POST.get('username'),
				pswd = request.POST.get('pass')
			).save()
			Wallet(
				user = User.objects.get(email = request.POST.get('email'))
			).save()
			request.session['email_user'] = request.POST.get('email')
			return redirect('Verified_Account')
		else:
			term = False
	return render(request,'authentication/register.html',{'term':term})


# -----------------------------------------------------------------------------------------------------------

def Profile(request,pk):
	user = User.objects.get(pk = pk)
	__property = Property.objects.filter(user = user)
	data_property = [
		{
			'pk':i.pk,
			'cover':Photo.objects.filter(propertys = i)[0].img.url,
			'title':i.title,
			'address':i.city+' - '+i.departament+' - '+i.country
		}
		for i in __property
	]

	data_trans = [
		{
			'title':i.propertys.title,
			'total': i.amount_total,
			'amount_me': i.amount_me,
			'amount_property': i.amount_property,
			'img':Photo.objects.filter(propertys = i.propertys)[0].img.url,
			'date_payment':i.date_payment
		}
		for i in History_Transaccion.objects.filter(user = user)
	]
	followers = Followers.objects.filter(user_follow = user)
	try:
		f_user = Followers.objects.filter(user_follow = user)
	except Followers.DoesNotExist as e:
		f_user = []
	return render(request,'settings/profile.html',{'user':user, 'followers':len(followers),'follow':followers,'f_user':f_user,
		'property':data_property,'history':Movement_History.objects.filter(user = user),
			'data_trans':data_trans})

def Settings_Profile(request):
	user = User.objects.get(email = request.session['email_user'])
	education = Education.objects.filter(user = user)
	we = Work_Experience.objects.filter(user = user)
	syp = See_Your_Profile.objects.get(user = user)
	ty = Tag_You.objects.get(user = user)
	account_settings = Account_Settings.objects.get(user = user)
	request.session['photo_user'] = user.img_profile.url
	wallet = Wallet.objects.get(user = user).amount
	return render(request,'settings/settings.html',{'user':user,'education':education,'we':we,
																	'syp':syp,'ty':ty,'as':account_settings,
																	"wallet": int(wallet)
																	})


def Change_Photo_Cover(request):
	if request.method == 'POST':
		user = User.objects.get(email = request.session['email_user'])
		user.img_cover = request.FILES.get("photo_cover")
		user.save()
	return redirect('Settings_Profile')


def update_information_person(request):
	if request.is_ajax():
		verified = False
		try:
			user = User.objects.get(pk = request.session['pk_user'])
			data = request.GET
			user.first_name = data['name']
			user.last_name = data['lastname']
			user.email = data['email']
			user.phone = data['phone']
			user.description = data['description']
			user.save()
			verified = True
		except User.DoesNotExist:
			pass
		
		return HttpResponse(verified)

def Change_Photo_Profile(request):
	if request.method == 'POST':
		print(request.FILES)
		user = User.objects.get(email = request.session['email_user'])
		user.img_profile = request.FILES.get('photo_profile')
		user.save()
		request.session['img_profile'] = user.img_profile.url
		return redirect('Settings_Profile')



def Add_Education(request):
	if request.method == 'POST':
		Education(
			school = request.POST.get('school'),
			titulo = request.POST.get('titulo'),
			froms = request.POST.get('froms'),
			to = request.POST.get('to'),
			user = User.objects.get(email = request.session['email_user'])
		).save()
		return redirect('Settings_Profile')





# -------------------------------------------------------------------------------------------------------------






def Owners_List(request):
	user = User.objects.all()
	data = [
		{
			'pk':i.pk,
			'property':len(Property.objects.filter(user = i)),
			'name':i.first_name,
			'block':i.active,
			'email':i.email,
			"amount":Wallet.objects.get(user = i).amount
		}
		for i in user
	]
	print(data)
	return render(request,'settings/list_user.html',{'user':data})