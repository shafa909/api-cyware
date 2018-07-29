#genaric
from django.db.models import Q
from rest_framework import generics , mixins
from Blog.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(generics.CreateAPIView):  
	lookup_field  = 'pk'  # we can use slug , id
	serializer_class =  BlogPostSerializer
	queryset      = BlogPost.objects.all()

	def get_quertset(self):
		return queryset


class BlogPostAPIListView(mixins.CreateModelMixin,generics.ListAPIView):  
	lookup_field  = 'pk'  # we can use slug , id
	serializer_class =  BlogPostSerializer
	queryset      = BlogPost.objects.all()

	# def get_quertset(self):
	# 	return queryset
	def get_queryset(self):
		qs = BlogPost.objects.all()
	
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(username__icontains=query)|Q(email__icontains=query)).distinct()
		return qs	
	
	def post(self,request,*args,**kwargs):
		return self.create(request, *args, **kwargs)

	def get_quertset(self):
		qs = BlogPost.objects.all()
		query = self.request.GET("q")
		if query is not None:
			qs = qs.filter(Q(username__icontains=query)) #|Q(email__icontains=query)).distinct()
		return qs	

		
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):  
	lookup_field  = 'pk'  # we can use slug , id
	serializer_class =  BlogPostSerializer
	queryset      = BlogPost.objects.all()

	def get_quertset(self):
		return queryset
