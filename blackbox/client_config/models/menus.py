from django.db import models

from blackbox.client_config.enums.menu_enums import MenuAccessTypeEnum
from blackbox.core.models import BaseEntity

__author__ = 'Ashraful'


class MenuGroup(BaseEntity):
    name = models.CharField(max_length=32)
    path = models.CharField(max_length=64)
    identifier = models.CharField(max_length=64, unique=True)
    submenus = models.ManyToManyField('self', blank=True)
    dropdown_items = models.ManyToManyField('self', blank=True)
    is_dropdown = models.BooleanField(default=False)
    auth = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    is_main_menu = models.BooleanField(default=True)

    class Meta:
        app_label = "client_config"


class MenuAccessControl(BaseEntity):
    access_type = models.IntegerField(default=MenuAccessTypeEnum.All.value, choices=MenuAccessTypeEnum.choices())
    menu = models.ForeignKey("client_config.MenuGroup", null=True, on_delete=models.CASCADE)

    class Meta:
        app_label = "client_config"


class AppLogo(BaseEntity):
    logo = models.ImageField(upload_to='')

    class Meta:
        app_label = "client_config"
