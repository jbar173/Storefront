import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'storefront.settings')

import django
django.setup()

from django.core.mail import send_mail
from enquiry.models import Enquiry,EnquiryEmail

# enq = EnquiryEmail.objects.all()[0]


def forward_enquiry(x):
    y = EnquiryEmail.objects.get(id=x.id)
    z = Enquiry.objects.get(id=y.enquiry.id)
    message = (z.message,z.name,z.email,z.phone)
    str_message = ' '.join(message)

    forward_email = send_mail(
    'New enquiry',
    str_message,
    'from@ourbusiness.com',
    ['xxxx@gmail.com','xxxx@hotmail.com'])

    return forward_email


if __name__ == '__main__':
    print("Hello")
    forward_enquiry(enq)
    print("finished")
