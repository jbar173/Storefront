from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Account


class CreateCustomerForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "Email Address"



class CreateAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ['user',]
        widgets = {
            'billing_address': forms.Textarea(attrs={'rows':5}),
            'delivery_address': forms.Textarea(attrs={'rows':5}),
        }


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['first_name','surname','billing_address','delivery_address']
        widgets = {
            'billing_address': forms.Textarea(attrs={'rows':5,}),
            'delivery_address': forms.Textarea(attrs={'rows':5,}),
        }
