from rest_framework import serializers

from blackbox.client_config.models import MenuGroup

__author__ = 'Ashraful'


class MenuGroupBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroup
        fields = (
            'id', 'name', 'path', 'identifier', 'auth', 'is_dropdown',
            'is_hidden', 'is_main_menu', 'created_at', 'updated_at'
        )


class MenuGroupSerializer(MenuGroupBaseSerializer):
    submenus = MenuGroupBaseSerializer(many=True, read_only=True)
    dropdown_items = MenuGroupBaseSerializer(many=True, read_only=True)

    class Meta(MenuGroupBaseSerializer.Meta):
        fields = MenuGroupBaseSerializer.Meta.fields + ('submenus', 'dropdown_items')
