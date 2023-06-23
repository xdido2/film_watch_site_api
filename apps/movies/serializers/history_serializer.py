from rest_framework.serializers import ModelSerializer

from apps.movies.models import History
from apps.movies.serializers.movie_serializer import MovieSerializer


class HistorySerializer(ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = History
        fields = 'movie',
