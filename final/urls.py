from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('notes/',include('notes.urls')),
    path('account',include('account.urls')),
    path('login/',include('account.urls')),
    path('', include('shopping_cart.urls')),
    path('posts/', include('posts.urls')),
    path('opinions/',include('opinions.urls')),
    path('friend_requests/', include('friend_notifications.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)