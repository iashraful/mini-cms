from django.db import models

from blackbox.core.models.base import BaseEntity


class AppConfig(BaseEntity):
    app_name = models.CharField(max_length=32, default='MiNi CMS')
    footer = models.TextField(verbose_name='App Footer', null=True)

    class Meta:
        app_label = 'cms'

    def __str__(self):
        return self.app_name
