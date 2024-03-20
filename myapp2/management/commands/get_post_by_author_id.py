from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get Posts by Author id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options['pk']
        author = Author.objects.filter(pk=pk).first()
        if author:
            posts = Post.objects.filter(author=author)
            intro = f"All posts of {author.name}\n"
            text = '\n'.join(post.content for post in posts)
            self.stdout.write(f"{intro}{text}")
        else:
            self.stdout.write(f"Пользователь с id = {pk} не найден")
