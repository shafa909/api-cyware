from django.contrib import admin

from .models import BlogPost


# @admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display  = ('username', 'email')
    search_fields = ('timestamp', 'email')
    list_filter   = ('username','timestamp')
  

admin.site.register(BlogPost,BlogPostAdmin)  



