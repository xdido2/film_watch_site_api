from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.users.models import User
from apps.users.serializers.users_serializer import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

