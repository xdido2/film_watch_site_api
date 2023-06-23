from django.urls import path

from apps.movies.views.favourite import FavouriteCreateDestroyView
from apps.movies.views.history import HistoryCreateView
from apps.movies.views.movie import MovieListApiView, MovieDetailApiView

urlpatterns = [
    path('', MovieListApiView.as_view(), name='movies_list'),
    path('detail/<slug:slug>/', MovieDetailApiView.as_view(), name='movies_detail'),
    path('favourite/', FavouriteCreateDestroyView.as_view(), name='favourite'),
    path('history/', HistoryCreateView.as_view(), name='history'),

]
