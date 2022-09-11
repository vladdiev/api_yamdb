from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TitleViewSet, GenreViewSet, CategoryViewSet


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')


urlpatterns = [
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
