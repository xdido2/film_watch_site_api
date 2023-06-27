from django.urls import path

from apps.movies.views.movie import MovieListApiView, MovieDetailApiView
from apps.movies.views.most_liked import MostLikedListApiView

urlpatterns = [
    path('', MovieListApiView.as_view(), name='movies_list'),
    path('detail/<slug:slug>/', MovieDetailApiView.as_view(), name='movies_detail'),
    path('homepage/most_liked', MostLikedListApiView.as_view(), name='most_liked')

]
