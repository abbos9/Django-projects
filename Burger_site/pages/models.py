# import
from django.db import models
from django.utils.translation import gettext_lazy as _
# models

# Create your models here.

class BannerModel(models.Model):
    title = models.CharField(max_length=100)
    headline = models.CharField(max_length = 64)
    country =  models.CharField(max_length=40)
    image = models.ImageField(upload_to='banner/')
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class ContactModel(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class GalleryModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

class TestimonialsModel(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField()
    icon = models.ImageField(upload_to='testimols/icon')
    is_active = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

class MenuModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu/', null=True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name        

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    @staticmethod
    def get_from_cart(cart):
        return MenuModel.objects.filter(pk__in=cart)