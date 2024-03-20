from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get users with age greater than <age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **options):
        age = options['age']
        users = User.objects.filter(age__gt=age)
        if users:
            for user in users:
                self.stdout.write(f"{user}")
        else:
            self.stdout.write(f"Пользователей старше {age} лет не найдено")
