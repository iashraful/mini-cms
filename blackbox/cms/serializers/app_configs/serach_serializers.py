from rest_framework.serializers import ModelSerializer

from blackbox.cms.models import Content

__author__ = 'Ashraful'


class SearchSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'identifier')
