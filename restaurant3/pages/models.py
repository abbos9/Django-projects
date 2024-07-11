from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    
    created_at  = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BaseModel(models.Model):
    title = models.CharField(max_length=100)
    icons = models.ImageField(upload_to='icons')
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    images = models.ImageField(upload_to='images')
    description = models.TextField()

    created_at  = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = 'base'
        verbose_name_plural = 'Bases'


class MessageModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='message'
        verbose_name_plural = 'messages'

class AffordableCategoryModel(models.Model):
    name = models.CharField(max_length=50)

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'affordable_category'
        verbose_name_plural = 'affordable_categories'

class AffordableModel(models.Model):
    image = models.ImageField(upload_to='affordable')
    price = models.IntegerField(default=5)
    category = models.ManyToManyField(AffordableCategoryModel)

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.price} - {', '.join(category.name for category in self.category.all())}"
    
    class Meta:
        verbose_name = 'affordable'
        verbose_name_plural = 'affordables'


class ReservationModel(models.Model):
   first_name = models.CharField(max_length=100)
   last_name =models.CharField(max_length=100)
   state =models.CharField(max_length=100)
   datepicker =models.DateField()
   phone =models.CharField(max_length=15)
   guest =models.IntegerField(default=1)
   email =models.EmailField( max_length=100)
   subject =models.CharField(max_length=200)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   class Meta:
        verbose_name ='reservation'
        verbose_name_plural ='reservations'