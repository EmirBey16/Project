from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('news/', posts_list, name='post_list_url'),
    path('post/<str:slug>/', posts_detail, name='posts_detail'),  # http://127.0.0.1:8000/blog/post/<str:slug>/
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('add/', add_news, name='add_news_url')
]