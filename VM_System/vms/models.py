from django.db import models
from django.db.models import JSONField
from django.conf import settings
from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .logics import update_vendor_performance_metrics  

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time =models.FloatField(default=0)
    fulfilment_rate = models.FloatField(default=0)
    
    def __str__(self) :
        return self.name
    
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) :
        return f"PO {self.po_number} - {self.vendor.name}"
    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg =models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfilment_rate = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    
    

