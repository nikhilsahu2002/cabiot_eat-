from django.contrib import admin
from .models import Kitchen,Menu,DeliveryArea,MenuItem

# Register your models here.
admin.site.register(Kitchen)
admin.site.register(Menu)
admin.site.register(DeliveryArea)
admin.site.register(MenuItem)