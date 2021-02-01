from django import forms
from .models import RangeBouquet
from django.forms import ModelForm


class CreateRBouquetForm(ModelForm):

    class Meta:
        model = RangeBouquet
        fields = ()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
