from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user with specific id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options['pk']
        # user = User.objects.get(id=id_)
        user = User.objects.filter(pk=pk).first()
        if user:
            self.stdout.write(f"{user}")
        else:
            self.stdout.write(f"Пользователь не найден с id = {pk}")
