from django.contrib import admin
from books.models import Book, Author,Genre, Currency
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('nbu_buy_price', 'nbu_cell_price', 'title', 'create_at', 'update_at')
    list_filter = ('nbu_buy_price', 'nbu_cell_price')
    search_fields = ('nbu_buy_price', 'nbu_cell_price', 'title')   
