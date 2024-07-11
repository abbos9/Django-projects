from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    date_of_birth = models.DateField()
       
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Genre(models.Model):
    title = models.CharField(max_length=24)
    icon = models.ImageField(upload_to='icons')
   
    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='books',null=True)
    page_size = models.IntegerField()
    price = models.IntegerField()
    published = models.CharField(max_length=14)
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(to=Genre)
   
    def __str__(self):
        return self.title


class Currency(models.Model):
    nbu_buy_price = models.CharField(max_length=255)
    nbu_cell_price = models.CharField(max_length=255)
    title = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        