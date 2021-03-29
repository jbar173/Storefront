from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext as _

def phone_regex(num):
    pattern = '^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$'
    x = re.findall(pattern,num)
    if x:
        return True
    else:
        return False

def validate_phone(num):
    regex = phone_regex(num)
    if regex == False:
        raise ValidationError(_('Please enter a valid phone number'), code="invalid")
