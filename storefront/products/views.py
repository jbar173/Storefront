from django.shortcuts import render,redirect
from django.views.generic import (CreateView, DetailView,
                                TemplateView, UpdateView,
                                DeleteView,)
from . import models
from . import forms
from basket.models import Basket
from .models import Type
from django.urls import reverse_lazy
import re


# Create your views here.

class FlowerCreate(CreateView):
    model = models.Flower
    form_class = forms.CreateFlowerForm
    template_name = 'products/create_flower.html'

    def get_context_data(self):
        context = super().get_context_data()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['prev'] = b3
        return context

    def form_valid(self,form):
        b1 = self.request.META.get('HTTP_REFERER')
        self.object = form.save(commit=False)
        self.object.price = self.object.type.price + self.object.colour.price
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        self.object.bouquet = models.Bouquet.objects.get(id__iexact=b3)
        self.object.save()
        return super().form_valid(form)


class FlowerDelete(DeleteView):
    model = models.Flower
    template_name = 'products/delete_flower.html'

    def get_success_url(self,**kwargs):
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        success_url = reverse_lazy('products:detail_bouquet',kwargs={'pk':b3})
        return success_url

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['prev'] = b3
        return context


def create_bouquet(request):
    new_bouquet = forms.CreateBouquetForm()

    if request.method == "POST":
        new_bouquet = forms.CreateBouquetForm(request.POST)

        if new_bouquet.is_valid():
            b = new_bouquet.save(commit=True)
            print("New bouquet created!")
            return redirect('products:detail_bouquet',pk=b.pk)
        else:
            print("Error - form invalid")

    return render(request,'products/tailor_home.html',{'bouquet_form': new_bouquet})


class BouquetDetail(DetailView):
    model = models.Bouquet
    template_name = 'products/tailor_flower.html'

    def get_context_data(self, **kwargs):
        context = super(BouquetDetail, self).get_context_data(**kwargs)
        result = 0
        for flower in self.object.flower.all():
            result += flower.price
        context['total'] = result
        return context


def update_bouquet(request,pk):
    bpk = pk
    object = models.Bouquet.objects.get(id=bpk)
    update_form = forms.UpdateBouquetForm()
    update_form.instance = object

    if request.method == "POST":
        update_form = forms.UpdateBouquetForm(request.POST)

        if update_form.is_valid():
            result = 0
            for flower in object.flower.all():
                result += flower.price
            object.price = result
            x = Basket.objects.get_or_create(user=request.user)[0]
            x.save()
            object.basket = x
            object.save()
            print("Bouquet updated")
            return redirect('basket:basket')
        else:
            print("Error - form invalid")

    return render(request,'products/update_bouquet.html', {'update_form': update_form,'bouquet_pk':pk})


class DeleteBouquet(DeleteView):
    model = models.Bouquet
    template_name = 'products/delete_bouquet.html'
    success_url = reverse_lazy('products:shop')


class BasketBouquetDetail(DetailView):
    model = models.Bouquet
    template_name = 'products/basket_bouquet_detail.html'


class ShopMain(TemplateView):
    template_name = 'products/shop_main.html'


class RangeHome(TemplateView):
    template_name = 'products/range_home.html'


### Update (condition: user doesn't have basket):

# class UpdateBouquet(UpdateView):
#     model = models.Bouquet
#     form_class = forms.UpdateBouquetForm
#     template_name = 'products/update_bouquet.html'
#
#     def get_success_url(self):
#         success_url = reverse_lazy('basket:create_basket', kwargs={'b_model':'b','pk':self.object.pk})
#         return success_url
#
#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         result = 0
#         for flower in self.object.flower.all():
#             result += flower.price
#         self.object.price = result
#         self.object.save()
#         return super().form_valid(form)

#####################


### Update (condition: user already has basket):
# class UpdateBouquetTwo(UpdateView):
#     model = models.Bouquet
#     form_class = forms.UpdateBouquetForm
#     template_name = 'products/update_bouquet.html'
#     success_url = reverse_lazy('basket:basket')
#
#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         result = 0
#         for flower in self.object.flower.all():
#             result += flower.price
#         self.object.price = result
#         self.object.basket = self.request.user.customer_basket
#         self.object.save()
#         return super().form_valid(form)

######################
