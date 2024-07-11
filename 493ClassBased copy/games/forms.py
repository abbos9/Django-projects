from django import forms

from games.models import GamesModel


class GamesModelForm(forms.ModelForm):
    class Meta:
        model = GamesModel
        fields = ['name', 'description', 'link']