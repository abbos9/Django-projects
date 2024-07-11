from django.contrib import admin
from pages.models import (MessageModel, AffordableCategoryModel, CategoryModel, BaseModel,
AffordableModel, ReservationModel)
# Register your models here.

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name','id', 'created_at']
    search_fields = ['name','id']
    ordering = ['-created_at']

@admin.register(BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['category','id', 'created_at']
    search_fields = ['title','id']
    ordering = ['-created_at'] 

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number',]
    order_display =['-create_at']
    search_fields = ['name', 'email', 'number',]


@admin.register(AffordableModel)
class AffordableModelAdmin(admin.ModelAdmin):
    list_display = ['price','id', 'creat_at']
    search_fields = ['price','id']
    ordering = ['-creat_at']

@admin.register(AffordableCategoryModel)
class AffordableCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'creat_at']
    search_fields = ['name','id']
    ordering = ['-creat_at']


@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','state', 'datepicker', 'guest', 'phone']
    search_fields = ['first_name', 'last_name','state', 'datepicker', 'guest']
    ordering = ['-created_at']