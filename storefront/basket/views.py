from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView,
                                  DetailView, UpdateView,
                                  DeleteView,)
from .models import Basket
from . import forms
from accounts.models import Account
from products.models import Bouquet
from themed_products.models import ThemedBouquet
from range_products.models import RangeBouquet, Range
from django.urls import reverse_lazy
import re
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your views here.


class CreateBasket(CreateView):
    model = Basket
    form_class = forms.CreateBasketForm
    template_name = 'basket/create_basket.html'

    def get_success_url(self,**kwargs):
        bas = self.request.user.customer_basket
        if self.kwargs['b_model']== 'b':
            success_url = reverse_lazy('products:update_bouquet_two', kwargs={'pk':bas.b_id_num})
        elif self.kwargs['b_model']== 'tb':
            success_url = reverse_lazy('themed_products:update_tbouquet_two', kwargs={'pk':bas.b_id_num})
        else:
            success_url = reverse_lazy('range_products:update_rbouquet', kwargs={'pk':bas.b_id_num})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(CreateBasket,self).get_context_data(**kwargs)
        b1 = self.request.META.get('HTTP_REFERER')

        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        context['bouq'] = b3

        res = False
        pattern = ['tbouquet']
        if re.search(pattern[0],b1):
            res = True
        context['tb'] = res

        pattern3 = ['/[-\w]+']
        range_results = []
        range_results = re.findall(pattern3[0],b1)
        range_results2 = [x.strip('/') for x in range_results]

        a = self.get_queryset()
        res2 = [x for x in a if x.name == range_results[-2]]
        rb = False
        if res2:
            rb = True
        context['r'] = rb
        context['rng_nm'] = range_results2[-2]
        context['r_slug'] = range_results2[-1]
        return context

    def get_initial(self,**kwargs):
        initial = super().get_initial()
        b1 = self.kwargs['pk']
        initial['b_id_num'] = b1
        return initial

    def get_queryset(self):
        return Range.objects.all()

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.b_id_num = form.cleaned_data['b_id_num']
        self.object.save()
        return super().form_valid(form)



class BasketDetail(DetailView):
    model = Basket
    template_name = "basket/basket_detail.html"



class BasketMain(TemplateView):
    template_name = "basket/basket.html"

    def get_context_data(self, **kwargs):
        context = super(BasketMain,self).get_context_data(**kwargs)
        b1 = self.get_queryset()[0]
        b2 = []
        for z in b1:
            if z.order:
                continue
            else:
                b2.append(z)        ######## Not working
        tb1 = self.get_queryset()[1]
        tb2 = []
        for z in tb1:
            if z.order:
                continue
            else:
                tb2.append(z)       ######## Not working
        r1 = self.get_queryset()[2]
        r2 = []
        for z in r1:
            if z.order:
                continue
            else:
                r2.append(z)
        context['b'] = b2
        context['tb'] = tb2
        context['r'] = r2

        result1 = 0
        result2 = 0
        result3 = 0
        if len(b2) > 0:
            for x in b2:
                result1 += x.price
        if len(tb2) > 0:
            for x in tb2:
                result2 += x.price
        if len(r1) > 0:
            for x in r2:
                result3 += x.price
        context['total'] = result1 + result2 + result3
        return context

    def get_queryset(self):
        x = Bouquet.objects.filter(basket=self.request.user.customer_basket)
        y = ThemedBouquet.objects.filter(basket=self.request.user.customer_basket)
        z = RangeBouquet.objects.filter(basket=self.request.user.customer_basket)
        return (x,y,z)



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
    success_url = reverse_lazy('basket:purchase_final')



######### Views for Order model in basket:

# class OrderList(LoginRequiredMixin,SelectRelatedMixin,ListView):
#     model = models.Order
#     select_related = ['account','order']

    # def get_queryset(self):
        # try:
        #     queryset = super().get_queryset(model=Account?) ???
        #     return queryset.filter(customer_id__exact=self.kwargs.get('username'))
        ### ^ Get an account with this specific customer variable

        # except DoesNotExist:
                ## redirect to CreateAccount view.
        #### ^ if an account with this specific customer variable doesn't exist

# class OrderList(TemplateView):
#     template_name = 'accounts/_order_list.html'
#
# class EditSuccess(TemplateView):
#     template_name = 'edit_success.html'
