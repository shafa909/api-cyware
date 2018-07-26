from .views import  BlogPostRudView ,BlogPostAPIView , BlogPostAPIListView 

from django.conf.urls import url


urlpatterns = [
	url(r'^$', BlogPostAPIListView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
     
]
