from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ('id', 'avatar', 'username', 'email',)
