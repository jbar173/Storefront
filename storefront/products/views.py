from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                TemplateView,)
from . import models
from . import forms

# Create your views here.


class FlowerCreate(CreateView):
    model = models.Flower
    form_class = forms.CreateFlowerForm
    template_name = 'products/create_flower.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.price = self.object.type.price + self.object.colour.price
        self.object.save()
        return super().form_valid(form)


class FlowerDetail(DetailView):
    model = models.Flower
    template_name = 'products/_flower_detail.html'


class ShopMain(TemplateView):
    template_name = 'products/shop_main.html'

class RangeHome(TemplateView):
    template_name = 'products/range_home.html'

class TailorHome(TemplateView):
    template_name = 'products/tailor_home.html'

class TailorByTheme(TemplateView):
    template_name = 'products/tailor_theme.html'

class TailorByFlower(TemplateView):
    template_name = 'products/tailor_flower.html'



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
