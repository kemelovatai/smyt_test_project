from django.db import models as db_models

from products import repositories, models


class ProductService:
    _repository = repositories.ProductRepository()

    def get_products(self) -> db_models.QuerySet[models.Product]:
        return self._repository.get_products()


class OrganizationService:
    _repository = repositories.OrganizationRepository()

    def get_organizations(self) -> db_models.QuerySet[models.Organization]:
        return self._repository.get_organizations()


class InventoryService:
    _repository = repositories.InventoryRepository()

    def get_inventories(self) -> db_models.QuerySet[models.Inventory]:
        return self._repository.get_inventories()

    def change_stock(self, inventory: models.Inventory, value: int) -> models.Inventory:
        return self._repository.change_stock(inventory=inventory, value=value)
