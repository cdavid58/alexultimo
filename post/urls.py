from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Post/$',Create_Post,name="Create_Post"),
	url(r'^Like_Post_Null/$',Like_Post_Null,name="Like_Post_Null"),
	url(r'^Delete_Like_Post/$',Delete_Like_Post,name="Delete_Like_Post"),
]