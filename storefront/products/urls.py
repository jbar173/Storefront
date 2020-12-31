from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^main/$',views.ShopMain.as_view(),name="shop"),
    url(r'^range/$',views.RangeHome.as_view(),name='range'),
    url(r'^base/$',views.ProductsBase.as_view(),name='base'),

    url(r'^tailor/$',views.create_bouquet,name='tailor'),
    url(r'^(?P<bouquet_id>\d+)/create/single/$',views.FlowerCreate.as_view(),name="create_single"),
    url(r'^bouquet/(?P<pk>\d+)/$',views.BouquetDetail.as_view(),name="detail_bouquet"),
    url(r'^bouquet/(?P<pk>\d+)/update/$',views.UpdateBouquet.as_view(),name="update_bouquet"),
    url(r'^bouquet/(?P<pk>\d+)/delete/$',views.DeleteBouquet.as_view(),name="delete_bouquet"),

    url(r'^theme/$',views.TailorByTheme.as_view(),name='theme'),

]












####### basket urls?:


    # url(r'^orders/$',views.OrderList.as_view(),name='orders'),
    # url(r'^order/pk<order>.../$',views.SingleOrder.as_view(),name='single'),
