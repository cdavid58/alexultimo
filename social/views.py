from rest_framework import serializers
from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
from django.db.models import Q
from serializer import MessageSerializer
from .models import *
import sqlite3,json,url_request

def Chat(request):
	_data = []
	try:
		users = User.objects.get(pk = request.session['pk_user'])
		followers = Followers.objects.filter(user_follow = users)
		pk_follow = followers.first().user.email
		message = Messages.objects.filter(Q(from_user = users) | Q(user_to = users),Q(from_user = User.objects.get(email = pk_follow)) | Q(user_to = User.objects.get(email = pk_follow)) ).order_by('pk')
		for i in message:

			_data.append({
				"img_user":url_request.URL+str(User.objects.get(pk = i.from_user.pk).img_profile.url),
				"sender":i.from_user.pk,
				"message": i.message,
				"time":str(i.time.hour)+':'+str(i.time.minute),
				"status":1,
				"recvId":i.user_to.pk,
				'date':i.date.year
			})
	except Exception as e:
		print(e)

	with open(url_request.STATIC+'chat.json','w') as file:
		json.dump(_data,file)

	return render(request,'social/chat_3.html',{'user':users,'followers':followers, 'number_follow':len(followers)})

def Follow_User(request):
	 if request.is_ajax():
	 	verified = False
	 	try:
	 		u_f = User.objects.get(pk = request.GET.get('user_follow'))
	 		f = Followers.objects.get(user_follow = u_f, user = User.objects.get(pk = request.session['pk_user'])).delete()
	 	except Followers.DoesNotExist:
	 		Followers(
	 			user_follow = User.objects.get(pk = request.GET.get('user_follow')),
	 			user = User.objects.get(pk = request.session['pk_user'])
	 		).save()
	 		verified = True
	 	return HttpResponse(verified)


def Follow_Delete(request):
	 if request.is_ajax():
	 	verified = True
	 	try:
	 		u_f = User.objects.get(pk = request.GET.get('user_follow'))
	 		Followers.objects.get(user_follow = u_f, user = User.objects.get(pk = request.session['pk_user'])).delete()
	 	except Followers.DoesNotExist:
	 		Followers(
	 			user_follow = User.objects.get(pk = request.GET.get('user_follow')),
	 			user = User.objects.get(pk = request.session['pk_user'])
	 		).save()
	 		verified = False
	 	
	 	return HttpResponse(verified)



def List_Followers(request):
	user = User.objects.get(pk = request.session['pk_user'])
	f = Followers.objects.filter(user_follow = user)
	return render(request,'social/followers.html',{'followers':f,'f_count':len(f)})



def Add_Message(request):
	if request.is_ajax():
		messages = {}
		with open(url_request.STATIC+'chat.json','r') as file:
			data_message = json.loads(file.read())
		x = data_message
		conse = len(x)
		print('PK',request.GET.get('pk'))
		data = {
			"img_user": url_request.URL+str(User.objects.get(pk = request.session['pk_user']).img_profile.url),
			"sender":request.session['pk_user'],
			"message": request.GET.get('message'),
			"time":"11:45",
			"status":1,
			"recvId":request.GET.get('pk')
		}
		z = x.append(data)
		with open('./static/chat.json','w') as file:
			json.dump(x,file)

		Messages(
			from_user = User.objects.get(pk = request.session['pk_user']),
			user_to = User.objects.get(pk = request.GET.get('pk')),
			message = request.GET.get('message')
		).save()
		if not User.objects.get(pk = request.GET.get('pk')).active :
			pass
		return HttpResponse('')


def backup_message(request):
	if request.is_ajax():
		print(request.GET.get('pk'),'Recuperando')
		users = User.objects.get(pk = request.session['pk_user'])
		user = User.objects.get(pk = request.GET.get('pk'))
		message = Messages.objects.filter(Q(from_user = users) | Q(user_to = users),Q(from_user = user) | Q(user_to = user) ).order_by('pk')
		data = []
		for i in message:
			i.read = True
			i.save()
			data.append({
				"img_user": url_request.URL+str(User.objects.get(pk = i.from_user.pk).img_profile.url),
				"sender":i.from_user.pk,
				"message": i.message,
				"time":str(i.time.hour)+':'+str(i.time.minute),
				"status":1,
				"recvId":i.user_to.pk
			})		
		with open(url_request.STATIC+'chat.json','w') as file:
			json.dump(data,file)
		return HttpResponse()