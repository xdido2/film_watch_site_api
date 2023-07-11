from rest_framework.generics import ListAPIView

from apps.movies.models import Movie
from apps.movies.serializers.movie_serializer import MovieSerializer
from apps.movies.paginations import MoviePagination


class MostLikedListApiView(ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = MoviePagination

    def get_queryset(self):
        return Movie.objects.order_by('-favourites_count')