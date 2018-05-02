from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from blackbox.cms.enums.content_enums import ContentStatusEnum
from blackbox.cms.models import Content
from blackbox.cms.serializers.app_configs.serach_serializers import SearchSerializer

__author__ = 'Ashraful'


class SearchListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SearchSerializer

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is None:
            return None
        _user = self.request.user.is_authenticated
        # This is basic searching for now. Will change it later.
        queryset = Content.objects.filter(title__icontains=q)
        if not _user:
            queryset = queryset.filter(status=ContentStatusEnum.Publish.value)
        return queryset
