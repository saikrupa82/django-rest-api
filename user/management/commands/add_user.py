from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add new user'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        username = 'mkawsar'
        user = User.objects.create_user(username=username, password='123456', email='admin@admin.com',
                                        first_name='Admin', last_name='Example', is_superuser=True, is_staff=False)
        user.save()
        for i in range(5):
            fake = Faker()
            name = fake.first_name()
            user = User.objects.create_user(username=name.lower(), password='123456', email=fake.email(),
                                            first_name=name, last_name=fake.last_name(), is_superuser=False,
                                            is_staff=False)
            user.save()
        self.stdout.write('Added new user')
