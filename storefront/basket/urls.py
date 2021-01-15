from django.conf.urls import url
from . import views
from orders.views import CreateNewOrder
from django.views.generic import TemplateView

app_name = 'basket'

urlpatterns = [

    url(r'^create/$',views.CreateBasket.as_view(),name='create_basket'),
    url(r'^$',views.BasketMain.as_view(),name='basket'),
    url(r'^x/$',views.BasketTemp.as_view(),name='basketx'),
    url(r'^(?P<pk>\d+)/$',views.BasketDetail.as_view(),name='basket_detail'),
    url(r'^(?P<pk>\d+)/(?P<basket_id>\d+)/delete/$',views.BasketBouquetDelete.as_view(),name='delete_bouquet'),
    url(r'^(?P<pk>\d+)/(?P<basket_id>\d+)/tdelete/$',views.BasketTBouquetDelete.as_view(),name='delete_tbouquet'),
    url(r'^confirm/$',views.CreateAccountFromBasket.as_view(),name='purchase'),
    url(r'^confirm/final/$',CreateNewOrder.as_view(),name='purchase_final'),
    url(r'^confirm/(?P<pk>\d+)/update/$',views.UpdateAccountFromBasket.as_view(),name="update_purchase"),

]
