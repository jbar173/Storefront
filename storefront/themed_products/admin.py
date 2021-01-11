from django.contrib import admin
from .models import (ThemedBouquet, Theme,
                    Size,)


# Register your models here.

admin.site.register(Theme)
admin.site.register(ThemedBouquet)
admin.site.register(Size)
