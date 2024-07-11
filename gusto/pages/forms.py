from django import forms
from pages.models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['name', 'email', 'message']
