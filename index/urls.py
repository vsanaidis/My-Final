from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('search_friends', views.search_friends, name='search_friends'),
]
