# Invoice and InvoiceDetail Models DjangoRestframework

## Overview

This Django project contains two models: `Invoice` and `InvoiceDetail`, which are designed to manage and store information related to invoices and their details.

## Invoice Model

The `Invoice` model represents the basic information of an invoice, such as the date, invoice number, and customer name. It has the following fields:

- `date` (DateField): This field stores the date of the invoice.
- `invoice_no` (CharField): This field stores the invoice number, with a maximum length of 100 characters.
- `customer_name` (CharField): This field stores the customer's name, with a maximum length of 100 characters.

## InvoiceDetail Model

The `InvoiceDetail` model represents the line items or details of an invoice. Each `InvoiceDetail` is associated with a specific `Invoice` through a foreign key relationship. It has the following fields:

- `invoice` (ForeignKey): This field establishes a many-to-one relationship with the `Invoice` model, allowing multiple details to be linked to a single invoice. When an invoice is deleted, its associated details will also be deleted due to the `on_delete=models.CASCADE` option.
- `description` (CharField): This field stores a brief description of the item or service provided, with a maximum length of 100 characters.
- `quantity` (IntegerField): This field stores the quantity of the item or service.
- `unit_price` (DecimalField): This field stores the unit price of the item or service with a maximum of 10 digits and 2 decimal places.
- `price` (DecimalField): This field stores the total price for the line item with a maximum of 10 digits and 2 decimal places.

## Usage

To use these models in your Django project, follow these steps:

1. Create a Django app or use an existing one.
2. Copy the `Invoice` and `InvoiceDetail` model definitions into one of your app's `models.py` files.
3. Run `makemigrations` and `migrate` commands to create the database tables for these models:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. You can now use the `Invoice` and `InvoiceDetail` models to create, retrieve, update, and delete invoices and their details through the Django admin interface or programmatically in your views and serializers.

## Example

Here's an example of how to create an invoice and its associated details programmatically in Django:

```python
# Import necessary modules
from your_app.models import Invoice, InvoiceDetail

# Create an invoice
invoice = Invoice(date='2023-09-16', invoice_no='INV-001', customer_name='John Doe')
invoice.save()

# Create invoice details
detail1 = InvoiceDetail(
    invoice=invoice,
    description='Product A',
    quantity=5,
    unit_price=10.99,
    price=54.95
)
detail1.save()

detail2 = InvoiceDetail(
    invoice=invoice,
    description='Service B',
    quantity=2,
    unit_price=25.50,
    price=51.00
)
detail2.save()
```

You can adapt and extend this code to suit your specific project requirements.
