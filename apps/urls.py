from django.urls import path, include

urlpatterns = [
    path('movie/', include('apps.movies.urls')),
    path('users/', include('apps.users.urls')),
    path('user_auth/', include('apps.user_auth.urls'))

]
