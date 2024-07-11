from django.urls import path
from orders.views import OrderView, add_to_order, Proceed_Order, OrderHistoryView

app_name = 'orders'

urlpatterns = [
    path('<int:order_pk>/order/', add_to_order, name='order'),
    path('order/', OrderView.as_view(), name='orders'),
    path("prooced_order/", Proceed_Order, name = 'prooced_order'),
    path('history/', OrderHistoryView.as_view(), name='history'),
]