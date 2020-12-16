from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


## Mock view:

class BasketMain(TemplateView):
    template_name = "basket/basket_main.html"

class ConfirmPurchase(TemplateView):
    template_name = "basket/confirm_purchase.html"
