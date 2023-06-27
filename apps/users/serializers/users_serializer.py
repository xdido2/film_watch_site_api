from rest_framework.serializers import ModelSerializer

from apps.users.models.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ('id', 'avatar', 'username', 'email',)
