from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView,)
from .models import Order
from products.models import Bouquet
from themed_products.models import ThemedBouquet
from range_products.models import RangeBouquet


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
        queryset = self.get_queryset()
        for x in queryset[0]:
            if x.order:
                print("b continue")
            else:
                x.order = self.object
                print(f"x.order: {x.order}")    ######## Not working
        for y in queryset[1]:
            if y.order:
                print("tb continue")
            else:
                y.order = self.object
                print(f"y.order: {y.order}")    ######## Not working
        for z in queryset[2]:
            if z.order:
                print("r continue")
            else:
                z.order = self.object
                print(f"z.order: {z.order}")

        # self.object.order_total = self.request.user.customer_basket.total  ###### fix
        ## On basket_detail template only show items not already associated with an order
        ## - only add these totals up in get_context_data
        # self.object.order_date = timezone.now
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self):
        a = Bouquet.objects.filter(basket=self.request.user.customer_basket)
        b = ThemedBouquet.objects.filter(basket=self.request.user.customer_basket)
        c = RangeBouquet.objects.filter(basket=self.request.user.customer_basket)
        return (a,b,c)
