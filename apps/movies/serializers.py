from rest_framework.serializers import ModelSerializer

from apps.movies.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
