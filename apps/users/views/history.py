from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models.history import History
from apps.users.serializers.history_serializer import HistorySerializer


class HistoryCreateView(ListCreateAPIView):
    serializer_class = HistorySerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return History.objects.filter(user_id=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user = request.user
            if not History.objects.filter(user_id=user.pk, movie_id=movie_id).exists():
                history = History.objects.create(user_id=user.pk, movie_id=movie_id)
                history.save()
                return Response({'success': 'Movie is added to your history library!'}, status=status.HTTP_201_CREATED)
            History.objects.filter(user_id=user.pk, movie_id=movie_id).delete()
            history = History.objects.create(user_id=user.pk, movie_id=movie_id)
            history.save()
            return Response({'success': 'Movie is added to your history library!'}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)
