from django.db import models as db_models, transaction

from orders import repositories, models


class OrderService:
    _repository = repositories.OrderRepository()

    def get_orders(self) -> db_models.QuerySet[models.Order]:
        return self._repository.get_orders()

    @transaction.atomic
    def create_order(self, data: dict) -> models.Order:
        order_items = data.pop('order_items')
        order = self._repository.create_order(data=data)

        for item in order_items:
            item['order_id'] = order.id

        self._repository.create_order_items(order_items=order_items)

        return order
