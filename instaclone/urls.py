from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from instaclone import views

urlpatterns = [
    path('api/', views.PhotoList.as_view()),
    path('api/<int:pk>/', views.PhotoDetail.as_view()),
    path('users/', views.UserList.as_view()), 
    path('users/<int:pk>/', views.UserDetail.as_view()),
   
]