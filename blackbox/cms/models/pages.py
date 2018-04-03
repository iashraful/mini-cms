import uuid

from django.db import models

from blackbox.cms.enums.content_enums import ContentTypeEnum
from blackbox.core.models import BaseEntity

__author__ = 'Ashraful'


class Page(BaseEntity):
    name = models.CharField(max_length=32, null=True)
    path = models.CharField(max_length=64, default=uuid.uuid4(), unique=True)
    contents = models.ManyToManyField('cms.Content')

    class Meta:
        app_label = 'cms'


class Content(BaseEntity):
    type = models.IntegerField(default=ContentTypeEnum.Table.value)
    identifier = models.CharField(max_length=64, default=uuid.uuid4(), unique=True)
    order = models.IntegerField(default=1)

    class Meta:
        app_label = 'cms'


class ContentData(BaseEntity):
    content = models.ForeignKey('cms.Content', )
