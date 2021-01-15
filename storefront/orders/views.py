from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView,)
from .models import Order
from products.models import Bouquet
from themed_products.models import ThemedBouquet


# Create your views here.

class OrderDetail(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'


class CreateNewOrder(LoginRequiredMixin,CreateView):
    template_name = 'orders/create_order.html'
    model = Order
    fields = ()

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user.customer_account
        self.object.save()
        return super().form_valid(form)
