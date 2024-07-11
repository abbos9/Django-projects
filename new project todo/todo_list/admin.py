from django.contrib import admin
from todo_list.models import Category, TodoList
# Register your models here.

admin.site.register(Category)
admin.site.register(TodoList)
