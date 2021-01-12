from django.conf.urls import url
from . import views
# from accounts.views import CreateAccount
from django.views.generic import TemplateView

app_name = 'basket'

urlpatterns = [

    url(r'^create/$',views.CreateBasket.as_view(),name='create_basket'),
    url(r'^$',views.BasketMain.as_view(),name='basket'),
    url(r'^x/$',views.BasketTemp.as_view(),name='basketx'),
    url(r'^(?P<pk>\d+)/$',views.BasketDetail.as_view(),name='basket_detail'),
    url(r'^confirm/$',views.CreateAccountFromBasket.as_view(),name='purchase'),
    url(r'^confirm/final/$',TemplateView.as_view(template_name="basket/confirm_purchase_final.html"),name='purchase_final'),
    url(r'^confirm/(?P<pk>\d+)/update/$',views.UpdateAccountFromBasket.as_view(),name="update_purchase"),

]
