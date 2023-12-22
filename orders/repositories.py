from django.db import models as db_models

from orders import models


class OrderRepository:
    @staticmethod
    def get_orders() -> db_models.QuerySet[models.Order]:
        return models.Order.objects.prefetch_related(
            'order_items',
            'order_items__organization',
            'order_items__product',
        )

    @staticmethod
    def create_order(data: dict) -> models.Order:
        return models.Order.objects.create(**data)

    @staticmethod
    def create_order_items(order_items: list[dict]) -> models.Order:
        return models.OrderItem.objects.bulk_create(
            (models.OrderItem(**item) for item in order_items)
        )
