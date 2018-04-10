from rest_framework import generics

from blackbox.cms.models import Page
from blackbox.cms.serializers.pages.pages_serializers import PageSerializer

__author__ = 'Ashraful'


class PageListView(generics.ListCreateAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.filter()
