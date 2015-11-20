__author__ = 'eveR'

from django.conf.urls import patterns, url, include
from rest_framework import routers
from digitalizame.apps.companies.views import TypesViewSet, CompaniesViewSet

router = routers.DefaultRouter()
router.register(r'types', TypesViewSet)
router.register(r'companies', CompaniesViewSet)

urlpatterns = patterns('digitalizame.apps.api',
                       url(r'^', include(router.urls)),
                       )