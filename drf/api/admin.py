from django.contrib import admin
from api.models import Author, BookModel, Rating
# Register your models here.


admin.site.register(Author)
admin.site.register(BookModel)
admin.site.register(Rating)