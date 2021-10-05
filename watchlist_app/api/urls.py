
from django.contrib import admin
from django.urls import path,include
from .views import MovieListView,MovieDetailView

urlpatterns = [
    path('list/',MovieListView,name='MovieList'),
    path('<int:pk>/',MovieDetailView,name='MovieDetail'),
]