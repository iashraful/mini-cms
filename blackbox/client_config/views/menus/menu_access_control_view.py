from rest_framework.generics import ListCreateAPIView

from blackbox.client_config.models import MenuAccessControl
from blackbox.client_config.serializers.menus.menu_access_control_serializers import MenuAccessControlSerializer

__author__ = 'Ashraful'


class MenuAccessControlView(ListCreateAPIView):
    serializer_class = MenuAccessControlSerializer
    queryset = MenuAccessControl.objects.filter()
