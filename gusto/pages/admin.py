from django.contrib import admin
from pages.models import MessageModel, MenuModel, CategoryModel, SpecialsModel

# Register your models here.


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','created_at']
    search_fields = ['name', 'email','id']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']
    

@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['title','price','description','id']
    search_fields = ['name','price','description','id']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
  list_display = ['title']
  search_fields = ['title', 'id']
  list_filter = ['created_at','updated_at']
  ordering = ['-created_at']


@admin.register(SpecialsModel)
class SpecialsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title', 'id']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']


    