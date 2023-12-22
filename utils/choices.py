from django.db.models import TextChoices


class OrderStatusChoices(TextChoices):
    SYNCED = 'synced'
    PROCESSING = 'processing'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'
    RETURNED = 'returned'
