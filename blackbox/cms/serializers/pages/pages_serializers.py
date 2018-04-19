from rest_framework import serializers

from blackbox.cms.enums.content_enums import ContentStatusEnum
from blackbox.cms.models import Page, Content

__author__ = 'Ashraful'


class ContentSerializer(serializers.ModelSerializer):
    page_slug = serializers.UUIDField(write_only=True)

    class Meta:
        model = Content
        fields = ('identifier', 'status', 'order', 'title', 'body', 'page_slug')


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('name', 'path',)
        lookup_field = 'path'


class PageDetailsSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Page
        fields = ('name', 'path', 'contents')
        lookup_field = 'path'

    def get_contents(self, obj):
        contents = obj.contents.order_by('-updated_at')
        _request = self.context.get('request')
        if _request and not _request.user.is_authenticated:
            contents = contents.filter(status=ContentStatusEnum.Publish.value)
        data = ContentSerializer(contents, many=True)
        return data.data
