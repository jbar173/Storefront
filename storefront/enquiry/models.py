from django.db.models import (Model, TextField, CharField, EmailField,
                            DateTimeField, OneToOneField, CASCADE, )
from regex import validate_phone

# Create your models here.

class Enquiry(Model):
    message = TextField(null=False,blank=False)
    name = CharField(max_length=300,null=False,blank=False)
    email = EmailField(null=False,blank=False)
    phone = CharField(validators=[validate_phone],max_length=15,null=False,blank=False)

    def __str__(self):
        return f"Enquiry #{self.id} ({self.name})"

    class Meta:
        verbose_name_plural = 'enquiries'

class EnquiryEmail(Model):
    date = DateTimeField(auto_now=True)
    enquiry = OneToOneField(Enquiry,on_delete=CASCADE,blank=True,null=True,related_name='enquiry_email')

    def __str__(self):
        return f"{self.date}: {self.enquiry}"
