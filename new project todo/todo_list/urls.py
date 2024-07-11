from django.urls import path
from todo_list.views import base

urlpatterns = [
    path('todo/', base),
]