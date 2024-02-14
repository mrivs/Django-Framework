from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Create Client."

    def handle(self, *args, **kwargs):
        client = Client(
            name="Eva",
            email="eva@example.com",
            phone_number="555-555-636",
            address="Downtown 55-9",
        )
        client.save()
        self.stdout.write(f"{client} created!")
