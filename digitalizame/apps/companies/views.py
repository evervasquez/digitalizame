
# Create your views here.

from rest_framework import viewsets
from digitalizame.apps.api.mixins import DefaultViewSetMixin
from .serializers import TypesSerializer, CompaniesSerializer
from .models import Type, Companies

# Create your views here.

class TypesViewSet(DefaultViewSetMixin, viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer
    search_fields = ('description',)
    ordering_fields = '__all__'

class CompaniesViewSet(DefaultViewSetMixin, viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    search_fields = ('name', 'description', 'latitude', 'longitude', 'tags', 'is_activate', 'type_id')
    ordering_fields = '__all__'
