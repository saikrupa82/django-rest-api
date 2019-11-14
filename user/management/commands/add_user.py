from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add new user'

    def handle(self, *args, **kwargs):
        username = 'mkawsar'
        user = User.objects.create_user(username=username, password='123456', email='admin@admin.com',
                                        first_name='Admin', last_name='Example')
        user.is_superuser = False
        user.is_staff = True
        user.save()
        self.stdout.write('Added new user')
