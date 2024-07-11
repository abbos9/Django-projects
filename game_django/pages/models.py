from django.db import models
from django import forms
# Create your models here.

class  GameModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


class GameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'description', 'link']        