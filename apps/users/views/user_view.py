from rest_framework import status
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response

from apps.users.models.user import User
from apps.users.serializers.users_serializer import UserSerializer


class UserViewSet(ListAPIView, UpdateAPIView):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, JSONParser,)

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'success': 'Profile info was edited successfully!'}, status=status.HTTP_202_ACCEPTED)
