from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from user.models import *


def Create_Post(request):
	if request.method == 'POST':
		user = User.objects.get(email = request.session['email_user'])
		Post(
			issuing_user = user,
			post = request.POST.get('post')
		).save()
		if request.FILES:
			Img_Post(
				user = user,
				img = request.FILES.get('img'),
				post = Post.objects.filter(issuing_user = user).last()
			).save()

		return redirect('Index')


def Like_Post_Null(request):
	if request.is_ajax():
		try:
			post = Post.objects.get(pk = request.GET.get('post_pk'))
			post.count_like = post.count_like + 1
			post.save()
			count = post.count_like
		except Post.DoesNotExist:
			Likes_Post(
				count = 1,
				user = User.objects.get(email = request.session['email_user']),
				post = Post.objects.get(pk = request.GET.get('post_pk'))
			).save()
		return HttpResponse(count)



def Delete_Like_Post(request):
	if request.is_ajax():
		try:
			post = Post.objects.get(pk = request.GET.get('post_pk_delete'))
			post.count_like = post.count_like - 1
			post.save()
			count = post.count_like
		except Post.DoesNotExist:
			Likes_Post(
				count = 1,
				user = User.objects.get(email = request.session['email_user']),
				post = Post.objects.get(pk = request.GET.get('post_pk'))
			).save()
	# count = 0
	# try:
	# 	lp = Likes_Post.objects.get(post = Post.objects.get(pk = request.GET.get('post_pk_delete')),user = User.objects.get(email = request.session['email_user']))
	# 	lp.delete()
	# 	count = 0
	# except Likes_Post.DoesNotExist as e:
		count = post.count_like
	return HttpResponse(count)


