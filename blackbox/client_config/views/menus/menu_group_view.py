from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blackbox.client_config.models import MenuGroup
from blackbox.client_config.serializers.menus.menu_group_serializers import MenuGroupSerializer

__author__ = 'Ashraful'


class MenuGroupView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MenuGroupSerializer
    queryset = MenuGroup.objects.filter(is_main_menu=True)

    def post(self, request, *args, **kwargs):
        menus = request.data
        api_response = {
            "success": True,
            "message": "Request process successfully."
        }
        for _menu in menus:
            _identifier = _menu.get('identifier')
            menu_obj = MenuGroup.objects.none()
            if _identifier:
                menu_obj = MenuGroup.objects.filter(identifier__iexact=_identifier).last()
            if menu_obj:
                _serializer = self.serializer_class(menu_obj, data=_menu)
            else:
                _serializer = self.serializer_class(data=_menu)
            if _serializer.is_valid(raise_exception=True):
                menu = _serializer.save()
                # Check for submenus
                _sub_menus = _menu.get('submenus')
                if _sub_menus:
                    for _sub_menu in _sub_menus:
                        _sub_identifier = _sub_menu.get('identifier')
                        sub_menu_obj = MenuGroup.objects.none()
                        if _sub_identifier:
                            sub_menu_obj = MenuGroup.objects.filter(identifier__iexact=_sub_identifier).last()
                        if sub_menu_obj:
                            _sub_serializer = self.serializer_class(sub_menu_obj, data=_sub_menu)
                        else:
                            _sub_serializer = self.serializer_class(data=_sub_menu)
                        if _sub_serializer.is_valid(raise_exception=True):
                            sub_menu_instance = _sub_serializer.save()
                            menu.submenus.add(sub_menu_instance)
                # Check for Dropdown items
                _dropdown_menus = _menu.get('dropdown_items')
                if _dropdown_menus:
                    for _dropdown_menu in _dropdown_menus:
                        _drop_identifier = _dropdown_menu.get('identifier')
                        drop_menu_obj = MenuGroup.objects.none()
                        if _drop_identifier:
                            drop_menu_obj = MenuGroup.objects.filter(identifier__iexact=_drop_identifier).last()
                        if drop_menu_obj:
                            _drop_serializer = self.serializer_class(drop_menu_obj, data=_dropdown_menu)
                        else:
                            _drop_serializer = self.serializer_class(data=_dropdown_menu)
                        if _drop_serializer.is_valid(raise_exception=True):
                            dropdown_instance = _drop_serializer.save()
                            menu.dropdown_items.add(dropdown_instance)
            else:
                api_response = {
                    "success": False,
                    "message": "Request does not process successfully."
                }
        return Response(data=api_response)
