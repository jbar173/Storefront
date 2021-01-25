from django.contrib import admin
from django.conf import settings
from .models import (Type,Colour,Flower,
                    Bouquet,)

# Register your models here.

admin.site.register(Type)
admin.site.register(Colour)
admin.site.register(Flower)
admin.site.register(Bouquet)
