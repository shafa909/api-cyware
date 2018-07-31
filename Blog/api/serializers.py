from rest_framework import serializers

from Blog.models import UserPost

class BlogPostSerializer(serializers.ModelSerializer):  #
	class Meta :
		model   = UserPost
		fields  = [
				'pk',
				'username',
				'email',
				'timestamp',	
		        'image',
		          ]
