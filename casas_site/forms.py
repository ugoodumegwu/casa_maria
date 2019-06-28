from django.forms import Form
from django import forms



class ContactForm(Form):
    name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'contact_input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'contact_input'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'contact_input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'contact_input contact_textarea'}))
