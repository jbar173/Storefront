from django.conf.urls import url
from . import views


app_name = 'orders'

urlpatterns = [

    url(r'^detail/(?P<pk>\d+)/$',views.OrderDetail.as_view(),name='detail'),

]
