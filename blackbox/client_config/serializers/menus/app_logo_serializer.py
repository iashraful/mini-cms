from rest_framework import serializers

from blackbox.client_config.models import AppLogo


class AppLogoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('logo', 'updated_at')
        model = AppLogo
