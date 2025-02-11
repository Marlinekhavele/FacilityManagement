from django.contrib import admin

from .models import Component, InventoryLevel

# Register your models here.
admin.site.register(InventoryLevel)
admin.site.register(Component)
