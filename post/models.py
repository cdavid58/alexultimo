from django.db import models
from user.models import User

class Post(models.Model):
	issuing_user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.TextField()
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add = True)
	count_like = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.pk)


class Img_Post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	img = models.ImageField(upload_to = "Img_Post")
	post = models.ForeignKey(Post,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email


class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add = True)

	def __str__(self):
		return self.post.issuing_user.email


class Likes_Post(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.user.email



class Likes_Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.post.issuing_user.email








