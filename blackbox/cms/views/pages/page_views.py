from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import AllowAny

from blackbox.cms.models import Page
from blackbox.cms.serializers.pages.pages_serializers import PageSerializer

__author__ = 'Ashraful'


class PageListView(generics.ListCreateAPIView):
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    queryset = Page.objects.filter()


class PageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            _obj = Page.objects.get(path=slug)
            return _obj
        except ObjectDoesNotExist:
            pass
