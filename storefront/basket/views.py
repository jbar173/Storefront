from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView,
                                  DetailView, UpdateView,
                                  DeleteView,)
from .models import Basket
from . import forms
from accounts.models import Account
from products.models import Bouquet
from orders.models import Order
from themed_products.models import ThemedBouquet
from range_products.models import RangeBouquet, Range
from django.urls import reverse_lazy
# import re
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


class BasketDetail(DetailView):
    model = Basket
    template_name = "basket/basket_detail.html"


class BasketMain(CreateView):
    model = Order
    template_name = "basket/basket.html"
    fields = ()

    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('basket:purchase_final')
        return success_url

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user.customer_account
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(BasketMain,self).get_context_data(**kwargs)
        b = Bouquet.objects.filter(basket=self.request.user.customer_basket)
        tb = ThemedBouquet.objects.filter(basket=self.request.user.customer_basket)
        r = RangeBouquet.objects.filter(basket=self.request.user.customer_basket)
        result = 0
        if len(b) > 0:
            for x in b:
                result += x.price
        if len(tb) > 0:
            for x in tb:
                result += x.price
        if len(r) > 0:
            for x in r:
                result += x.price
        context = {'b':b,'tb':tb,'r':r,'total':result}
        return context


class BasketTemp(TemplateView):
    template_name = "basket/basket_temp.html"


class BasketBouquetDelete(DeleteView):
    model = Bouquet
    template_name = 'basket/basket_bouquet_delete.html'
    success_url = reverse_lazy('basket:basket')


class BasketTBouquetDelete(DeleteView):
    model = ThemedBouquet
    template_name = 'basket/basket_bouquet_delete.html'
    success_url = reverse_lazy('basket:basket')


class BasketRBouquetDelete(DeleteView):
    model = RangeBouquet
    template_name = 'basket/basket_bouquet_delete.html'
    success_url = reverse_lazy('basket:basket')


class CreateAccountFromBasket(LoginRequiredMixin,CreateView):
    model = Account
    fields = ['first_name','surname','billing_address','delivery_address']
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('basket:basket')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateAccountFromBasket(LoginRequiredMixin,UpdateView):
    model = Account
    fields = ['first_name','surname','billing_address','delivery_address']
    template_name = 'accounts/edit_details.html'

    def get_success_url(self,**kwargs):
        success_url = reverse_lazy('basket:basket')
        return success_url



# class CreateBasket(CreateView):
#     model = Basket
#     form_class = forms.CreateBasketForm
#     template_name = 'basket/create_basket.html'
#
#     def get_success_url(self,**kwargs):
#         bas = self.request.user.customer_basket
#         if self.kwargs['b_model']== 'b':
#             success_url = reverse_lazy('products:update_bouquet_two', kwargs={'pk':bas.b_id_num})
#         elif self.kwargs['b_model']== 'tb':
#             success_url = reverse_lazy('themed_products:update_tbouquet_two', kwargs={'pk':bas.b_id_num})
#         else:
#             success_url = reverse_lazy('range_products:update_rbouquet', kwargs={'pk':bas.b_id_num})
#         return success_url
#
#     def get_context_data(self, **kwargs):
#         context = super(CreateBasket,self).get_context_data(**kwargs)
#         b1 = self.request.META.get('HTTP_REFERER')
#
#         b2 = re.findall(r'/\d+',b1)[-1]
#         b3 = re.findall(r'\d+',b2)[0]
#         context['bouq'] = b3
#
#         res = False
#         pattern = ['tbouquet']
#         if re.search(pattern[0],b1):
#             res = True
#         context['tb'] = res
#
#         pattern3 = ['/[-\w]+']
#         range_results = []
#         range_results = re.findall(pattern3[0],b1)
#         range_results2 = [x.strip('/') for x in range_results]
#         rb = False
#         if self.kwargs['b_model'] == 'r':
#             rb = True
#         context['r'] = rb
#         context['rng_nm'] = range_results2[-2]
#         context['r_slug'] = range_results2[-1]
#         return context
#
#     def get_initial(self,**kwargs):
#         initial = super().get_initial()
#         b1 = self.kwargs['pk']
#         initial['b_id_num'] = b1
#         return initial
#
#     def get_queryset(self):
#         return Range.objects.all()
#
#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.b_id_num = form.cleaned_data['b_id_num']
#         self.object.save()
#         return super().form_valid(form)
