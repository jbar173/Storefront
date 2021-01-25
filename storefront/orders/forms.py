from django import forms
from . import models
from products.models import Bouquet
from themed_products.models import ThemedBouquet
from range_products.models import RangeBouquet


class UpdateOrderBouquetsForm(forms.Form):
    confirm = forms.CharField(max_length=100,required=False,widget=forms.HiddenInput())
