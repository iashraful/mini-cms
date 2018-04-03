from rest_framework import serializers

from blackbox.client_config.models import MenuAccessControl

__author__ = 'Ashraful'


class MenuAccessControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuAccessControl
        fields = '__all__'
