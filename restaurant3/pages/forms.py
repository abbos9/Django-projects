from django import forms
from .models import MessageModel, ReservationModel
class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ('name', 'email', 'number','message',)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['first_name', 'last_name', 'state', 'datepicker', 'phone', 'guest', 'email', 'subject']
