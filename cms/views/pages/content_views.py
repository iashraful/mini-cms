import uuid

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cms.enums.content_enums import ContentStatusEnum
from cms.models import Content, Page
from cms.serializers.pages.pages_serializers import ContentSerializer

__author__ = 'Ashraful'


class ContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Content.objects.order_by('order')
        if not self.request.user.is_authenticated:
            return queryset.filter(status=ContentStatusEnum.Publish.value)
        return queryset


class ContentCreateView(generics.CreateAPIView):
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        page_slug = serializer.validated_data.pop('page_slug', None)
        instance = serializer.save()
        try:
            _page = Page.objects.get(path=page_slug)
            _page.contents.add(instance)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(data={'message': 'Something went wrong. Please try again'},
                            status=status.HTTP_400_BAD_REQUEST)


class ContentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            uuid.UUID(slug)
            queryset = Content.objects.get(identifier=slug)
            return queryset
        except (ObjectDoesNotExist, ValueError):
            return None
