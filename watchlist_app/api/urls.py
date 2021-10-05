
from django.contrib import admin
from django.urls import path,include
# from .views import MovieListView,MovieDetailView
from .views import MovieListAPIView,MovieDetailAPIView

urlpatterns = [
    # path('list/',MovieListView,name='MovieList'),
    # path('<int:pk>/',MovieDetailView,name='MovieDetail'),
    path('list/',MovieListAPIView.as_view(),name='MovieList'),
    path('<int:pk>/',MovieDetailAPIView.as_view(),name='MovieDetail'),
]