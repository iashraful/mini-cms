from django.contrib.auth.models import User
from django.db import models
from drf_role.models import Role

from blackbox.core.helpers.enums import GenderEnum
from blackbox.core.models.base import BaseEntity


class Profile(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='documents/%Y/%m/', null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(verbose_name="Birth Date", null=True)
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=16)
    mobile = models.CharField(max_length=16, unique=True, null=True, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        try:
            return "{0} {1}".format(
                self.user.first_name, self.user.last_name
            ) if (self.user.first_name or self.user.last_name) is None else self.user.username
        except AttributeError:
            return 'N/A'
