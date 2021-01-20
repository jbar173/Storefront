from django.conf.urls import url
from . import views


app_name = 'orders'

urlpatterns = [

    url(r'^detail/(?P<pk>\d+)/$',views.OrderDetail.as_view(),name='detail'),

]

####### basket urls?:
    # url(r'^orders/$',views.OrderList.as_view(),name='orders'),
    # url(r'^order/pk<order>.../$',views.SingleOrder.as_view(),name='single'),
