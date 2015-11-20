__author__ = 'eveR'

from rest_framework import serializers
from .models import Type, Companies

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'description', 'icon')


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('id', 'name', 'description', 'latitude', 'longitude', 'tags',
                  'slug', 'is_activate', 'picture', 'type')
