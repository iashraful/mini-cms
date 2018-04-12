from rest_framework import generics
from rest_framework.permissions import AllowAny

from blackbox.cms.enums.content_enums import ContentStatusEnum
from blackbox.cms.models import Content
from blackbox.cms.serializers.pages.pages_serializers import ContentSerializer

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
