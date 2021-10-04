from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from .models import Movie
# Create your views here.
 
def MovieListView(request):
    movies = Movie.objects.all()
    # print(movies.values())
    # print(list(movies.values()))
    data ={
        'movie' : list(movies.values())
    }
    return JsonResponse(data)

