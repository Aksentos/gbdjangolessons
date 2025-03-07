from django.core.management.base import BaseCommand
from myapp.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            intro = f"All posts of {author.name}\n"
            text = "\n".join(post.get_summary() for post in posts)
            self.stdout.write(f"{intro}{text}")
