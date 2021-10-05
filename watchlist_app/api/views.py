from watchlist_app.models import StreamPlatform,Watchlist
from .serializers import WatchlistSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class StreamPlatformlistAPIView(APIView):
    def get(self, request):
        platfoems = StreamPlatform.objects.all()
        serializers =StreamPlatformSerializer(platfoems, many=True,context={'request': request})
        return Response(serializers.data)
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
class StreamPlatformDetailAPIView(APIView):
    def get(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'movie does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializers = StreamPlatformSerializer(movie)
        return Response(serializers.data)
    def put(self, request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    def delete(self, request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
class WatchListAPIView(APIView):
    def get(self, request):
        movies = Watchlist.objects.all()
        serializers = WatchlistSerializer(movies, many=True)
        return Response(serializers.data)
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAPIView(APIView):
    def get(self, request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'movie does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializers = WatchlistSerializer(movie)
        return Response(serializers.data)
    def put(self, request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    def delete(self, request,pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def MovieListView(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializers = WatchlistSerializer(movies, many=True)
#         print('movies = ', movies)
#         print('serializers = ', serializers)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
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
        
#         serializers = WatchlistSerializer(movie)
#         print('movie = ', movie)
#         print('serializers = ', serializers)
#         return Response(serializers.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = WatchlistSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
