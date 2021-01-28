from django import forms


class UpdateOrderBouquetsForm(forms.Form):
    confirm = forms.CharField(max_length=100,required=False,widget=forms.HiddenInput())
