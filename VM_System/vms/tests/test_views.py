from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import timezone
from vendors.models import Vendor, PurchaseOrder

class VendorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.vendor_data ={
            'name': 'Simbha',
            'contact': '123456789',
            'address': 'India',
            'vendor_code': 'V1',
        }
        
        self.vendor = Vendor.objects.create(**self.vendor_data)

    
    def test_get_vendor_list(self):
        
        url = reverse('vendor_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)   
        
    def test_get_vendor_detail(self):
        
        url = reverse('vendors:vendor_detail', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.vendor_data['name'])
        
class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name='Simbha',
            contact_details = '123456789',
            address = "India",
            vendor_code = 'V001',
            
        )
        
        self.po_data = {
            'po_number' : 'P0001',
            'vendor' : self.vendor,
            'order_date' : timezone.now(),
            'delivery_date': timezone.now() + timezone.timedelta(days=7),
            'items' : {'item1':5, 'item2': 10},
            'quantity' : 15,
            'status' : 'pending',
            'issue_date' : timezone.now(),
            
        }
        self.po = PurchaseOrder.objects.create(**self.po_data)
        
    
    def test_get_purchase_order(self):
        url = reverse('vendor:purchase_order_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        
    def test_get_purchase_order_detail(self):
        url = reverse('vendors:purchase_order_detail', args=[self.po.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['po_number'], self.po_data['po_number'])