from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Reports_property/$',Reports_property,name="Reports_property"),
	url(r'^Payment/$',Payment,name="Payment"),
	url(r'^List_Pago/$',List_Pago,name="List_Pago"),
]