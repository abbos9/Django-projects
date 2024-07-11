from django.urls import path
from .views import news_list,news_detail


urlpatterns = [
    path('new/', news_list),
     path('news/<int:pk>',news_detail)
]
