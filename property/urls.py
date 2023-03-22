from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Ads/$',List_Ads,name="List_Ads"),
	url(r'^Create_Ads/$',Create_Ads,name="Create_Ads"),
	url(r'^Create_Hosting_Space/$',Create_Hosting_Space,name="Create_Hosting_Space"),
	url(r'^Save_Address/$',Save_Address,name="Save_Address"),
	url(r'^Update_Informations/$',Update_Informations,name="Update_Informations"),
	url(r'^Gallery/$',Gallery,name="Gallery"),
	url(r'^Elements/$',Elements,name="Elements"),
	url(r'^UpdateTitle/$',UpdateTitle,name="UpdateTitle"),
	url(r'^UpdateDescription/$',UpdateDescription,name="UpdateDescription"),
	url(r'^UpdatePrice/$',UpdatePrice,name="UpdatePrice"),
	url(r'^Detaild_ADS/(\d+)/$',Detaild_ADS,name="Detaild_ADS"),
]