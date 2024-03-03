from django.contrib import admin
from .models import Client, Order, Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "address"]
    list_filter = ["name", "registration_date"]
    pass


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "count", "date_added", "photo"]
    # list_filter = ["price", "date_added", "count"]
    readonly_fields = ['date_added']
    
    search_fields = ['description','name']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    
    fieldsets = [
        (
            "Основная информация",
            {
                "classes": ["wide"],
                "fields": ["name",'price'],
            },
        ),
        (
            "Подробности",
            {
                "description": "Категория товара и его подробное описание",
                "fields": [ "description",'count','date_added'],
            },
        ),
    ]

    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "total_price", "date_ordered"]
    readonly_fields = ['total_price']
    list_filter = ["date_ordered"]
    pass
