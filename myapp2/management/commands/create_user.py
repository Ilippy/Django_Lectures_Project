from django.core.management.base import BaseCommand
from myapp2.models import User
from faker import Faker
from random import randint

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        user = User(name=fake.name(), email=fake.unique.email(), password=fake.password(), age=randint(15, 60))
        user.save()
        self.stdout.write(f"{user}")
