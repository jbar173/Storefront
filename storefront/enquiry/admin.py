from django.contrib import admin
from .models import Enquiry, EnquiryEmail

# Register your models here.

admin.site.register(Enquiry)
admin.site.register(EnquiryEmail)
