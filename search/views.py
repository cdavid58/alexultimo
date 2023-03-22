from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from user.models import User

def Search_People(request):
	search_people = str(request.POST.get('search_people'))
	user = User.objects.filter(Q(email__icontains = search_people) | Q(user__icontains = search_people) | Q(first_name__icontains = search_people) | Q(last_name__icontains = search_people), verified=True,disable=False)

	return render(request,'search/search_people.html',{'users':user,'number_people':len(user)})


