import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models

from blackbox.core.models.base import BaseEntity
from django.conf import settings

__author__ = 'Ashraful'


class Settings(BaseEntity):
    email_notification = models.BooleanField(default=False, verbose_name="Email Notification")
    web_notification = models.BooleanField(default=False, verbose_name="Web Notification")

    def __str__(self):
        return "{0}".format("Settings")  # TODO will update this later


class Confirmation(BaseEntity):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    token = models.UUIDField(unique=True, default=uuid.uuid4)
    verified = models.BooleanField(default=False)

    @classmethod
    def send_email(cls, user_id=None):
        object = cls.objects.create(user_id=user_id)

        html_mgs = """
            <h2 style="text-align: center">Welcome to My Project</h2>
            <p style="text-align: center">
                Please copy the token from  below and put the token in desired place to complete your registration.<br/>
                {token}
            </p>
        """.format(token=object.token)

        status = send_mail(
            subject="User Registration Confirmation Email",
            message="",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[object.user.email],
            fail_silently=False,
            html_message=html_mgs
        )
        if status == 1:
            return True
        return False
