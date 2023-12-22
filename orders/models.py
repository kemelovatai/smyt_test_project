from django.db import models

from products.models import Organization, Product
from utils import choices
from utils.models import BaseModel


class Order(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=1000)
    status = models.CharField(
        choices=choices.OrderStatusChoices,
        default=choices.OrderStatusChoices.SYNCED,
        max_length=25,
    )

    class Meta:
        ordering = ('-created_at',)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

    class Meta:
        ordering = ('-created_at',)
