from django.core.management.base import BaseCommand
from myapp.models import Author, Post


class Command(BaseCommand):
    help = "Delete fake authors ans posts."

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        posts = Post.objects.all()
        authors.delete()
        posts.delete()
        self.stdout.write("Fakes are deleted")
