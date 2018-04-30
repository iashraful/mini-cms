import uuid

from django.db import models

from blackbox.core.models import BaseEntity
from blackbox.discuss.enums.comment_enums import CommentTypeEnum

__author__ = 'Ashraful'


class Comment(BaseEntity):
    uuid = models.UUIDField(unique=True, editable=False)
    text = models.TextField(verbose_name='Comment or Reply')
    status = models.IntegerField(default=CommentTypeEnum.Pending.value)
    replies = models.ManyToManyField('self')

    class Meta:
        app_label = 'discuss'

    def __str__(self):
        return self.text[:10]
