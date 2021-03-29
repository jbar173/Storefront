from django.conf.urls import url
from . import views

app_name = 'enquiry'

urlpatterns = [
    url(r'^$',views.CreateEnquiry.as_view(),name="new_enquiry"),
    url(r'^success/$',views.SuccessView.as_view(),name="success"),
]
