
from django.urls import path
from . import views
from blog.views import (PostList, PostDetail)
from .views import post_detail, search, aboutPage, contactPage

urlpatterns = [
    path('', views.index, name="Blog"),
    path('post', PostList.as_view(), name='post_list'),
    # path('<slug:slug>/', PostDetail.as_view(), name= 'post_detail'),
    path('search', views.search, name="search"),
    path('<slug:slug>/search', views.search, name="search"),
    path('<slug:slug>/', views.post_detail, name="post-detail"),
    path('about', views.aboutPage, name="about"),
    path('contact', views.contactPage, name="contact"),
]
