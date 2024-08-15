from django.urls import path
from . import views

app_name = 'friend_notifications'

urlpatterns = [
    path('friend-requests/', views.view_friend_requests, name='friend_requests'),
    path('send/<int:user_id>/', views.send_friend_request, name='send_request'),
    path('get/', views.get_friend_requests, name='get_requests'),
    path('handle/<int:request_id>/', views.handle_friend_request, name='handle_request'),
    path('cancel/<int:user_id>/', views.cancel_friend_request, name='cancel_request'),
    path('my-friends/', views.my_friends, name='my_friends'),
]