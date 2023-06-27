from django.urls import path

from apps.users.views.user_view import UserViewSet
from apps.users.views.favourite import FavouriteCreateDestroyView
from apps.users.views.history import HistoryCreateView

urlpatterns = [
    path('user-profile/', UserViewSet.as_view(), name='user'),
    path('favourite/', FavouriteCreateDestroyView.as_view(), name='favourite'),
    path('history/', HistoryCreateView.as_view(), name='history'),
]
