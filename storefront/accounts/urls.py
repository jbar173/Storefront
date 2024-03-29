from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    url(r'^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),
    url(r'^create/$',views.CreateAccount.as_view(),name='create'),
    url(r'^details/(?P<pk>\d+)/$',views.DisplayDetails.as_view(),name='details'),
    url(r'^edit/(?P<pk>\d+)/$',views.EditAccount.as_view(),name='edit'),

]
