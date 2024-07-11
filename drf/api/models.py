from django.db import models
from rest_framework.validators import UniqueTogetherValidator
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self) -> str:
        return self.name

class BookModel(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, null=True)
    is_active = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.name}: {self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'description'],
                name='unique_title_description'
            )
        ]

class Rating(models.Model):
    book =  models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='rating')
    score =  models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])


    def __str__(self) -> str:
        return self.book.title

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = "Ratings"
        unique_together = ['book', 'score']