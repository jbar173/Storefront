from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView,
                                    UpdateView,)
from django.urls import reverse_lazy

from .models import Order
from products.models import Bouquet
from themed_products.models import ThemedBouquet
from range_products.models import RangeBouquet
from .forms import UpdateOrderBouquetsForm


# Create your views here.

class OrderDetail(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        b = Bouquet.objects.filter(order_id=self.object.pk)
        t = ThemedBouquet.objects.filter(order_id=self.object.pk)
        r = RangeBouquet.objects.filter(order_id=self.object.pk)
        context= {'b':b,'t':t,'r':r}
        return context


def update_new_order(request):
    order_bouquets = UpdateOrderBouquetsForm

    if request.method == "POST":
        order_bouquets = UpdateOrderBouquetsForm(request.POST)

        if order_bouquets.is_valid():
            bo = Bouquet.objects.filter(basket=request.user.customer_basket)
            th = ThemedBouquet.objects.filter(basket=request.user.customer_basket)
            ra = RangeBouquet.objects.filter(basket=request.user.customer_basket)
            ord = Order.objects.filter(account=request.user.customer_account)

            bo1 = [x for x in bo]
            th1 = [x for x in th]
            ra1 = [x for x in ra]
            ord1 = [x for x in ord]

            i = -1
            for x in bo1:
                i += 1
                if x.order:
                    bo1.pop(i)
            i = -1
            for x in th1:
                i += 1
                if x.order:
                    th1.pop(i)
            i = -1
            for x in ra1:
                i += 1
                if x.order:
                    ra1.pop(i)

            ord2 = ord1[0]
            o_price = 0
            for x in bo1:
                o_price += x.price
                new_bouq = x
                new_bouq.order = ord2
                new_bouq.basket = None
                new_bouq.save()

            for x in th1:
                o_price += x.price
                new_tbouq = x
                new_tbouq.order = ord2
                new_tbouq.basket = None
                new_tbouq.save()

            for x in ra1:
                o_price += x.price
                new_rbouq = x
                new_rbouq.order = ord2
                new_rbouq.basket = None
                new_rbouq.save()

            ord2.final = True
            ord2.order_total = o_price
            ord2.save()
            return redirect('orders:detail',pk=ord2.pk)
        else:
            print("Error - form invalid")

    return render(request,'orders/create_order.html',{'bouquet_order_form': order_bouquets})
