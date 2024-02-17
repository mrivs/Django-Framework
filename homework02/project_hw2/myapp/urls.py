from django.urls import path
from .import views

urlpatterns = [
 path('', views.main, name='main'),
 path('client_orders/<int:client_id>/', views.client_orders,
name='client_orders'),
 path('order_full/<int:order_id>/', views.order_full, name='order_full'),
 
]