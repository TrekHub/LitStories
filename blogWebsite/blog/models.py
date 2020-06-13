from django.db import models
from django.conf.urls import include
from django.contrib.auth.models import User

STATUS = (
    (0,'Draft'),
    (1,'Publish')
    
)
class blogPost(models.Model):
   
    title = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'blog_posts')
    updated_on =  models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover = models.ImageField(upload_to='photos/')
     
     
    class Meta:
         ordering = [ '-created_on']
    def __str__(self):
             return self.title
     
    
     
   
         

