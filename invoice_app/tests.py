from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            'date': '2023-07-15',
            'invoice_no': 'RAH-002',
            'customer_name': 'Rahul',
            'details': [
                {
                    'description': 'Product 1',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'price': '20.00',
                },
                {
                    'description': 'Product 2',
                    'quantity': 1,
                    'unit_price': '15.00',
                    'price': '15.00',
                }
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.first().details.count(), 2)

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, 200)
