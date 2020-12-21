from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib import auth

from django import template
register = template.Library()
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name


class Flower(models.Model):
    type = models.ForeignKey(Type,on_delete=models.CASCADE,related_name='flower_type')
    colour = models.ForeignKey(Colour,on_delete=models.CASCADE,related_name='flower_colour')
    price = models.DecimalField(blank=True,decimal_places=2,max_digits=8)

    def __str__(self):
        return f"{self.colour} {self.type}".title()

    def get_absolute_url(self):
        return reverse('products:detail_single',kwargs= {'pk':self.pk})

# class BouquetFlower(models.Model):
#


class Bouquet(models.Model):
    bouquet_flower = models.ManyToManyField(Flower,related_name='flower')
    price = models.DecimalField(blank=True,decimal_places=2,max_digits=8)

    def __str__(self):
        return f"Bouquet #{self.pk}"
        pass

    def get_absolute_url(self):
        return reverse('products:bouquet_detail',kwargs= {'pk':self.pk})

    pass



##### basket app notes:

# class CustomerOrders(models.Model):
#     account = models.ForeignKey(Account,related_name='prev_order',on_delete=models.CASCADE)
#     order = models.ForeignKey(Order,related_name='prev_order',on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Previous orders for {self.account.username}:"
#
#     class Meta:
#         unique_together = ['account','order']
############### ^ Handled by OrderList View?


##### in basket app??:

# class Order(models.Model):
#     account = models.ForeignKey(Account,related_name='orders',on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)
#     # basket = models.ForeignKey(Basket,related_name='order',on_delete=models.CASCADE)
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
