# import
from django import template
from django.db.models import Sum

# models
from pages.models import MenuModel
from orders.models import OrderModel

# register library
register = template.Library()

@register.simple_tag(name='cart_data')
def total_price(request):
    cart = request.session.get('cart', [])
    total,amount = MenuModel.objects.filter(pk__in=cart).aggregate(total_price=Sum('price'))['total_price'], len(cart)
    return "{:.2f}".format(total) if total is not None else 0, amount