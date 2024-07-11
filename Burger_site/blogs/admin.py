from django.contrib import admin

from blogs.models import AuthorModel, CategoryModel, CommentModel, InstragramModel, LikedModel, PostModel, TagsModel

# Register your models here.

@admin.register(InstragramModel)
class InstragramModelAdmin(admin.ModelAdmin):
    ordering =['-created_at']
    search_fields = ['name', 'created_at', 'updated_at']
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'image', 'info', 'created_at', 'updated_at']

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['headline', 'description', 'short_description', 'phrase', 'category', 'author', 'created_at', 'updated_at']

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment', 'post', 'created_at', 'updated_at']

@admin.register(LikedModel)
class LikedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']