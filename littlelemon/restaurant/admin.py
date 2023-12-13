from django.contrib import admin
from .models import MenuItems, Booking

# Register your models here.
admin.site.register(Booking)
admin.site.register(MenuItems)