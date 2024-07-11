from django import forms
from pages.models import GameModel

class GameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'description', 'link']