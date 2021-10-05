from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def MovieListView(request):
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies,many=True)
        print('movies = ',movies)
        print('serializers = ',serializers)
        return Response(serializers.data)

@api_view()
def MovieDetailView(request,pk):
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movie)
        print('movie = ',movie)
        print('serializers = ',serializers)
        return Response(serializers.data)
