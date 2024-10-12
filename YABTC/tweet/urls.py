# urls.py
from django.urls import path
from . import views
from .views import register, user_login, user_logout

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Check this line
    path('tweets/<int:tweet_id>/retweet/', views.tweet_retweet, name='tweet_retweet'),
    path('tweets/<int:tweet_id>/like/', views.tweet_like, name='tweet_like'),
    path('tweets/search/', views.tweet_search, name='tweet_search'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    
    
]