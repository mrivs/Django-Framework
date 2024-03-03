from django.core.management.base import BaseCommand
from myapp.models import Product
import random
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create 5 Products."

    def handle(self, *args, **kwargs):
        
        for i in range (5):
            product = Product(
                name = f'Unit {random.choice(lorem_ipsum.WORDS)}',
                description = "\n".join(lorem_ipsum.paragraphs(2,common=False)),
                price = random.randint(100,1000),
                count = random.randint(6,10),
            )
            product.save()
            self.stdout.write(f"{product} created!")