from django.conf.urls import url
from . import views

app_name = 'themed_products'

urlpatterns = [

    url(r'^create/$',views.CreateThemedBouquet.as_view(),name="create_themed"),
    url(r'^tbouquetty/update/(?P<b_id>\d+)/$',views.CreateTypeTheme.as_view(),name="update_type"),
    url(r'^tbouquetc/update/(?P<b_id>\d+)/$',views.CreateColourTheme.as_view(),name="update_colour"),
    url(r'^tbouquetth/(?P<pk>\d+)/(?P<bouquet_id>\d+)/delete/$',views.DeleteTheme.as_view(),name="delete_theme"),
    url(r'^tbouquet/(?P<pk>\d+)/$',views.ThemedBouquetDetail.as_view(),name="themed_detail"),
    url(r'^tbouquetb/(?P<pk>\d+)/$',views.BasketThemedBouquetDetail.as_view(),name="basket_tbouquet"),
    url(r'^tbouquet/(?P<pk>\d+)/update/$',views.update_themed_bouquet,name='update_tbouquet'),
    url(r'^tbouquet/(?P<pk>\d+)/delete/$',views.DeleteThemedBouquet.as_view(),name="delete_tbouquet"),
    url(r'^rbouquet/(?P<pk>\d+)/update/$',views.RandomUpdateThemedBouquet.as_view(),name="random_update"),

    # url(r'^tbouquet/(?P<pk>\d+)/update/$',views.UpdateTBouquet.as_view(),name="update_tbouquet"),
    # url(r'^tbouquet/(?P<pk>\d+)/updatetwo/$',views.UpdateTBouquetTwo.as_view(),name="update_tbouquet_two"),
    ]
