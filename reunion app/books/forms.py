from django import forms
from books.models import Book

class homework(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('created_at',)



