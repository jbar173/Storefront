from django.conf.urls import url
from . import views
from themed_products.views import RandomCreateThemedBouquet

app_name = 'products'

urlpatterns = [

    url(r'^main/$',RandomCreateThemedBouquet.as_view(),name="shop"),
    url(r'^range/$',views.RangeHome.as_view(),name='range'),

    url(r'^tailor/$',views.create_bouquet,name='tailor'),
    url(r'^(?P<bouquet_id>\d+)/create/single/$',views.FlowerCreate.as_view(),name="create_single"),
    url(r'^(?P<pk>\d+)/(?P<bouquet_id>\d+)/delete/single/$',views.FlowerDelete.as_view(),name="delete_flower"),
    url(r'^bouquet/(?P<pk>\d+)/$',views.BouquetDetail.as_view(),name="detail_bouquet"),
    url(r'^bouquet/(?P<pk>\d+)/update/$',views.UpdateBouquet.as_view(),name="update_bouquet"),
    url(r'^bouquet/(?P<pk>\d+)/updatetwo/$',views.UpdateBouquetTwo.as_view(),name="update_bouquet_two"),
    url(r'^bouquet/(?P<pk>\d+)/delete/$',views.DeleteBouquet.as_view(),name="delete_bouquet"),
    url(r'^bouquetb/(?P<pk>\d+)/$',views.BasketBouquetDetail.as_view(),name="basket_bouquet"),

]












####### basket urls?:


    # url(r'^orders/$',views.OrderList.as_view(),name='orders'),
    # url(r'^order/pk<order>.../$',views.SingleOrder.as_view(),name='single'),
