from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('notes/<str:title>/', views.notes_details, name='notes_details'),
    path('search/',views.search_views.as_view(), name="search_bar"),
    # path('posts/', views.posts_views, name="posts")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)