from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.movies.models import Favourite
from apps.movies.models import Movie
from apps.movies.serializers import FavouriteSerializer


class FavouriteView(DestroyAPIView, CreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = IsAuthenticated,

    def post(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user_id = request.data['user']
            if not Favourite.objects.filter(movie_id=movie_id, user_id=user_id).exists():
                favourite = Favourite.objects.create(user_id=request.data['user'], movie_id=request.data['movie'])
                movie = get_object_or_404(Movie, pk=movie_id)
                movie.favourites_count += 1
                movie.save()
                favourite.save()
                return Response({'success': 'Movie added to favourite library'}, status=status.HTTP_201_CREATED)
            return Response({'error': 'This movie is already in favourite library!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user_id = request.data['user']
            if Favourite.objects.filter(movie_id=movie_id, user_id=user_id).exists():
                Favourite.objects.filter(movie_id=movie_id, user_id=user_id).delete()
                movie = get_object_or_404(Movie, pk=movie_id)
                movie.favourites_count -= 1
                movie.save()
                return Response({'success': 'Movie removed from favourite library'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'This movie is already removed from favourite library!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)
