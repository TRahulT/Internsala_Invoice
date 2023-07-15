from django.urls import include, path
from invoice_app.views import invoice_list, invoice_detail

urlpatterns = [
    path('invoices/', invoice_list, name='invoice-list'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice-detail'),
]
