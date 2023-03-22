from django.utils.crypto import get_random_string
from django.db import models
from user.models import User

class Messages(models.Model):
	from_user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='From_User')
	user_to = models.ForeignKey(User,on_delete = models.CASCADE,related_name='To_User')
	message = models.TextField()
	date = models.DateField(auto_now_add = True)
	time = models.TimeField(auto_now_add = True)
	read = models.BooleanField(default = False)


class Followers(models.Model):
	user_follow = models.ForeignKey(User,on_delete = models.CASCADE,related_name='user_follow',default=1)
	user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='user_follwer',default=1)
	block = models.BooleanField(default = False)


class Notifications(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	read = models.BooleanField(default = False)