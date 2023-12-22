from rest_framework import serializers

from orders import models
from products import serializers as products_serializers


class CreateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = (
            'id',
            'organization',
            'product',
            'quantity',
        )


class OrderItemSerializer(CreateOrderItemSerializer):
    organization = products_serializers.OrganizationSerializer(read_only=True)
    product = products_serializers.ProductShortSerializer(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = (
            *CreateOrderItemSerializer.Meta.fields,
        )


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            'id',
            'organization',
            'address',
            'status',
        )


class CreateOrderSerializer(UpdateOrderSerializer):
    order_items = CreateOrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = models.Order
        fields = (
            *UpdateOrderSerializer.Meta.fields,
            'order_items',
        )
        extra_kwargs = {'status': {'read_only': True}}


class OrderSerializer(CreateOrderSerializer):
    organization = products_serializers.OrganizationSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = (
            *CreateOrderSerializer.Meta.fields,
        )
