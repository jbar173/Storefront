from django.contrib import admin
from django.conf import settings
from .models import (Type,Colour,Flower)



# Register your models here.

admin.site.register(Type)
admin.site.register(Colour)
admin.site.register(Flower)
