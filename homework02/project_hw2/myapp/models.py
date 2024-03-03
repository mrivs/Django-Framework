from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# Create your models here.
'''
Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

'''

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name},  email: {self.email}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField( null=True, blank=True)
    
    def __str__(self):
        return f'{self.name.upper()}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.client} on {self.total_price}"

        
@receiver(m2m_changed, sender=Order.products.through)
def update_total_price(sender, instance, action, **kwargs):
        if action in ['post_add', 'post_remove', 'post_clear']:
            instance.total_price = instance.products.aggregate(total_price=models.Sum('price'))['total_price'] or 0
            instance.save()