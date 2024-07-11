from django.urls import path
from books.views import (book_list,book_details,
                         book_delate, get_currency,
                         form_data,
                         update_book,get_weather)


   
urlpatterns = [
    path('list/',book_list),
    path('add/', form_data, name='form_data'),
    path("detail/<int:pk>",book_details),
    path('<int:pk>/delete/',book_delate),
    path('<int:pk>/update/',update_book),
    path('weather/', get_weather),
    path('currency/', get_currency),
]



