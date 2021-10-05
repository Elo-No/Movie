from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def MovieListView(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        print('movies = ', movies)
        print('serializers = ', serializers)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)


@api_view(['GET', 'PUT','DELETE'])
def MovieDetailView(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movie)
        print('movie = ', movie)
        print('serializers = ', serializers)
        return Response(serializers.data)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response()
