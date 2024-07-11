from django.urls import path
from pages.views import home_pages_view, message_view


app_name = 'pages'

urlpatterns = [
    path('',home_pages_view, name='home'),
    path('message/', message_view, name='message'),
]