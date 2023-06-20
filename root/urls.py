from django.contrib import admin
from django.urls import path, include

from root.swagger import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/v1/movie/', include('apps.movies.urls')),
    path('api/v1/user/', include('apps.users.urls')),

]
