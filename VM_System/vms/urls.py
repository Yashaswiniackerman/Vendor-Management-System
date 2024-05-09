from django.urls import path
from .views import (
    VendorListCreateView,
    VendorDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderDetailView,
    VendorPerformanceView,
)

app_name = 'vms'

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor_list_create'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor_detail'),
    
    path('api/purchase_order/', PurchaseOrderListCreateView.as_view(), name='purchase_order_list_create'),
    path('api/purchase_order/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase_order_detail'),
    
    path('api/vendors/<int:pk/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
]