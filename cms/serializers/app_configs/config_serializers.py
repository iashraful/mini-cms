from rest_framework.serializers import ModelSerializer

from cms.models.configs import AppConfig


class AppConfigSerializer(ModelSerializer):
    class Meta:
        model = AppConfig
        fields = ('id', 'app_name', 'footer', 'hide_footer', 'browser_title')
