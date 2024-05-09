from django.db.models.signals import post_save
from django.dispatch import receiver
from .logics import update_vendor_performance_metrics
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    update_vendor_performance_metrics(instance.vendor)