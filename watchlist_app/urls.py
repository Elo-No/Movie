
from django.contrib import admin
from django.urls import path,include
from .views import MovieListView
urlpatterns = [
    path('list/',MovieListView,name='MovieList'),
]
