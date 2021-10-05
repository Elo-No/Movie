from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        return Response(serializers.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)

class MovieDetailAPIView(APIView):
    def get(self, request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'movie does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializers = MovieSerializer(movie)
        return Response(serializers.data)
    def put(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    def delete(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def MovieListView(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializers = MovieSerializer(movies, many=True)
#         print('movies = ', movies)
#         print('serializers = ', serializers)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'PUT','DELETE'])
# def MovieDetailView(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'movie does not exist'},status=status.HTTP_404_NOT_FOUND)
        
#         serializers = MovieSerializer(movie)
#         print('movie = ', movie)
#         print('serializers = ', serializers)
#         return Response(serializers.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
