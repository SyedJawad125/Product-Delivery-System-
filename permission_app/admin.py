from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Role)
admin.site.register(Permission)
# admin.site.register(Product)
