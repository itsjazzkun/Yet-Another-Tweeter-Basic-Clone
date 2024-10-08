# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Check this line
    path('tweets/<int:tweet_id>/retweet/', views.tweet_retweet, name='tweet_retweet'),
]
