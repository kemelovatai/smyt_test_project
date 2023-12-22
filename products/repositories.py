from django.db import models as db_models

from products import models


class ProductRepository:
    @staticmethod
    def get_products() -> db_models.QuerySet[models.Product]:
        return models.Product.objects.select_related(
            'organization',
        ).annotate(
            total_stock=db_models.Sum('inventories__stock')
        )


class OrganizationRepository:
    @staticmethod
    def get_organizations() -> db_models.QuerySet[models.Organization]:
        return models.Organization.objects.all()


class InventoryRepository:
    @staticmethod
    def get_inventories() -> db_models.QuerySet[models.Inventory]:
        return models.Inventory.objects.all()

    @staticmethod
    def change_stock(inventory: models.Inventory, value: int) -> models.Inventory:
        inventory.stock += value
        inventory.save()

        return inventory
