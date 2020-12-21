from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^create/single/$',views.FlowerCreate.as_view(),name="create_single"),
    url(r'^single/detail/(?P<pk>\d+)/$',views.FlowerDetail.as_view(),name="detail_single"),
    url(r'^main/$',views.ShopMain.as_view(),name="shop"),
    url(r'^tailor/$',views.TailorHome.as_view(),name='tailor'),
    url(r'^range/$',views.RangeHome.as_view(),name='range'),
    url(r'^theme/$',views.TailorByTheme.as_view(),name='theme'),
    url(r'^flower/$',views.TailorByFlower.as_view(),name='flower'),
]












####### basket urls?:


    # url(r'^orders/$',views.OrderList.as_view(),name='orders'),
    # url(r'^order/pk<order>.../$',views.SingleOrder.as_view(),name='single'),
