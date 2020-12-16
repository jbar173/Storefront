from django.db import models

# Create your models here.













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
