from django.urls import path

from apps.movies.views.movie import MovieListApiView, MovieDetailApiView

urlpatterns = [
    path('', MovieListApiView.as_view(), name='movies_list'),
    path('detail/<slug:slug>/', MovieDetailApiView.as_view(), name='movies_detail'),
]
