from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
from decimal import Decimal

from accounts.models import Account

from django import template
register = template.Library()



# Create your models here.

class Basket(models.Model):

    total = models.DecimalField(decimal_places=2,max_digits=8,null=True,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='customer_basket',on_delete=models.CASCADE)
    b_id_num = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.user}'s basket"

    def get_absolute_url(self):
        return reverse('basket:basket')


# class Order(models.Model):
#
#     user = models.ForeignKey(User,related_name='order',on_delete=models.CASCADE)
#     basket = models.ForeignKey(Basket,related_name='order',on_delete=models.CASCADE)
#
#     order_number = models.PositiveIntegerField()
#     order_date = models.DateField()
#
#     def __str__(self):
#         return self.order_number
#         # ^ Make this pk for OrderList View?
#
#     def get_absolute_url(self):
#         return reverse('accounts:single',kwargs={'account':self.account,
#                                                 'pk':self.pk})
#
#     class Meta:
#         ordering = ['-order_date']
