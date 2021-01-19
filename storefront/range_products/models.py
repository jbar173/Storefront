from django.db import models
from basket.models import Basket
from orders.models import Order
from django.utils.text import slugify


# Create your models here.


class RangeBouquet(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=8,null=True,blank=True)
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE,blank=True,null=True,related_name='range_bouquet')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True,related_name='r_bouquet')
    image = models.ImageField(upload_to='range_pics',blank=True,null=True)
    slug = models.SlugField(allow_unicode=True,null=True)

    def __str__(self):
        return self.item_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.item_name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('range_products:r_bouquet_detail',kwargs= {'pk':self.pk})


class Range(models.Model):
    name = models.CharField(max_length=100)
    r_bouquet = models.ForeignKey(RangeBouquet,on_delete=models.CASCADE,blank=True,null=True,related_name='range')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('range_products:range_list',kwargs={'range_name':self.name})
