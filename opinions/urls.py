from django.urls import path
from . import views

urlpatterns = [
    path('opinions/', views.professor_list, name='opinions'),
    path('professor/<int:professor_id>/', views.professor_posts, name='professor_posts'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]