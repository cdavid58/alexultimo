from django.conf.urls import url
from .update_information import *
from .views import *

urlpatterns=[
	url(r'^Login/$',Login,name="Login"),
	url(r'^Register/$',Register,name="Register"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
	url(r'^Disable_Account/$',Disable_Account,name="Disable_Account"),
	url(r'^Delete_Account/$',Delete_Account,name="Delete_Account"),
	url(r'^Profile/(\d+)/$',Profile,name="Profile"),
	url(r'^Settings_Profile/$',Settings_Profile,name="Settings_Profile"),
	url(r'^Verified_Account/$',Verified_Account,name="Verified_Account"),
	
	url(r'^Verified_Activate/(\w+)/(\w+)/$',Verified_Activate,name="Verified_Activate"),
	url(r'^Expired_Token/$',Expired_Token,name="Expired_Token"),
	


	url(r'^update_information_person/$',update_information_person,name="update_information_person"),
	url(r'^Change_Photo_Profile/$',Change_Photo_Profile,name="Change_Photo_Profile"),
	url(r'^Change_Photo_Cover/$',Change_Photo_Cover,name="Change_Photo_Cover"),
	

	url(r'^Update_See_Your_Profile/$',Update_See_Your_Profile,name="Update_See_Your_Profile"),
	url(r'^Update_Tag_You/$',Update_Tag_You,name="Update_Tag_You"),
	url(r'^Update_Account_Settings/$',Update_Account_Settings,name="Update_Account_Settings"),
	url(r'^Update_Password/$',Update_Password,name="Update_Password"),

	url(r'^Owners_List/$',Owners_List,name="Owners_List"),
	# url(r'^Profile/(\d+)/$',Profile,name="Profile"),

]