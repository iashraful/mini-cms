from rest_framework.serializers import ModelSerializer

from blackbox.cms.models.configs import AppConfig


class AppConfigSerializer(ModelSerializer):
    class Meta:
        model = AppConfig
        fields = ('id', 'app_name', 'footer')
