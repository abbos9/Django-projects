from django.urls import path
from pages.views import home_view, message, reservation_view
app_name = 'pages'
urlpatterns = [
    path('', home_view , name='home'),
    path('message/', message, name='message'),
    path('reservation/', reservation_view, name='reservation'),
]