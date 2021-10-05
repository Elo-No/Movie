
from django.contrib import admin
from django.urls import path,include
# from .views import MovieListView,MovieDetailView
from .views import WatchListAPIView,WatchDetailAPIView,StreamPlatformlistAPIView,StreamPlatformDetailAPIView

urlpatterns = [
    # path('list/',MovieListView,name='MovieList'),
    # path('<int:pk>/',MovieDetailView,name='MovieDetail'),
    path('watchlist/',WatchListAPIView.as_view(),name='WatchList'),
    path('watchlist/<int:pk>/',WatchDetailAPIView.as_view(),name='WatchDetail'),

    path('platformlist/',StreamPlatformlistAPIView.as_view(),name='StreamPlatformlist'),
    path('platformlist/<int:pk>/',StreamPlatformDetailAPIView.as_view(),name='StreamPlatformDetail'),
]