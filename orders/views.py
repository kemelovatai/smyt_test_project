from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet

from orders import models, serializers, services


class OrderViewSet(ModelViewSet):
    service = services.OrderService()

    serializer_class = serializers.OrderSerializer

    def get_queryset(self) -> QuerySet[models.Order]:
        return self.service.get_orders()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateOrderSerializer
        if self.action in ('update', 'partial_update'):
            return serializers.UpdateOrderSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer) -> None:
        self.service.create_order(serializer.validated_data)
