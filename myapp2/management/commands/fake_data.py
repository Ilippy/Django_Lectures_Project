from django.core.management.base import BaseCommand
from myapp2.models import Author, Post
from faker import Faker

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **options):
        count = options['count']
        for i in range(1, count + 1):
            author = Author(
                name=fake.name(),
                email=fake.unique.email()
            )
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=fake.sentence(nb_words=10),
                    content=fake.sentence(nb_words=20),
                    author=author
                )
                post.save()