from django.db import models


class UserPost(models.Model):
	username  = models.CharField(max_length=120, unique=True)
	email     = models.EmailField(unique=True)
	image     = models.ImageField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	



	def __str__(self):
	 	return self.username

	
