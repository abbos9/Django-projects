from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class InstragramModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instagram/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instragram'
        verbose_name_plural = 'Instragrams'


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name =  'Category'
        verbose_name_plural = 'Categories'

class TagsModel(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name =  'Tag'
        verbose_name_plural = 'Tags'

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author/icon')
    info = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name =  'Author'
        verbose_name_plural = 'Authors'


class PostModel(models.Model):
    headline = models.CharField(max_length=200)
    tags = models.ManyToManyField(TagsModel)
    description = models.TextField()
    short_description = models.TextField()
    phrase = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/images', null=True, blank=True)
    visitor_count = models.IntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline
    
    def get_next(self):
        return self.get_next_by_created_at()
    
    def get_previous(self):
        return self.get_previous_by_created_at()
    
    def is_new(self):   
        curently= timezone.now()
        difference = (curently - self.created_at)
        if difference.days <= 3:
            return  True
        else:
            return    False
        
    class Meta:
        verbose_name =  'Post'
        verbose_name_plural = 'Posts'



class CommentModel(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=50,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.SlugField(null=True, blank=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name =  'Comment'
        verbose_name_plural = 'Comments'


class LikedModel(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='liked')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name =  'Like'
        verbose_name_plural = 'Likes'
        unique_together = ['user', 'post']
