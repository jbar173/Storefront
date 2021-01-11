from django import forms
from . import models
from products.models import (Type,Colour,)
from django.forms import ModelForm



class CreateThemedBouquetForm(ModelForm):

    size = forms.ModelChoiceField(queryset=models.Size.objects.all())

    class Meta:
        model = models.ThemedBouquet
        exclude = ('basket','price',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



class CreateTypeThemeForm(ModelForm):

    b_id_num = forms.IntegerField(max_value=None,min_value=1,widget=forms.HiddenInput())
    type = forms.ModelChoiceField(queryset=models.Type.objects.all())

    class Meta:
        model = models.Theme
        exclude = ('name','colour','t_bouquet')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



class CreateColourThemeForm(ModelForm):

    b_id_num = forms.IntegerField(max_value=None,min_value=1,widget=forms.HiddenInput())
    colour = forms.ModelChoiceField(queryset=models.Colour.objects.all())

    class Meta:
        model = models.Theme
        exclude = ('name','type','t_bouquet')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
