from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('blog_details/<blog_id>', detail_view, name = 'detail_view'),
    path('create_blog/', create_view.as_view(), name = 'create_view'),
    path('update_blog/<int:pk>', update_view.as_view(), name = 'update_view'),
    path('delete_blog/<int:pk>', delete_view.as_view(), name = 'delete_view'),
    path('create_category/', create_category.as_view(), name = 'create_category'),
    path('category/<str:cates>', listCategoryView, name = 'list_category'),
    path('like/<int:pk>', likeView, name = 'like_blog'),
    path('user_profile/<int:pk>', userProfileView, name = 'user_profile'),
    path('add_user_profile/<int:pk>', addUserProfile.as_view(), name = 'add_user_profile'),
    path('update_user_profile/<int:pk>', updateUserProfile.as_view(), name = 'update_user_profile'),
    path('add_comment/<int:pk>', add_comment, name = 'add_comment')
]
