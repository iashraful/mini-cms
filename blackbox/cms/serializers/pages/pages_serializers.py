from rest_framework import serializers

from blackbox.cms.models import Page, Content

__author__ = 'Ashraful'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    def validate(self, attrs):
        path = attrs.get('path')
        if path and path[0] != '/':
            path = '/' + path
            attrs['path'] = path
            return attrs
        return attrs

    class Meta:
        model = Page
        fields = '__all__'
        lookup_field = 'path'
