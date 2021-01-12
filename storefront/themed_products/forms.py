from django import forms
from .models import (ThemedBouquet, Theme, Size,)
from products.models import (Type, Colour,)
from django.forms import ModelForm



class CreateThemedBouquetForm(ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects.all())

    class Meta:
        model = ThemedBouquet
        exclude = ('basket','price',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



class CreateTypeThemeForm(ModelForm):

    b_id_num = forms.IntegerField(max_value=None,min_value=1,widget=forms.HiddenInput())
    type = forms.ModelChoiceField(queryset=Type.objects.all())

    class Meta:
        model = Theme
        exclude = ('name','colour','t_bouquet')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



class CreateColourThemeForm(ModelForm):

    b_id_num = forms.IntegerField(max_value=None,min_value=1,widget=forms.HiddenInput())
    colour = forms.ModelChoiceField(queryset=Colour.objects.all())

    class Meta:
        model = Theme
        exclude = ('name','type','t_bouquet')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class UpdateTBouquetForm(ModelForm):

    class Meta:
        model = ThemedBouquet
        exclude = ('price','basket','theme_name','size')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
