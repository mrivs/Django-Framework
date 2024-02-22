from django.core.management.base import BaseCommand
from myapp.models import Client
import random

class Command(BaseCommand):
    help = "Create Client ."
    
    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Client name")
        
    def handle(self, *args, **kwargs):
        client = Client(
            name=kwargs.get("name"),
            email=f"{kwargs.get('name')}@example.com",
            phone_number=f"555-555-{random.randint(100,999)}",
            address=f"Downtown {random.randint(1,99)}-{random.randint(1,99)}",
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f"{client} created!"))
