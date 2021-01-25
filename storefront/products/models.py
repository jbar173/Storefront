from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
from decimal import Decimal
from basket.models import Basket
from orders.models import Order

from django import template
register = template.Library()

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Colour(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name


class Bouquet(models.Model):
    price = models.DecimalField(decimal_places=2,max_digits=8,default=Decimal('0.00'))
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE,blank=True,null=True,related_name='bouquet')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True,related_name='bouquet')

    def __str__(self):
        return f"Bouquet #{self.pk}"

    def get_absolute_url(self):
        return reverse('products:detail_bouquet',kwargs= {'pk':self.pk})


class Flower(models.Model):
    type = models.ForeignKey(Type,on_delete=models.CASCADE,related_name='flower_type')
    colour = models.ForeignKey(Colour,on_delete=models.CASCADE,related_name='flower_colour')
    price = models.DecimalField(blank=True,decimal_places=2,max_digits=8)
    bouquet = models.ForeignKey(Bouquet,on_delete=models.CASCADE,related_name='flower',null=True)

    def __str__(self):
        return f"{self.colour} {self.type}".title()

    def get_absolute_url(self):
        return reverse('products:detail_bouquet',kwargs={'pk':self.bouquet.pk})
