from django import forms
from school.models import ContactModel

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter the Name")
    email = forms.EmailField(max_length=40, help_text="Enter the email")
    message = forms.CharField(widget=forms.Textarea, help_text="Enter the message")

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = (
            'name',
            'email',
            'message',
            'university',
        )