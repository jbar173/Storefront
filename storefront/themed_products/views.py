from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                UpdateView, DeleteView,)
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import (Theme,ThemedBouquet,
                    Size,)
from products.models import (Type,Colour,)
from basket.models import Basket
from . import forms
import re


# Create your views here.

class RandomCreateThemedBouquet(CreateView):
    model = ThemedBouquet
    fields = ()
    template_name = 'products/shop_main.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('themed_products:random_update', self.object.id)


class RandomUpdateThemedBouquet(UpdateView):
    model = ThemedBouquet
    fields = ('price',)
    template_name = 'themed_products/update_random.html'


class CreateThemedBouquet(CreateView):
    model = ThemedBouquet
    form_class = forms.CreateThemedBouquetForm
    template_name = 'themed_products/create_themed_bouquet.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.price = self.object.size.price
        self.object.save()
        return super().form_valid(form)


class ThemedBouquetDetail(DetailView):
    model = ThemedBouquet
    template_name = 'themed_products/themed_detail.html'


class BasketThemedBouquetDetail(DetailView):
    model = ThemedBouquet
    template_name = 'themed_products/basket_tbouquet_detail.html'


class CreateTypeTheme(CreateView):
    model = Type
    form_class = forms.CreateTypeThemeForm
    template_name = 'themed_products/update_theme.html'

    def get_initial(self):
        initial = super().get_initial()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        initial['b_id_num'] = b3
        return initial

    def get_context_data(self):
        context = super().get_context_data()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['bouq'] = b3
        return context

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
    template_name = 'themed_products/update_theme.html'

    def get_initial(self):
        initial = super().get_initial()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        initial['b_id_num'] = b3
        return initial

    def get_context_data(self):
        context = super().get_context_data()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['bouq'] = b3
        return context

    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('themed_products:themed_detail', kwargs={'pk':self.object.t_bouquet.pk})
        return success_url

    def form_valid(self,form):
        self.object = form.save(commit=False)
        x = form.cleaned_data['b_id_num']
        self.object.t_bouquet = ThemedBouquet.objects.get(id__iexact=x)
        self.object.save()
        return super().form_valid(form)


class DeleteTheme(DeleteView):
    model = Theme
    template_name = 'themed_products/delete_theme.html'

    def get_success_url(self,**kwargs):
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        success_url = reverse_lazy('themed_products:themed_detail',kwargs={'pk':b3})
        return success_url

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['prev'] = b3
        return context


class DeleteThemedBouquet(DeleteView):
    model = ThemedBouquet
    template_name = 'themed_products/delete_tbouquet.html'
    success_url = reverse_lazy('products:shop')


### Update (condition: user doesn't have basket):
class UpdateTBouquet(UpdateView):
    model = ThemedBouquet
    form_class = forms.UpdateTBouquetForm
    template_name = 'themed_products/update_tbouquet.html'

    def get_success_url(self):
        success_url = reverse_lazy('basket:create_basket', kwargs={'b_model':'tb','pk':self.object.pk})
        return success_url


### Update (condition: user already has basket):
class UpdateTBouquetTwo(UpdateView):
    model = ThemedBouquet
    form_class = forms.UpdateTBouquetForm
    template_name = 'themed_products/update_tbouquet.html'
    success_url = reverse_lazy('basket:basket')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.basket = self.request.user.customer_basket
        self.object.save()
        return super().form_valid(form)
