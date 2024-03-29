"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$',views.HomePage.as_view(),name='home'),
    path('admin/', admin.site.urls, name='myadmin'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^loggedin/$',views.LoggedInPage.as_view(),name='logged_in'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^about/$',views.AboutPage.as_view(),name='about'),
    url(r'^basket/',include('basket.urls',namespace='basket')),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^themed_products/',include('themed_products.urls',namespace='themed_products')),
    url(r'^orders/',include('orders.urls',namespace='orders')),
    url(r'^range_products/',include('range_products.urls',namespace='range_products')),
    url(r'^enquiry/',include('enquiry.urls',namespace='enquiry')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
