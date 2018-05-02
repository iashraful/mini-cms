from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from drf_role.models import Role

from blackbox.cms.models.configs import AppConfig
from blackbox.core.models import Profile

ROLE_NAMES = ('Developer',)


class Command(BaseCommand):
    def create_role(self):
        for _i, role in enumerate(ROLE_NAMES):
            obj, _created = Role.objects.get_or_create(name=role, type=_i+1)
            if _created:
                print("...Created {0}".format(role))
            else:
                print("...Already Exist.")

    def create_user(self):
        """ Only create an admin user """
        __username = 'admin'
        __password = 'r00t'
        role = Role.objects.first()
        _exists = User.objects.filter(username=__username).exists()
        with transaction.atomic():
            if role and not _exists:
                user = User.objects.create_user(username=__username, password=__password)
                profile = Profile.objects.create(user_id=user.pk, role_id=role.pk)
                print("...Created {0}".format(profile.name))
            else:
                print('...Already Exist.')

    def frontend_app_config(self):
        """ Only Create App Config instance """
        _config = AppConfig.objects.last()
        if not _config:
            config = AppConfig()
            config.app_name = 'MiNi CMS'
            config.save()
            print("AppConfig Added")
        else:
            print("...Already Exist.")

    def handle(self, *args, **options):
        # Create role
        print("Creating Role...")
        self.create_role()
        # Create User
        print("Creating User...")
        self.create_user()
        print("Creating AppConfig...")
        self.frontend_app_config()
