from django import forms
from django.forms import ModelForm
from . import models
from regex import validate_phone

class CreateEnquiryForm(ModelForm):
    phone = forms.CharField(validators=[validate_phone,],
                            error_messages={'invalid': 'Please enter a valid phone number'},
                            widget=forms.TextInput(attrs={
                                'class': "phone-field",}))

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['message'].label = ''
        self.fields['message'].widget.attrs['placeholder'] = 'type your message here!'
        self.fields['name'].label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'your name'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'your email address'
        self.fields['phone'].label = ''
        self.fields['phone'].widget.attrs['placeholder'] = 'your phone number'

    class Meta:
        model = models.Enquiry
        fields = '__all__'
