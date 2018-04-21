import uuid

from django.db import models

from blackbox.client_config.enums.menu_enums import MenuAccessTypeEnum
from blackbox.core.models import BaseEntity

__author__ = 'Ashraful'


class MenuGroup(BaseEntity):
    page = models.ForeignKey('cms.Page', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4())
    submenus = models.ManyToManyField('self', blank=True)
    dropdown_items = models.ManyToManyField('self', blank=True)
    auth = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    is_main_menu = models.BooleanField(default=True)
    is_dropdown = models.BooleanField(default=False)

    class Meta:
        app_label = "cms"

    def __str__(self):
        return self.title


class MenuAccessControl(BaseEntity):
    access_type = models.IntegerField(default=MenuAccessTypeEnum.All.value, choices=MenuAccessTypeEnum.choices())
    menu = models.ForeignKey("cms.MenuGroup", null=True, on_delete=models.CASCADE)

    class Meta:
        app_label = "cms"


class AppLogo(BaseEntity):
    logo = models.ImageField(upload_to='')

    class Meta:
        app_label = "cms"
