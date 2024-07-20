from django.urls import path
from . import views



urlpatterns = [
    path('', views.account_view, name='account'),
    path('login/', views.user_login, name="login"),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
]
