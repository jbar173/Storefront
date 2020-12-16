from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse
from django.http import Http404

from django import template
register = template.Library()

# Create your models here

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='customer_account',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,blank=True)
    surname = models.CharField(max_length=30,blank=True)
    billing_address = models.TextField(blank=True)
    delivery_address = models.TextField(blank=True)

    def __str__(self):
        return f"Account: {self.user.username}"

    def get_absolute_url(self):
        return reverse('accounts:details',kwargs={'pk':self.pk})
