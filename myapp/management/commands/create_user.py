from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name="John", email="john@example.com", password="secret", age=25)
        user.save()
        self.stdout.write(f"{user}")
        user = User(name="Neo", email="neo@example.com", password="mrAnderson", age=58)
        user.save()
        self.stdout.write(f"{user}")
        user = User(name="Morpheus", email="morpheus@example.com", password="InNeoWeTrust", age=60)
        user.save()
        self.stdout.write(f"{user}")
