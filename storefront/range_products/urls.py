from django.conf.urls import url
from . import views


app_name = 'range_products'


urlpatterns = [
    url(r'^create/$', views.CreateRangeBouquet.as_view(),name='create_one'),
    url(r'^create2/$', views.CreateRangeBouquetTwo.as_view(),name='create_two'),
    url(r'^list/(?P<range_name>[-\w]+)/$',views.RangeBouquetList.as_view(),name='range_list'),
    url(r'^detail/(?P<pk>\d+)/$',views.RangeBouquetDetail.as_view(),name='r_bouquet_detail'),
]
