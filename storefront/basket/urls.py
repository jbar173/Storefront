from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'basket'

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="basket/basket_main.html"),name='basket'),
    url(r'^confirm/$',TemplateView.as_view(template_name="basket/confirm_purchase.html"),name='purchase'),
    # url(r'^$',views.BasketMain.as_view(),name='basket'),
    # url(r'^confirm/$',views.ConfirmPurchase.as_view(),name='purchase'),
]
