from django.contrib import admin

from products import models
from utils.admin import BaseAdmin


@admin.register(models.Organization)
class OrganizationAdmin(BaseAdmin):
    list_display = ('id', 'name', 'email')


@admin.register(models.Product)
class ProductAdmin(BaseAdmin):
    list_display = ('id', 'organization', 'name', 'sku')


@admin.register(models.Warehouse)
class WarehouseAdmin(BaseAdmin):
    list_display = ('id', 'organization', 'address')


@admin.register(models.Inventory)
class InventoryAdmin(BaseAdmin):
    list_display = ('id', 'product', 'warehouse', 'stock')
