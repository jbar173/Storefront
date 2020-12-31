from django.db import models

# Create your models here.



# class Basket(models.Model):
#    user = models.ForeignKey(get_user_model....etc)
#     ( if user.account...etc)
#    bouquet = models.ForeignKey(Bouquet....etc)


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
