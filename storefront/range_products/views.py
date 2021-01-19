from django.shortcuts import render
from .models import (RangeBouquet, Range,)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView,
                                DetailView,)



# Create your views here.


class CreateRangeBouquet(CreateView):
    model = RangeBouquet
    template_name = 'range_products/create_range_bouquet.html'
    fields = ()
    success_url = reverse_lazy('basket:create_basket')


### Already has a basket:

class CreateRangeBouquetTwo(CreateView):
    model = RangeBouquet
    template_name = 'range_products/create_range_bouquet.html'
    fields = ()
    success_url = reverse_lazy('basket:basket')

    def get_queryset(self):
        a = RangeBouquet.objects.filter(slug=self.kwargs['slug'])[0]
        b = Range.objects.filter(name=self.kwargs['range_name'])[0]
        return (a,b)

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        y = self.get_queryset()[1]
        context['rng'] = y.name
        return context

    def form_valid(self,form):
        self.object = form.save(commit=False)
        z = self.get_queryset()[0]
        self.object.item_name = z.item_name
        self.object.price = z.price
        self.object.image = z.image
        self.object.basket = self.request.user.customer_basket
        self.object.save()
        print("bouquet created")
        return super().form_valid(form)



class RangeBouquetList(ListView):
    model = Range
    template_name = 'range_products/range_products_list.html'

    def get_queryset(self):
         return Range.objects.filter(name=self.kwargs['range_name'])


class RangeBouquetDetail(DetailView):
    model = RangeBouquet
    template_name = 'range_products/rbouquet_detail.html'
