from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from random import choice

class Command(BaseCommand):
    help = """
    Create order for a client with multiple products : 
    python manage.py create_order <client_id>  ...
    
    """
    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
       
    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        client = Client.objects.get(pk=client_id)
        order = Order.objects.create(client=client, total_price=0)
        products = Product.objects.all()
        total_price = 0
        for _ in range(5):  
            product = choice(products)
            if product not in order.products.all():
                order.products.add(product)
                total_price += product.price
                print(product)
        order.total_price = total_price
        order.save()
        self.stdout.write(self.style.SUCCESS(f'Order {order} created successfully'))

