from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . import models

### Tailoring the AUTH form for the AUTH User model :
class CreateCustomerForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "Email Address"
