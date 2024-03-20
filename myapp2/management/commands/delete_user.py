from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Delete user by <id>."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options['pk']
        user = User.objects.filter(pk=pk).first()
        if user:
            user.delete()
            self.stdout.write(f"Пользователь с id = {pk} был удален")
        else:
            self.stdout.write(f"Пользователь c id = {pk} не найден")
