import uuid

from django.db import models

from blackbox.cms.enums.content_enums import ContentTypeEnum, ContentStatusEnum
from blackbox.core.models import BaseEntity

__author__ = 'Ashraful'


class Page(BaseEntity):
    name = models.CharField(max_length=32)
    path = models.UUIDField(default=uuid.uuid4, editable=False)
    contents = models.ManyToManyField('cms.Content')

    class Meta:
        app_label = 'cms'


class Content(BaseEntity):
    type = models.IntegerField(default=ContentTypeEnum.Plain.value)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    order = models.IntegerField(default=1)
    status = models.IntegerField(default=ContentStatusEnum.Draft.value)
    title = models.CharField(max_length=256)
    body = models.TextField(verbose_name='Content Body', null=True, blank=True)

    class Meta:
        app_label = 'cms'
