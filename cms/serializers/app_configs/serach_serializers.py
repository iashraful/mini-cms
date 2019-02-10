from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from cms.models import Content

__author__ = 'Ashraful'


class SearchSerializer(ModelSerializer):
    type = SerializerMethodField(read_only=True)
    path_to_go = SerializerMethodField(read_only=True)

    class Meta:
        model = Content
        fields = ('title', 'identifier', 'type', 'path_to_go')

    def get_type(self, obj):
        return obj.__class__.__name__

    def get_path_to_go(self, obj):
        return "/c/{0}".format(obj.identifier)
