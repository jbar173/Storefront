from django.conf.urls import url
from . import views

app_name = 'themed_products'

urlpatterns = [

    url(r'^create/$',views.CreateThemedBouquet.as_view(),name="create_themed"),
    url(r'^tbouquetty/update/$',views.CreateTypeTheme.as_view(),name="update_type"),
    url(r'^tbouquetc/update/$',views.CreateColourTheme.as_view(),name="update_colour"),
    url(r'^tbouquet/(?P<pk>\d+)/$',views.ThemedBouquetDetail.as_view(),name="themed_detail"),
    
    ]
