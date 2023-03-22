from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Chat/$',Chat,name="Chat"),
	url(r'^Add_Message/$',Add_Message,name="Add_Message"),
	url(r'^Follow_User/$',Follow_User,name="Follow_User"),
	url(r'^Follow_Delete/$',Follow_Delete,name="Follow_Delete"),
	
	url(r'^List_Followers/$',List_Followers,name="List_Followers"),
	url(r'^backup_message/$',backup_message,name="backup_message"),
	
]