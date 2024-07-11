from django.urls import path
from .views import index, registration,news_list,news_detail



urlpatterns = [
    path('welcome/', index),
    path('forms/', registration),
    path('news/',news_list),
    path('news/<int:pk>',news_detail)
]