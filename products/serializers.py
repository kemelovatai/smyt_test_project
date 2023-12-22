from rest_framework import serializers

from products import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'id',
            'name',
            'email',
        )


class ProductShortSerializer(serializers.ModelSerializer):
    total_stock = serializers.IntegerField()  # annotated field

    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'sku',
            'total_stock',  # annotated field
        )


class CreateOrUpdateProductSerializer(ProductShortSerializer):
    class Meta:
        model = models.Product
        fields = (
            *ProductShortSerializer.Meta.fields,
            'organization',
        )


class ProductSerializer(ProductShortSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = models.Product
        fields = (
            *ProductShortSerializer.Meta.fields,
            'organization',
        )


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = (
            'id',
            'organization',
            'address',
        )


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = (
            'stock',
        )
