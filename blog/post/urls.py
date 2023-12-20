from django.urls import path

from post.views import post_create_view, post_list_view, post_detail_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('detail/<slug:slug>', post_detail_view, name='post_detail'),
    path('create-post/', post_create_view, name='create_post'),
]
