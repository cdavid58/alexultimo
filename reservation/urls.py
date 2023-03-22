from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Reservations/$',List_Reservations,name="List_Reservations"),
	url(r'^Details_Reservation/(\d)/$',Details_Reservation,name="Details_Reservation"),
]