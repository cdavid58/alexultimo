from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Product/$',List_Product,name="List_Product"),
	url(r'^Product_Details/(\d+)/$',Product_Details,name="Product_Details"),
	url(r'^Add_Cart/$',Add_Cart,name="Add_Cart"),
	url(r'^Shopping_Cart/$',Shopping_Cart,name="Shopping_Cart"),
	url(r'^CheckOut/$',CheckOut,name="CheckOut"),
	url(r'^Order/$',Orders,name="Order"),
	url(r'^List_Orders/$',List_Orders,name="List_Orders"),
	url(r'^Add_Product/$',Add_Product,name="Add_Product"),
	

	
	url(r'^Delete_Product_Shopping_Cart/$',Delete_Product_Shopping_Cart,name="Delete_Product_Shopping_Cart"),
]