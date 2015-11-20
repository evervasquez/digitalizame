__author__ = 'eveR'

from rest_framework import authentication, permissions, filters


# to available when were permissions

class DefaultViewSetMixin(object):
    # authentication_classes= (
    #     authentication.BaseAuthentication,
    #     authentication.TokenAuthentication,
    # )
    # permissions_classes = (
    #     permissions.IsAuthenticated,
    # )
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
    paginate_by = 50
    paginate_by_param = 'page_size'
    max_paginate_by = 100
