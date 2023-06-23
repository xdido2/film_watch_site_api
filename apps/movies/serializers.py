from rest_framework.serializers import ModelSerializer

from apps.movies.models import Favourite
from apps.movies.models import History
from apps.movies.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class FavouriteSerializer(ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Favourite
        fields = 'movie',
        # depth = 1


class HistorySerializer(ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = History
        fields = 'movie',
