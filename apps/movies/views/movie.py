from rest_framework.generics import ListAPIView

from apps.movies.models import Movie
from apps.movies.paginations import MoviePagination
from apps.movies.serializers import MovieSerializer


class MovieListApiView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination


class MovieDetailApiView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Movie.objects.filter(slug_link=slug)
