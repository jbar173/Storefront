from django import forms
from . import models
from django.forms import ModelForm


# Create your forms here:


class CreateFlowerForm(ModelForm):

    class Meta:
        model = models.Flower
        fields = ('type','colour')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['type'].label = 'Select a flower:'
        self.fields['colour'].label = 'Select a colour:'


class CreateBouquetForm(ModelForm):

    class Meta:
        model = models.Bouquet
        exclude = ('basket','price','order',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class UpdateBouquetForm(ModelForm):

    class Meta:
        model = models.Bouquet
        exclude = ('price','basket','order',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
