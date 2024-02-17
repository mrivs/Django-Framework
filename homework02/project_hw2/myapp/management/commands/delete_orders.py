from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = 'Delete all orders'

    def handle(self, *args, **options):
        Order.objects.all().delete()
        
        self.stdout.write(self.style.ERROR('!!! All orders deleted !!!'))
        
