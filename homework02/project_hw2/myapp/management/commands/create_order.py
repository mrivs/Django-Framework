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
        # parser.add_argument('products_list', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        # products_list = kwargs['products_list']

        client = Client.objects.get(pk=client_id)
        order = Order.objects.create(client=client, total_price=0)
        products = Product.objects.all()
        total_price = 0
<<<<<<< HEAD
        for product_id in range(5):
            
=======
        for product_id in range(10):
>>>>>>> 241f2c3a5c327fb9253da92f4ca94573e05b9f40
            product = choice(products)
            order.products.add(product)
            total_price += product.price
            
            # product = Product.objects.get(pk=product_id)
            # order.products.add(product)
            # total_price += product.price

        order.total_price = total_price
        order.save()
        
        self.stdout.write(self.style.SUCCESS(f'Order {order} created successfully'))
