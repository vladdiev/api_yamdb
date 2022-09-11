from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from .permissions import AdminOrReadOnly


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """Viewset for creating viewset models of Genre, Category."""
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
