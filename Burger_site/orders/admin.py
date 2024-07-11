from django.contrib import admin

from orders.models import OrderItemModel, OrderModel

# Register your models here.


admin.site.register(OrderItemModel)
admin.site.register(OrderModel)