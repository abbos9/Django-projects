from django.forms import ModelForm
# models
from pages.models import ContactModel

class contactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['message', 'name', 'email', 'subject']
