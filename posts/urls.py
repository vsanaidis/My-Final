from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/posts/', views.course_posts, name='course_posts'),
    path('course/<int:course_id>/posts/add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]
