
from django.urls import path
from . import views


urlpatterns = [
      path('', views.index, name='index'),  # Home view (or main page)
      path('tweet/', views.index, name='tweet'),  # You may have a tweet view
    # Add your other URL patterns here
]
