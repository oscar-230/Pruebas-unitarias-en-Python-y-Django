from django.urls import path
from .views import create_post, post_list, delete_post,index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_post, name='create_post'),
    path('list/', post_list, name='post_list'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
]
