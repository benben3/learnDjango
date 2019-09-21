
from django import forms
from django.forms import ModelForm
from .models import Contact

# class ContactForm(forms.Form):
    # yourname = forms.CharField(max_length=100, label='Your Name')
    # email = forms.EmailField(required=False, label='Your Email Address')
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)

class ContactForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Contact
        fields = ['yourname', 'email', 'subject', 'message']
