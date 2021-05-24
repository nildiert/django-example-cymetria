from django.contrib import admin

from .models import OfficeInventory

# Register your models here.

@admin.register(OfficeInventory)
class OfficeInventoryAdmin(admin.ModelAdmin):
    pass