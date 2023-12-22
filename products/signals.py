from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from conf import settings
from products import models, constants


@receiver(post_save, sender=models.Inventory)
def change_stock(sender, instance, created, *args, **kwargs):
    if not created and instance.stock <= 0:
        send_mail(
            subject=constants.NO_INVENTORY_SUBJECT,
            message=constants.NO_INVENTORY_BODY.format(
                product_name=instance.product.name,
                warehouse_address=instance.warehouse.address,
                stock=instance.stock,
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(instance.product.organization.email,),
        )
