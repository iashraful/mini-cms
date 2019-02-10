from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from cms.models.configs import AppConfig
from cms.serializers.app_configs.config_serializers import AppConfigSerializer


class AppConfigDetailsView(APIView):
    serializer_class = AppConfigSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        obj = AppConfig.objects.last()
        serializer = self.serializer_class(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AppConfigCreateView(APIView):
    serializer_class = AppConfigSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        _obj = AppConfig.objects.last()
        serializer = self.serializer_class(_obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)