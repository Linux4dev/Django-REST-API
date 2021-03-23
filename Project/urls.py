from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from App.API.viewsets import BookViewSet

route = routers.DefaultRouter()
route.register('book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
