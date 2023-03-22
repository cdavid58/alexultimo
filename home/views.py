from django.http import HttpResponse
from django.shortcuts import render, redirect
from post.models import *
import json,constants

def Home(request):
	return redirect('Login')

def Index(request):
	if 'pk_user' in request.session:
		post = Post.objects.all().order_by('-pk')
		img_post = Img_Post.objects.all()
		l_p = Likes_Post.objects.all()
		if 'carrito' not in request.session:
			request.session['carrito'] = 0
		commentaries = Comment.objects.all()
		print(commentaries)

		return render(request,'index.html',{'p':post,'img':img_post,'lp':l_p, 'commentaries':commentaries})
	return redirect('Login')


def Commentaries(request):
	if request.is_ajax():
		user = User.objects.get(pk = request.session['pk_user'])
		Comment(
			post = Post.objects.get(pk = request.GET.get('pk_post')),
			user = user,
			description = request.GET.get('message')
		).save()
		data = {
			'username':user.user,
			'img_profile': constants.PATH_LOCAL+user.img_profile.url
		}
		return HttpResponse(json.dumps(data))

def Search_Friends(request):
	return render(request,'social/search_friends.html')