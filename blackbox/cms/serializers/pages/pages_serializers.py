from rest_framework import serializers

from blackbox.cms.models import Page, Content

__author__ = 'Ashraful'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = '__all__'
