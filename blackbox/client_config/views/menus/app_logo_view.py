from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from blackbox.client_config.models import AppLogo
from blackbox.client_config.serializers.menus.app_logo_serializer import AppLogoSerializer


class AppLogoView(APIView):
    serializer_class = AppLogoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = AppLogo.objects.filter()

    def get(self, request, *args, **kwargs):
        obj = self.queryset.last()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        logo_obj = AppLogo.objects.last()
        if logo_obj is None:
            serializer = self.serializer_class(data=request.data)
        else:
            serializer = self.serializer_class(logo_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
