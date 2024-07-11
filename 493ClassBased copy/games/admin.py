from django.contrib import admin

from games.models import GamesModel


@admin.register(GamesModel)
class GamesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)