from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Search_People/$',Search_People,name="Search_People"),
]