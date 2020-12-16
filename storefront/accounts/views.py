from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.views.generic import (CreateView, UpdateView,
                                ListView, DetailView,
                                TemplateView,)
from . import forms
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.http import Http404
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

class EditAccount(LoginRequiredMixin,UpdateView):
    model = models.Account
    fields = ['first_name','surname','billing_address','delivery_address']
    template_name = 'accounts/edit_details.html'
