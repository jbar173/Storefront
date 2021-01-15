from django.db import models
from django.urls import reverse
from accounts.models import Account

from django import template
register = template.Library()


# Create your models here.


class Order(models.Model):

    order_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True,related_name='order')
    order_total = models.DecimalField(decimal_places=2,max_digits=8,null=True,blank=True)

    def __str__(self):
        return f"Order # {self.pk}"

    def get_absolute_url(self,*args,**kwargs):
        return reverse('orders:detail',kwargs={'pk':self.pk})
