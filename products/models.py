from django.db import models

from utils.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=120, db_index=True)
    email = models.EmailField(max_length=50, unique=True, db_index=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Product(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=1000)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Warehouse(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='warehouses')
    address = models.CharField(max_length=1000)

    class Meta:
        ordering = ('-created_at',)


class Inventory(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    stock = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Inventories'
        ordering = ('-created_at',)
