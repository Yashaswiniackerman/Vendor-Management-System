from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .signals import *
from . serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.utils import timezone
from .logics import update_vendor_performance_metrics  

# Create your views here.

class VendorListCreateView(generics.ListCreateAPIView):
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer 
    
class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class VendorPerformanceView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    

@action(detail=True, methods=['post'])
def acknowledge(self, request, *args, **kwargs):
    
    purchase_order = self.get_object()
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()
    update_vendor_performance_metrics(purchase_order.vendor)
    return Response({'status': 'Acknowledged successfully'})


