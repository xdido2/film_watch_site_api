from rest_framework.serializers import ModelSerializer

from apps.movies.models import Favourite
from apps.movies.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
