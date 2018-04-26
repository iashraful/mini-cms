import uuid

from django.db import models
from django.db.models import Max

from blackbox.cms.enums.content_enums import ContentTypeEnum, ContentStatusEnum
from blackbox.core.models import BaseEntity

__author__ = 'Ashraful'


class Page(BaseEntity):
    order = models.IntegerField(default=1)
    name = models.CharField(max_length=32)
    path = models.UUIDField(default=uuid.uuid4, editable=False)
    contents = models.ManyToManyField('cms.Content')

    class Meta:
        app_label = 'cms'

    def __str__(self):
        return "({0}) {1}".format(self.order, self.name)

    @classmethod
    def get_max_order(cls):
        _max_order = cls.objects.aggregate(Max('order'))['order__max']
        if _max_order is not None:
            return _max_order
        return 1


class Content(BaseEntity):
    type = models.IntegerField(default=ContentTypeEnum.Plain.value)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    order = models.IntegerField(default=1)
    status = models.IntegerField(default=ContentStatusEnum.Draft.value)
    title = models.CharField(max_length=256)
    body = models.TextField(verbose_name='Content Body', null=True, blank=True)

    class Meta:
        app_label = 'cms'

    def __str__(self):
        return self.title
