from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                TemplateView, UpdateView,
                                DeleteView,)
from . import models
from . import forms
from .models import Type
from django.urls import reverse_lazy
from django.shortcuts import redirect
import re


# Create your views here.

class FlowerCreate(CreateView):
    model = models.Flower
    form_class = forms.CreateFlowerForm
    template_name = 'products/create_flower.html'

    def form_valid(self,form):
        b1 = self.request.META.get('HTTP_REFERER')
        self.object = form.save(commit=False)
        self.object.price = self.object.type.price + self.object.colour.price
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        self.object.bouquet = models.Bouquet.objects.get(id__iexact=b3)
        self.object.save()
        return super().form_valid(form)


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


### Update (condition: user doesn't have basket):
class UpdateBouquet(UpdateView):
    model = models.Bouquet
    form_class = forms.UpdateBouquetForm
    template_name = 'products/update_bouquet.html'
    success_url = reverse_lazy('basket:create_basket')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        result = 0
        for flower in self.object.flower.all():
            result += flower.price
        self.object.price = result
        self.object.save()
        return super().form_valid(form)


### Update (condition: user already has basket):
class UpdateBouquetTwo(UpdateView):
    model = models.Bouquet
    form_class = forms.UpdateBouquetForm
    template_name = 'products/update_bouquet.html'
    success_url = reverse_lazy('basket:basket')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        result = 0
        for flower in self.object.flower.all():
            result += flower.price
        self.object.price = result
        self.object.basket = self.request.user.customer_basket
        self.object.save()
        return super().form_valid(form)


class DeleteBouquet(DeleteView):
    model = models.Bouquet
    template_name = 'products/delete_bouquet.html'
    success_url = reverse_lazy('products:shop')


########


class ShopMain(TemplateView):
    template_name = 'products/shop_main.html'


class RangeHome(TemplateView):
    template_name = 'products/range_home.html'


########
