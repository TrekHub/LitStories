from django.contrib import admin
from .models import blogPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on','cover')
    list_filter =("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}
    
# Registering our posts here
admin.site.register(blogPost, PostAdmin)