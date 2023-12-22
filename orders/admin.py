from django.contrib import admin

from orders import models
from utils.admin import BaseAdmin


class OrderItemInline(admin.StackedInline):
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(BaseAdmin):
    list_display = ('id', 'organization', 'address', 'status')
    inlines = (
        OrderItemInline,
    )
