from django.db import models

# Create your models here.

class MessageModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'


class SpecialsModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='special'
        verbose_name_plural = 'specials'

class CategoryModel(models.Model):
    title = models.CharField(max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class MenuModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='menu'
        verbose_name_plural ='menus'
        
