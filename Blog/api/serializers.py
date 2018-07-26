from rest_framework import serializers

from Blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):  #
	class Meta :
		model   = BlogPost
		fields  = [
				'pk',
				'username',
				'email',
				'timestamp',	
		        'image',
		          ]