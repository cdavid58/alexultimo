from django.db import models
from user.models import User

class Notifications_Message(models.Model):
	message = models.CharField(max_length = 150)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	read = models.BooleanField(default = False)
	date = models.DateField(auto_now_add = True)
	time = models.TimeField(auto_now_add = True)
	url = models.CharField(max_length = 40)