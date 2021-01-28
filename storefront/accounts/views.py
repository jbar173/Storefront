from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.views.generic import (CreateView, UpdateView,
                                DetailView,)
from . import forms
from . import models
from orders.models import Order
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class SignUp(CreateView):
    form_class = forms.CreateCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class CreateAccount(LoginRequiredMixin,CreateView):
    model = models.Account
    fields = ['first_name','surname','billing_address','delivery_address']
    template_name = 'accounts/create_account.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DisplayDetails(DetailView,SelectRelatedMixin):
    model = models.Account
    template_name = 'accounts/display_details.html'

    def get_context_data(self,*args,**kwargs):
        context = super(DisplayDetails,self).get_context_data(*args,**kwargs)
        q = Order.objects.filter(account=self.request.user.customer_account)
        r = [x for x in q if x.final == True]
        context['customer_orders'] = r
        return context

class EditAccount(LoginRequiredMixin,UpdateView):
    model = models.Account
    fields = ['first_name','surname','billing_address','delivery_address']
    template_name = 'accounts/edit_details.html'
