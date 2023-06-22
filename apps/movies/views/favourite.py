from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.movies.models import Favourite


class FavouriteView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user_id = request.data['user']
            if not Favourite.objects.filter(movie_id=movie_id, user_id=user_id).exists():
                favourite = Favourite.objects.create(user_id=request.data['user'], movie_id=request.data['movie'])
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
                return Response({'success': 'Movie removed from favourite library'}, status=status.HTTP_201_CREATED)
            return Response({'error': 'This movie is already removed from favourite library!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)
