from audioop import reverse
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# models
from orders.models import OrderItemModel, OrderModel
from pages.models import MenuModel
# Create your views here.

def Proceed_Order(request):
    cart = request.session.get('cart',[])
    if not cart:
        return HttpResponse("Cart is Empty")
    products = MenuModel.get_from_cart(cart)
    order = OrderModel.objects.create(user=request.user, total_amount=0.0)
    total_amount = 0
    for product in products:
        total_amount += float(product.price)
        OrderItemModel.objects.create(order=order, product=product, quantity=1, price=product.price)
    if request.GET.get('total_amount'):
        total_amount = float(request.GET.get('total_amount'))
    order.total_amount = float("{:.2f}".format(total_amount))
    order.save()
    request.session['cart'] = []
    return HttpResponse('Your order has been created',)


@login_required
def add_to_order(request, order_pk):
    cart = request.session.get('cart', [])
    if order_pk in cart:
        cart.remove(order_pk)
    else:
        cart.append(order_pk)
    request.session['cart'] = cart
    print(cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class OrderView(ListView):
    template_name = 'order.html'
    model = MenuModel
    context_object_name = 'orders'


    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        self.request.session['cart'] = cart
        orders = MenuModel.objects.filter(pk__in=cart)
        return orders                   
    
class OrderHistoryView(ListView):
    template_name =  'history.html'
    model = OrderModel
    context_object_name = 'orders'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = OrderModel.objects.filter(user=self.request.user).order_by('-created_at')
        return queryset