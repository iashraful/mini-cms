from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from drf_role.models import Role

from blackbox.core.models import Profile

ROLE_NAMES = ('Developer',)


class Command(BaseCommand):
    def create_role(self):
        for _i, role in enumerate(ROLE_NAMES):
            Role.objects.create(name=role, type=_i+1)
            print("...Created {0}".format(role))

    def create_user(self):
        """ Only create an admin user """
        __username = 'admin'
        __password = 'r00t'
        role = Role.objects.first()
        with transaction.atomic():
            if role:
                user = User.objects.create_user(username=__username, password=__password)
                profile = Profile.objects.create(user_id=user.pk, role_id=role.pk)
                print("...Created {0}".format(profile.name))

    def handle(self, *args, **options):
        # Create role
        print("Creating Role...")
        self.create_role()
        # Create User
        print("Creating User...")
        self.create_user()
