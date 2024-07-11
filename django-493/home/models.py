from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to="news")
    created_at = models.DateTimeField(auto_now_add=True)