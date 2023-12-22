from django.db.models import QuerySet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products import models, serializers, services


class ProductViewSet(ModelViewSet):
    service = services.ProductService()

    serializer_class = serializers.ProductSerializer

    def get_queryset(self) -> QuerySet[models.Product]:
        return self.service.get_products()

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return serializers.CreateOrUpdateProductSerializer

        return super().get_serializer_class()


class OrganizationViewSet(ModelViewSet):
    service = services.OrganizationService()

    serializer_class = serializers.OrganizationSerializer

    def get_queryset(self) -> QuerySet[models.Organization]:
        return self.service.get_organizations()


class InventoryViewSet(mixins.UpdateModelMixin, GenericViewSet):
    service = services.InventoryService()

    serializer_class = serializers.InventorySerializer

    def get_queryset(self) -> QuerySet[models.Inventory]:
        return self.service.get_inventories()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.service.change_stock(inventory=instance, value=serializer.validated_data['stock'])

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
