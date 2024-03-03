from django.core.management.base import BaseCommand
from myapp.models import Order
from datetime import datetime

class Command(BaseCommand):
    help = 'Change the order date by order id'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int)
        parser.add_argument('new_date', type=str, help='New date in "YYYY-MM-DD" format')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        new_date_str = kwargs['new_date']
        
        try:
            new_date = datetime.strptime(new_date_str, '%Y-%m-%d').date()  # Преобразование строки в объект date
            order = Order.objects.get(pk=order_id)
            current_datetime = order.date_ordered  # Получение текущей даты и времени заказа
            new_datetime = datetime.combine(new_date, current_datetime.time())  # Создание нового datetime с новой датой и текущим временем

            order.date_ordered = new_datetime  # Установка новой даты заказа
            order.save()  # Сохранение изменений
            self.stdout.write(self.style.SUCCESS(f'Order {order_id} date changed to {new_datetime} successfully'))
        except Order.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Order with id {order_id} does not exist'))
        except ValueError:
            self.stderr.write(self.style.ERROR('Invalid date format, please use "YYYY-MM-DD"'))
