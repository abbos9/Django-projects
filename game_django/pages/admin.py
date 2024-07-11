from django.contrib import admin
from pages.models import GameModel
# Register your models here.

@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'link', 'created_at')
    search_fields = ('id','title', 'link')
    list_filter = ('id','title', 'created_at')
    ordering = ['-created_at']