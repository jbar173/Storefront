from django import forms
from . import models
from products.models import Bouquet
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


class CreateBasketForm(ModelForm):

    b_id_num = forms.IntegerField(max_value=None,min_value=1,widget=forms.HiddenInput())

    class Meta:
        model = models.Basket
        exclude = ('user','order')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
