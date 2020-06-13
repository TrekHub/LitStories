from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('blogPost/<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail')
]
