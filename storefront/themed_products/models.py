from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
from decimal import Decimal

from orders.models import Order
from basket.models import Basket
from products.models import (Type,Colour,)

from django import template
register = template.Library()


THEME_CHOICES = [

    ('Type', 'Type'),
    ('Colour', 'Colour'),
    ('Type and Colour', 'Type and Colour'),
]

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name


class ThemedBouquet(models.Model):
    theme_name = models.CharField(max_length=50,null=True,blank=True,choices=THEME_CHOICES)
    price = models.DecimalField(decimal_places=2,max_digits=8,default=Decimal('0.00'))
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE,blank=True,null=True,related_name='themed_bouquet')
    size = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True,related_name='bouquet')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True,related_name='tbouquet')

    def __str__(self):
        return f"Themed Bouquet #{self.pk}"

    def get_absolute_url(self):
        return reverse('themed_products:themed_detail',kwargs= {'pk':self.pk})


class Theme(models.Model):
    name = models.CharField(max_length=50)
    colour = models.ForeignKey(Colour,on_delete=models.CASCADE,null=True,blank=True,related_name='theme_colour')
    type = models.ForeignKey(Type,on_delete=models.CASCADE,null=True,blank=True,related_name='theme_type')
    t_bouquet = models.ForeignKey(ThemedBouquet,on_delete=models.CASCADE,null=True,blank=True,related_name='theme')

    def __str__(self):
        return f"Theme: By {self.t_bouquet.theme_name}"
