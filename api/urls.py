from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^GetLastProperty/$',GetLastProperty,name="GetLastProperty"),
	url(r'^GetSpace/$',GetSpace,name="GetSpace"),
	# url(r'^Search_Property/$',Search_Property,name="Search_Property"),
	url(r'^Details_Property/$',Details_Property,name="Details_Property"),
	url(r'^Create_Reservation/$',Create_Reservation,name="Create_Reservation"),
	url(r'^GetReservations/$',GetReservations,name="GetReservations"),
]