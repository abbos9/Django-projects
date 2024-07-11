from django.contrib import admin

# models
from pages.models import (ContactModel, GalleryModel, BannerModel,
TestimonialsModel, MenuModel)
# Register your models here.


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['name', 'email']
    list_display = ['name', 'email', 'created_at', 'updated_at']

@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['name', 'created_at', 'updated_at']
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['title', 'created_at', 'updated_at']
    list_display = ['title', 'created_at', 'updated_at', 'is_active']
    list_editable = ['is_active']


@admin.register(TestimonialsModel)
class TestimonialsModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['name', 'created_at', 'updated_at']
    list_display = ['name', 'created_at', 'updated_at','is_active']
    list_editable = ['is_active']

@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['name', 'created_at', 'updated_at']
    list_display = ['name', 'created_at', 'updated_at']
