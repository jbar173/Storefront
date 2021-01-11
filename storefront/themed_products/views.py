from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                TemplateView, UpdateView,
                                DeleteView,)
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import (Theme,ThemedBouquet,
                    Size,)
from products.models import (Type, Colour,)
from . import forms
from basket.models import Basket

import re


# Create your views here.


class CreateThemedBouquet(CreateView):
    model = ThemedBouquet
    form_class = forms.CreateThemedBouquetForm
    template_name = 'themed_products/create_themed_bouquet.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.price = self.object.size.price
        x = Theme.objects.all()
        for y in x:
            print(f"y1: {y}")
            if y.name == self.object.theme_name:
                print(f"y2: {y}")
                y.t_bouquet = self.object
        self.object.save()
        return super().form_valid(form)


class ThemedBouquetDetail(DetailView):
    model = ThemedBouquet
    template_name = 'themed_products/themed_detail.html'


class CreateTypeTheme(CreateView):
    model = Type
    form_class = forms.CreateTypeThemeForm
    template_name = 'themed_products/update_type_theme.html'

    def get_initial(self):
        initial = super().get_initial()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        initial['b_id_num'] = b3
        return initial

    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('themed_products:themed_detail', kwargs={'pk':self.object.t_bouquet.pk})
        return success_url

    def form_valid(self,form):
        self.object = form.save(commit=False)
        x = form.cleaned_data['b_id_num']
        self.object.t_bouquet = ThemedBouquet.objects.get(id__iexact=x)
        self.object.save()
        return super().form_valid(form)


class CreateColourTheme(CreateView):
    model = Colour
    form_class = forms.CreateColourThemeForm
    template_name = 'themed_products/update_type_theme.html'

    def get_initial(self):
        initial = super().get_initial()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        initial['b_id_num'] = b3
        return initial

    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('themed_products:themed_detail', kwargs={'pk':self.object.t_bouquet.pk})
        return success_url

    def form_valid(self,form):
        self.object = form.save(commit=False)
        x = form.cleaned_data['b_id_num']
        self.object.t_bouquet = ThemedBouquet.objects.get(id__iexact=x)
        self.object.save()
        return super().form_valid(form)
