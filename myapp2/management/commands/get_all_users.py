from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **options):
        users = User.objects.all()
        if users:
            for user in users:
                self.stdout.write(f"{user}")
        else:
            self.stdout.write("Пользователей не найдено")

