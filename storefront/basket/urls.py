from django.conf.urls import url
from . import views
from orders.views import update_new_order
from django.views.generic import TemplateView

app_name = 'basket'

urlpatterns = [

    url(r'^$',views.BasketMain.as_view(),name='basket'),
    url(r'^x/$',views.BasketTemp.as_view(),name='basketx'),
    url(r'^(?P<pk>\d+)/$',views.BasketDetail.as_view(),name='basket_detail'),
    url(r'^(?P<pk>\d+)/(?P<basket_id>\d+)/delete/$',views.BasketBouquetDelete.as_view(),name='delete_bouquet'),
    url(r'^(?P<pk>\d+)/(?P<basket_id>\d+)/tdelete/$',views.BasketTBouquetDelete.as_view(),name='delete_tbouquet'),
    url(r'^(?P<pk>\d+)/(?P<basket_id>\d+)/rdelete/$',views.BasketRBouquetDelete.as_view(),name='delete_rbouquet'),
    url(r'^confirm/$',views.CreateAccountFromBasket.as_view(),name='purchase'),
    url(r'^confirm/final/$',update_new_order,name='purchase_final'),
    url(r'^confirm/(?P<pk>\d+)/update/$',views.UpdateAccountFromBasket.as_view(),name="update_purchase"),

    # url(r'^create/(?P<b_model>[-\w]+)/(?P<pk>\d+)/$',views.CreateBasket.as_view(),name='create_basket'),
]
