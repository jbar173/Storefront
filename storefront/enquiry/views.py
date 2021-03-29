from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Enquiry,EnquiryEmail
from . import forms
from s_email import forward_enquiry

class CreateEnquiry(CreateView):
    model = Enquiry
    template_name = 'enquiry/enquiry.html'
    form_class = forms.CreateEnquiryForm
    success_url = reverse_lazy('enquiry:success')

    def form_invalid(self,form):
        print(f"**{form.errors.as_data()['phone'][0].code}")
        return super().form_invalid(form)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        x = EnquiryEmail.objects.create(enquiry=self.object)
        x.save()
        forward_enquiry(x)
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'enquiry/success.html'
