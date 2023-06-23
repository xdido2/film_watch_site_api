from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.movies.models import Movie
from apps.movies.paginations import MoviePagination
from apps.movies.serializers.movie_serializer import MovieSerializer


class MovieListApiView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    permission_classes = IsAuthenticatedOrReadOnly,


class MovieDetailApiView(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = IsAuthenticatedOrReadOnly,

    def get_queryset(self):
        slug = self.kwargs['slug']
        response = get_object_or_404(Movie, slug_link=slug)
        response.view_count += 1
        response.save()
        return Movie.objects.filter(slug_link=slug)
