from django.shortcuts import render
from django.views import generic
from .models import  blogPost


class BlogList(generic.ListView):
    model = blogPost
    queryset = blogPost.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'
    
class BlogDetail(generic.DetailView):
    model = blogPost
    template_name = 'blog_detail.html'
    context_object_name = "post"
