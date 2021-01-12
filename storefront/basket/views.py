from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView,
                                  DetailView, UpdateView,)
from .models import Basket
from . import forms
from accounts.models import Account
from products.models import Bouquet
from themed_products.models import ThemedBouquet
from django.urls import reverse_lazy
import re
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


class CreateBasket(CreateView):
    model = Basket
    form_class = forms.CreateBasketForm
    template_name = 'basket/create_basket.html'

    def get_success_url(self):
        bas = self.request.user.customer_basket
        success_url = reverse_lazy('products:update_bouquet_two', kwargs={'pk':bas.b_id_num})
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
        return context

    def get_initial(self):
        initial = super().get_initial()
        b1 = self.request.META.get('HTTP_REFERER')
        b2 = re.findall(r'/\d+',b1)[-1]
        b3 = re.findall(r'\d+',b2)[0]
        initial['b_id_num'] = b3
        return initial

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
            b2.append(z)
        tb1 = self.get_queryset()[1]
        tb2 = []
        for z in tb1:
            tb2.append(z)
        context['b'] = b2
        context['tb'] = tb2

        result1 = 0
        result2 = 0
        if len(b1) > 0:
            for x in b1:
                result1 += x.price
        if len(tb2) > 0:
            for x in tb2:
                result2 += x.price
        context['total'] = result1+result2
        return context

    def get_queryset(self):
        x = Bouquet.objects.filter(basket=self.request.user.customer_basket)
        y = ThemedBouquet.objects.filter(basket=self.request.user.customer_basket)
        return (x,y)



class BasketTemp(TemplateView):
    template_name = "basket/basket_temp.html"


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
    success_url = reverse_lazy('basket:purchase_final') ## change to Order createview url


class FinalConfirmView(TemplateView):
    template_name = 'basket/confirm_purchase_final.html'


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
