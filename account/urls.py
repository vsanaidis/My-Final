from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.account_view, name='account'),
    path('login/', views.user_login, name="login"),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
    path('password/change/', views.custom_password_change, name='password_change'),
    path('password/change/done/', views.password_change_done, name='password_change_done'),
    # path('update-avatar/', views.update_avatar, name='update_avatar'),
    path('update-profile-picture/', views.profile_picture_update, name='update_profile_picture'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
