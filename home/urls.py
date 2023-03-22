from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^Index/$',Index,name="Index"),
	url(r'^Commentaries/$',Commentaries,name="Commentaries"),
	url(r'^Search_Friends/$',Search_Friends,name="Search_Friends"),
]